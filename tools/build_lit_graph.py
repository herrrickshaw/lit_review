#!/usr/bin/env python3
"""
build_lit_graph.py — build a knowledge graph of the literature-review corpus and
BRIDGE it to the code knowledge graph.

Two graphs already exist and have never been connected:
  A. the code graph  — ~/.graphify/global-graph.json (69 repos, tree-sitter AST nodes)
  B. the literature corpus — /Users/Shared/lit_review/**.md (the daily review's output)

Generic markdown extraction on (B) yields 68 shallow heading nodes, which links to
nothing. But the registers were written with a hard rule that every repo claim must
be cited as `file.py:LINE` — so the corpus already contains explicit, machine-readable
pointers INTO (A). This script parses those out and resolves them.

Node kinds emitted:
  paper      — an arXiv entry in LITERATURE_REGISTER.md, with its evidence grade
  queue_item — a numbered action in BACKTEST_QUEUE.md
  source     — a graded entry in masaladeutsch SOURCE_REGISTER.md
  commission — an open article idea in COMMISSION_QUEUE.md
  run        — one daily log under literature_runs/
  code       — a RESOLVED market-pipeline AST node (the bridge target)
  post       — a published masaladeutsch post, by slug

Edge kinds:
  cites      — literature node -> code node   (THE BRIDGE)
  motivates  — paper -> queue_item
  logged_in  — paper/source -> run
  covers     — commission -> post
"""
import json, os, re, collections

LIT = "/Users/Shared/lit_review"
GLOBAL = os.path.expanduser("~/.graphify/global-graph.json")
OUT = os.path.expanduser("~/.graphify/literature-graph.json")

# ---------------------------------------------------------------- code index
# Build source_file -> [(line, node)] so a `file.py:NNN` citation can be resolved to
# the innermost definition that ENCLOSES that line. graphify records only a start
# line per node, so "enclosing" = the nearest definition at or before the cited line.
print("indexing code graph ...")
G = json.load(open(GLOBAL))
by_file = collections.defaultdict(list)
repo_of = {}
for n in G["nodes"]:
    sf = n.get("source_file")
    loc = n.get("source_location") or ""
    if not sf or not loc.startswith("L"):
        continue
    try:
        ln = int(loc[1:].split("-")[0])
    except ValueError:
        continue
    by_file[(n.get("repo"), os.path.basename(sf))].append((ln, n))
    repo_of[n["id"]] = n.get("repo")
for k in by_file:
    by_file[k].sort(key=lambda t: t[0])
print(f"  {len(by_file)} (repo, file) buckets from {len(G['nodes'])} nodes")


def resolve(fname, line, prefer_repo="market-pipeline"):
    """Return the node whose definition most tightly encloses fname:line."""
    for repo in (prefer_repo, None):
        cands = (by_file.get((repo, fname)) if repo
                 else [v for (r, f), v in by_file.items() if f == fname])
        if not cands:
            continue
        flat = cands if repo else [x for sub in cands for x in sub]
        flat = sorted(flat, key=lambda t: t[0])
        best = None
        for ln, node in flat:
            if ln <= line:
                best = (ln, node)
            else:
                break
        if best:
            return best[1], best[0]
        if flat:                      # cited line precedes every def -> file node
            return flat[0][1], flat[0][0]
    return None, None


# ---------------------------------------------------------------- parse corpus
CITE = re.compile(r'([A-Za-z_][A-Za-z0-9_]*\.py):(\d+)')
ARXIV_H = re.compile(r'^###\s+(?:arXiv:)?(\d{4}\.\d{4,5})\s+—\s+(.+?)\s*$')
# The closing ** is optional at end-of-line: queue titles are hand-wrapped prose and
# four of them (20, 21, 23, 24) carry the bold across two lines, which a mandatory
# closing ** dropped silently. Non-greedy .+? still stops at a same-line ** first, so
# single-line titles parse exactly as before; a wrapped one keeps its first-line
# fragment, which the 120-char truncation below would have clipped anyway.
QUEUE_H = re.compile(r'^(\d+)\.\s+~?~?\*\*(.+?)(?:\*\*|$)')
SRC_H = re.compile(r'^###\s+(.+?)\s*$')
GRADE = re.compile(r'EVIDENCE-GRADE:\s*([\w/-]+)', re.I)  # n/a and medium-strong are real values
MDGRADE = re.compile(r'^-?\s*Grade:\s*\*\*(\w+)\*\*', re.I | re.M)
SLUG = re.compile(r'`([a-z0-9]+(?:-[a-z0-9]+){2,})`')

nodes, edges = [], []
seen = set()


def add(nid, **kw):
    if nid in seen:
        return nid
    seen.add(nid)
    nodes.append({"id": nid, **kw})
    return nid


def link(s, t, kind):
    edges.append({"source": s, "target": t, "kind": kind})


def sections(path, header_re):
    """Split a markdown file into (key, title, body, raw_header, part) by a heading
    regex. `part` carries the enclosing '## ' section so a paper filed under
    'Strong evidence' inherits that grade when it states none inline, and raw_header
    is kept so strikethrough (~~done~~) on the heading itself stays visible."""
    if not os.path.exists(path):
        return []
    lines = open(path).read().split("\n")
    out, cur, part = [], None, ""
    for ln in lines:
        if ln.startswith("## "):
            part = ln[3:].strip()
        m = header_re.match(ln)
        if m:
            if cur:
                out.append(cur)
            g = m.groups()
            cur = [g[0], g[-1], [], ln, part]
        elif cur:
            cur[2].append(ln)
    if cur:
        out.append(cur)
    return [(k, t, "\n".join(b), h, p) for k, t, b, h, p in out]


def section_grade(part):
    """Map the enclosing register section to an evidence grade."""
    p = part.lower()
    if p.startswith("strong evidence"):
        return "strong"
    if p.startswith("weak evidence") or "weak" in p:
        return "weak"
    if p.startswith("rejected"):
        return "rejected"
    return None


def wire_citations(owner_id, body, bucket):
    """Extract file.py:LINE from a body, resolve, and emit bridge edges."""
    hits = 0
    for fname, lnum in set(CITE.findall(body)):
        node, defline = resolve(fname, int(lnum))
        if node is None:
            bucket["unresolved"].append(f"{fname}:{lnum}")
            continue
        cid = add(node["id"], kind="code", label=node.get("label"),
                  file=node.get("source_file"), line=defline,
                  repo=node.get("repo"))
        link(owner_id, cid, "cites")
        bucket["resolved"].append((fname, int(lnum), node.get("label")))
        hits += 1
    return hits


stats = {"resolved": [], "unresolved": []}

# --- papers -----------------------------------------------------------------
reg = f"{LIT}/market-pipeline/LITERATURE_REGISTER.md"
papers = sections(reg, ARXIV_H)
for aid, title, body, _hdr, part in papers:
    g = GRADE.search(body)
    grade = g.group(1).lower() if g else (section_grade(part) or "unstated")
    pid = add(f"paper::{aid}", kind="paper", label=aid, title=title.strip(),
              grade=grade, section=part, side="market-pipeline")
    wire_citations(pid, body, stats)

# --- backtest queue ---------------------------------------------------------
q = f"{LIT}/market-pipeline/BACKTEST_QUEUE.md"
qitems = sections(q, QUEUE_H)
for num, title, body, hdr, _part in qitems:
    # strikethrough lives on the heading line, and a DONE stamp may sit on either
    # the heading or the first body lines — check both, not just the body.
    done = "~~" in hdr or "**DONE" in hdr or "**DONE" in body[:400]
    qid = add(f"queue::{num}", kind="queue_item", label=f"#{num}",
              title=re.sub(r'[*~]+', '', title)[:120],
              status=("done" if done else "open"), side="market-pipeline")
    wire_citations(qid, body, stats)
    for aid in set(re.findall(r'(\d{4}\.\d{4,5})', body)):
        if f"paper::{aid}" in seen:
            link(f"paper::{aid}", qid, "motivates")

# --- daily runs -------------------------------------------------------------
rundir = f"{LIT}/market-pipeline/literature_runs"
for fn in sorted(os.listdir(rundir)) if os.path.isdir(rundir) else []:
    if not fn.endswith(".md"):
        continue
    day = fn[:-3]
    body = open(os.path.join(rundir, fn)).read()
    rid = add(f"run::{day}", kind="run", label=day, side="both")
    for aid in set(re.findall(r'(\d{4}\.\d{4,5})', body)):
        if f"paper::{aid}" in seen:
            link(f"paper::{aid}", rid, "logged_in")
    wire_citations(rid, body, stats)

# --- masaladeutsch sources --------------------------------------------------
src = f"{LIT}/masaladeutsch/SOURCE_REGISTER.md"
for key, title, body, _h, _p in sections(src, SRC_H):
    g = MDGRADE.search(body)
    grade = (g.group(1).lower() if g else "unstated")
    if len(title) < 8:
        continue
    sid = add(f"source::{title[:60]}", kind="source", label=title[:70],
              grade=grade, side="masaladeutsch")
    for slug in set(SLUG.findall(body)):
        if slug.endswith(".py") or "/" in slug:
            continue
        pid = add(f"post::{slug}", kind="post", label=slug, side="masaladeutsch")
        link(sid, pid, "covers")

# --- commission queue -------------------------------------------------------
cq = f"{LIT}/masaladeutsch/COMMISSION_QUEUE.md"
if os.path.exists(cq):
    txt = open(cq).read()
    for m in re.finditer(r'^- \[( |x)\] (.+?)$', txt, re.M):
        state, title = m.group(1), m.group(2).strip()
        blk = txt[m.end():m.end() + 2500]
        cid = add(f"commission::{title[:60]}", kind="commission", label=title[:80],
                  status=("done" if state == "x" else "open"), side="masaladeutsch")
        for slug in set(SLUG.findall(blk)):
            if slug.endswith(".py") or "/" in slug:
                continue
            pid = add(f"post::{slug}", kind="post", label=slug, side="masaladeutsch")
            link(cid, pid, "covers")

# ---------------------------------------------------------------- report
kinds = collections.Counter(n["kind"] for n in nodes)
ekinds = collections.Counter(e["kind"] for e in edges)
bridge = [e for e in edges if e["kind"] == "cites"]
bridged_files = collections.Counter(
    n["file"] for n in nodes if n["kind"] == "code" and n.get("file"))

meta = {
    "nodes": len(nodes), "edges": len(edges),
    "node_kinds": dict(kinds), "edge_kinds": dict(ekinds),
    "bridge_edges": len(bridge),
    "distinct_code_targets": sum(1 for n in nodes if n["kind"] == "code"),
    "citations_resolved": len(stats["resolved"]),
    "citations_unresolved": sorted(set(stats["unresolved"])),
    "most_cited_files": bridged_files.most_common(15),
}
json.dump({"directed": True, "nodes": nodes, "edges": edges, "meta": meta},
          open(OUT, "w"), indent=1)

print(f"\nLITERATURE GRAPH -> {OUT}")
print(f"  {len(nodes)} nodes / {len(edges)} edges")
print(f"  node kinds : {dict(kinds)}")
print(f"  edge kinds : {dict(ekinds)}")
print(f"\nBRIDGE to code graph: {len(bridge)} 'cites' edges -> "
      f"{meta['distinct_code_targets']} distinct code nodes")
print(f"  citations resolved   : {len(stats['resolved'])}")
print(f"  citations unresolved : {len(meta['citations_unresolved'])} "
      f"{meta['citations_unresolved'][:8]}")
print("\n  most-cited files (literature -> code):")
for f, c in bridged_files.most_common(12):
    print(f"    {c:3d}  {f}")
