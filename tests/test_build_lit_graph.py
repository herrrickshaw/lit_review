import json

import pytest


def node(i, repo, sf, loc, label=None):
    return {"id": i, "repo": repo, "source_file": sf, "source_location": loc, "label": label or i}


CODE_NODES = [
    node("mp::a", "market-pipeline", "/x/scan.py", "L10", "scan_top()"),
    node("mp::b", "market-pipeline", "/x/scan.py", "L50-80", "scan_bottom()"),
    node("mp::c", "market-pipeline", "/x/scan.py", "L5", "scan_head()"),
    node("o::d", "other-repo", "/y/helper.py", "L7", "helper()"),
    node("bad1", "market-pipeline", "/x/zzz.py", "Lxyz"),      # unparseable line -> skipped
    node("bad2", "market-pipeline", None, "L3"),               # no file -> skipped
    node("bad3", "market-pipeline", "/x/q.py", None),          # no location -> skipped
    node("bad4", "market-pipeline", "/x/q.py", "C3"),          # not an L location -> skipped
]

REGISTER = """# Register
## Strong evidence
### arXiv:2401.00001 — Momentum paper
Cites scan.py:60 and helper.py:9 plus missing.py:1. EVIDENCE-GRADE: Medium-Strong

### 2401.00002 — Inline-less paper
Body with scan.py:2 only.
## Weak evidence
### arXiv:2401.00003 — Weak one
nothing
## Rejected
### arXiv:2401.00004 — Rejected one
nothing
## Misc
### arXiv:2401.00005 — Misc one
nothing
"""

QUEUE = """# Queue
1. **First action**
   cites scan.py:12 (see 2401.00001 and 2401.99999)
2. ~~**Struck action**~~ done long ago
3. **DONE: third** body
4. **Fourth wraps
   across lines** and mentions 2401.00002
5. **Fifth** details
   **DONE** on first lines
"""

SOURCES = """# Sources
### Short
Grade: **A**
### Ministry of Statistics release
- Grade: **B**
Related posts: `my-first-post-slug`, `two-part`, `a/b-c-d` and `file-name-x.py`
### Another long title here
no grade line
"""

COMMISSION = """- [ ] Write about steel
  see `steel-trade-flows` and `foo-bar-baz`
- [x] Done article
  `done-article-slug`
not a list line
"""


def build(sandbox, queue=QUEUE, register=REGISTER, runs=True, sources=True, commission=True, code=CODE_NODES):
    sandbox.write_json(sandbox.home / ".graphify/global-graph.json", {"nodes": code, "edges": []})
    mp = sandbox.lit / "market-pipeline"
    mp.mkdir(parents=True, exist_ok=True)
    if register is not None:
        (mp / "LITERATURE_REGISTER.md").write_text(register)
    if queue is not None:
        (mp / "BACKTEST_QUEUE.md").write_text(queue)
    if runs:
        (mp / "literature_runs").mkdir(exist_ok=True)
        (mp / "literature_runs" / "2026-08-23.md").write_text("Reviewed 2401.00001 and 2401.55555; see scan.py:70")
        (mp / "literature_runs" / "notes.txt").write_text("ignored")
    md = sandbox.lit / "masaladeutsch"
    md.mkdir(exist_ok=True)
    if sources:
        (md / "SOURCE_REGISTER.md").write_text(SOURCES)
    if commission:
        (md / "COMMISSION_QUEUE.md").write_text(COMMISSION)
    return sandbox("build_lit_graph.py")


def test_resolve_picks_enclosing_definition(sandbox):
    ns = build(sandbox)
    resolve = ns["resolve"]
    assert resolve("scan.py", 10)[0]["id"] == "mp::a" and resolve("scan.py", 10)[1] == 10      # exact line
    assert resolve("scan.py", 49)[0]["id"] == "mp::a"                                          # nearest definition at or before
    assert resolve("scan.py", 50)[0]["id"] == "mp::b"
    assert resolve("scan.py", 9999)[0]["id"] == "mp::b"
    assert resolve("scan.py", 1)[0]["id"] == "mp::c" and resolve("scan.py", 1)[1] == 5         # before every def -> first node
    assert resolve("helper.py", 100)[0]["id"] == "o::d"                                        # falls back to other repos
    assert resolve("nope.py", 1) == (None, None)
    assert resolve("helper.py", 100, prefer_repo="other-repo")[0]["id"] == "o::d"


def test_index_skips_unusable_nodes(sandbox, capsys):
    ns = build(sandbox)
    assert set(k for k in ns["by_file"]) == {("market-pipeline", "scan.py"), ("other-repo", "helper.py")}
    assert "2 (repo, file) buckets from 8 nodes" in capsys.readouterr().out
    assert [ln for ln, _ in ns["by_file"][("market-pipeline", "scan.py")]] == [5, 10, 50]       # sorted


def test_papers_grades_and_sections(sandbox):
    ns = build(sandbox)
    n = {x["id"]: x for x in ns["nodes"]}
    assert n["paper::2401.00001"]["grade"] == "medium-strong"        # inline grade (hyphenated value) wins over section
    assert n["paper::2401.00001"]["title"] == "Momentum paper"
    assert n["paper::2401.00002"]["grade"] == "strong"               # inherited from '## Strong evidence'
    assert n["paper::2401.00003"]["grade"] == "weak"
    assert n["paper::2401.00004"]["grade"] == "rejected"
    assert n["paper::2401.00005"]["grade"] == "unstated"
    assert n["paper::2401.00001"]["section"] == "Strong evidence" and n["paper::2401.00001"]["side"] == "market-pipeline"


def test_citation_bridge_edges_and_unresolved(sandbox):
    ns = build(sandbox)
    cites = {(e["source"], e["target"]) for e in ns["edges"] if e["kind"] == "cites"}
    assert ("paper::2401.00001", "mp::b") in cites                     # scan.py:60 -> definition at line 50
    assert ("paper::2401.00001", "o::d") in cites                      # helper.py:9 resolved via fallback
    assert ("paper::2401.00002", "mp::c") in cites                     # scan.py:2 precedes every def
    assert ("queue::1", "mp::a") in cites and ("run::2026-08-23", "mp::b") in cites
    code = {x["id"]: x for x in ns["nodes"] if x["kind"] == "code"}
    assert code["mp::b"]["label"] == "scan_bottom()" and code["mp::b"]["line"] == 50 and code["mp::b"]["repo"] == "market-pipeline"
    assert ns["stats"]["unresolved"] == ["missing.py:1"]
    assert ns["meta"]["citations_unresolved"] == ["missing.py:1"]
    assert ns["meta"]["bridge_edges"] == len(cites) and ns["meta"]["distinct_code_targets"] == len(code)


def test_queue_items_status_and_motivates(sandbox):
    ns = build(sandbox)
    n = {x["id"]: x for x in ns["nodes"]}
    assert {k: v["status"] for k, v in n.items() if k.startswith("queue::")} == {
        "queue::1": "open", "queue::2": "done", "queue::3": "done", "queue::4": "open", "queue::5": "done"}
    assert n["queue::1"]["title"] == "First action" and n["queue::2"]["title"] == "Struck action"
    assert n["queue::4"]["title"] == "Fourth wraps"                    # wrapped bold keeps its first-line fragment
    mot = {(e["source"], e["target"]) for e in ns["edges"] if e["kind"] == "motivates"}
    assert mot == {("paper::2401.00001", "queue::1"), ("paper::2401.00002", "queue::4")}    # unknown arXiv ids ignored


def test_runs_logged_in_edges(sandbox):
    ns = build(sandbox)
    n = {x["id"]: x for x in ns["nodes"]}
    assert n["run::2026-08-23"]["side"] == "both" and "run::notes" not in n
    logged = {(e["source"], e["target"]) for e in ns["edges"] if e["kind"] == "logged_in"}
    assert logged == {("paper::2401.00001", "run::2026-08-23")}


def test_sources_and_commissions_cover_posts(sandbox):
    ns = build(sandbox)
    n = {x["id"]: x for x in ns["nodes"]}
    src = [x for x in ns["nodes"] if x["kind"] == "source"]
    assert [s["label"] for s in src] == ["Ministry of Statistics release", "Another long title here"]   # 'Short' (<8 chars) dropped
    assert src[0]["grade"] == "b" and src[1]["grade"] == "unstated" and src[0]["side"] == "masaladeutsch"
    covers = {(e["source"], e["target"]) for e in ns["edges"] if e["kind"] == "covers"}
    assert ("source::Ministry of Statistics release", "post::my-first-post-slug") in covers
    assert ("source::Ministry of Statistics release", "post::two-part") not in covers          # needs >= 3 hyphen segments
    assert not any(t in ("post::a/b-c-d", "post::file-name-x.py") for _, t in covers)
    assert ("commission::Write about steel", "post::steel-trade-flows") in covers
    assert n["commission::Write about steel"]["status"] == "open" and n["commission::Done article"]["status"] == "done"
    assert ("commission::Done article", "post::done-article-slug") in covers


def test_output_file_and_summary(sandbox, capsys):
    ns = build(sandbox)
    out = json.loads((sandbox.home / ".graphify/literature-graph.json").read_text())
    assert out["directed"] is True and len(out["nodes"]) == len(ns["nodes"]) and out["meta"] == json.loads(json.dumps(ns["meta"]))
    assert out["meta"]["node_kinds"]["paper"] == 5 and out["meta"]["node_kinds"]["queue_item"] == 5
    assert out["meta"]["most_cited_files"][0] == ["/x/scan.py", 3]     # distinct code nodes per file
    text = capsys.readouterr().out
    assert "LITERATURE GRAPH ->" in text and "BRIDGE to code graph:" in text and "citations unresolved : 1 ['missing.py:1']" in text
    assert "  most-cited files (literature -> code):" in text


def test_missing_corpus_files_are_tolerated(sandbox):
    ns = build(sandbox, queue=None, register=None, runs=False, sources=False, commission=False)
    assert ns["nodes"] == [] and ns["edges"] == [] and ns["meta"]["bridge_edges"] == 0


def test_duplicate_nodes_are_not_added_twice(sandbox):
    ns = build(sandbox)
    ids = [x["id"] for x in ns["nodes"]]
    assert len(ids) == len(set(ids))
    assert ns["add"]("paper::2401.00001", kind="x") == "paper::2401.00001"
    assert len(ns["nodes"]) == len(ids)


def test_section_grade_mapping(sandbox):
    sg = build(sandbox)["section_grade"]
    assert sg("Strong evidence (3)") == "strong" and sg("weak evidence") == "weak" and sg("Mostly weak signals") == "weak"
    assert sg("Rejected / retracted") == "rejected" and sg("Other") is None and sg("") is None


def test_sections_keeps_header_and_part(sandbox):
    ns = build(sandbox)
    p = sandbox.lit / "x.md"
    p.write_text("## Part A\n### K1 — T1\nline\n## Part B\n### K2 — T2\nmore\n")
    import re
    out = ns["sections"](str(p), re.compile(r"^###\s+(\w+)\s+—\s+(.+?)\s*$"))
    assert out == [("K1", "T1", "line\n## Part B", "### K1 — T1", "Part A"), ("K2", "T2", "more\n", "### K2 — T2", "Part B")]
    assert ns["sections"](str(sandbox.lit / "none.md"), re.compile("x")) == []


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="build_lit_graph.py: sections() puts only the lines AFTER a heading in `body`, so a "
                          "file.py:LINE citation or arXiv id written on the numbered queue item's own first line "
                          "is never wired (no 'cites' / 'motivates' edge)")
def test_citation_on_queue_heading_line_is_wired(sandbox):
    ns = build(sandbox, queue="1. **Action** cites scan.py:12 and 2401.00001\n")
    edges = {(e["source"], e["target"], e["kind"]) for e in ns["edges"]}
    assert ("queue::1", "mp::a", "cites") in edges and ("paper::2401.00001", "queue::1", "motivates") in edges
