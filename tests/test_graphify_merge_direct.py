import json
import os
import subprocess
import types

import pytest


def write_graph(home, repo, nodes, edges=None, key="edges"):
    d = home / repo / "graphify-out"
    d.mkdir(parents=True)
    (d / "graph.json").write_text(json.dumps({"nodes": nodes, key: edges or []}))
    return d / "graph.json"


@pytest.fixture
def fake_git(monkeypatch):
    """subprocess.run -> remote URL per checkout dir (None -> empty stdout, 'ERR' -> raises)."""
    remotes = {}

    def run(cmd, capture_output, text, timeout):
        assert cmd[:3] == ["git", "-C", cmd[2]] and cmd[3:] == ["remote", "get-url", "origin"]
        v = remotes.get(cmd[2], "")
        if v == "ERR":
            raise subprocess.TimeoutExpired(cmd, timeout)
        return types.SimpleNamespace(stdout=v + "\n")

    monkeypatch.setattr(subprocess, "run", run)
    return remotes


def setup(sandbox, batch=(), clones=None):
    sandbox.write_json(sandbox.home / ".ruflo/logs/graphify_batch.json", list(batch))
    if clones is not None:
        sandbox.write_json(sandbox.home / ".ruflo/logs/graphify_clones.json", clones)


def merged(sandbox):
    return json.loads((sandbox.home / ".graphify/global-graph.json").read_text())


def index(sandbox):
    return json.loads((sandbox.home / ".graphify/global-index.json").read_text())


def test_namespacing_and_cross_repo_index(sandbox, fake_git, capsys):
    h = sandbox.home
    write_graph(h, "alpha", [{"id": "n1", "label": "parse_frame()"}, {"name": "named-only"}, {"label": "label-only"}, "junk"],
                [{"source": "n1", "target": "named-only", "kind": "calls"}, {"from": "n1", "to": "ghost"}, "junk"])
    write_graph(h, "beta", [{"id": "m1", "label": "parse_frame()"}, {"id": "m2", "label": "abc"}], key="links")
    setup(sandbox, [{"repo": "alpha", "status": "ok"}, {"repo": "beta", "status": "ok"}, {"repo": "fail", "status": "failed"}])
    fake_git[str(h / "alpha")] = "git@github.com:Owner/Alpha.git"
    fake_git[str(h / "beta")] = "https://github.com/Owner/Beta"
    sandbox("graphify_merge_direct.py")
    g = merged(sandbox)
    ids = {n["id"]: n["repo"] for n in g["nodes"]}
    assert ids == {"alpha::n1": "alpha", "alpha::named-only": "alpha", "alpha::label-only": "alpha",
                   "beta::m1": "beta", "beta::m2": "beta"}                                # non-dict node skipped
    assert g["directed"] is True and g["meta"] == {"repos": 2, "shared_symbols": 1}
    e = [x for x in g["edges"]]
    assert {(x["source"], x["target"]) for x in e} == {("alpha::n1", "alpha::named-only"), ("alpha::n1", "alpha::ghost")}
    assert all(x["repo"] == "alpha" for x in e)                                               # 'from'/'to' keys accepted
    idx = index(sandbox)
    assert idx["repos"] == {"alpha": 4, "beta": 2}
    assert idx["totals"] == {"nodes": 5, "edges": 2, "cross_repo_links": 1}
    assert idx["shared_symbols"] == {"parse_frame()": ["alpha", "beta"]}                      # 'abc' (<4 chars) never indexed
    out = capsys.readouterr().out
    assert "MERGED 2 repos -> 5 nodes, 2 edges (1 cross-repo links)" in out
    assert "parse_frame()" in out and "in 2 repos: alpha, beta" in out


def test_local_checkout_beats_clone_of_same_remote(sandbox, fake_git, capsys):
    h = sandbox.home
    write_graph(h, "local-dir", [{"id": "real1"}, {"id": "real2"}, {"id": "real3"}])
    clone_graph = write_graph(h / "clones", "clone-name", [{"id": "stub"}])
    setup(sandbox, [{"repo": "local-dir", "status": "ok"}],
          clones=[{"repo": "clone-name", "status": "ok", "path": str(h / "clones" / "clone-name"), "graph": str(clone_graph)}])
    fake_git[str(h / "local-dir")] = "https://github.com/Owner/Same.git"
    fake_git[str(h / "clones" / "clone-name")] = "https://github.com/owner/same"            # same remote, different case/.git
    sandbox("graphify_merge_direct.py")
    assert index(sandbox)["repos"] == {"local-dir": 3}


def test_clone_used_when_no_local_and_distinct_remotes_kept(sandbox, fake_git):
    h = sandbox.home
    g1 = write_graph(h / "clones", "c1", [{"id": "a"}])
    g2 = write_graph(h / "clones", "c2", [{"id": "b"}, {"id": "c"}])
    g3 = write_graph(h / "clones", "c3", [{"id": "d"}])
    setup(sandbox, [], clones=[
        {"repo": "c1", "status": "ok", "path": str(h / "clones/c1"), "graph": str(g1)},
        {"repo": "c2", "status": "ok", "path": str(h / "clones/c2"), "graph": str(g2)},
        {"repo": "c3", "status": "failed", "path": str(h / "clones/c3"), "graph": str(g3)},
        {"repo": "c4", "status": "ok", "path": "", "graph": str(h / "clones/missing/graphify-out/graph.json")}])
    fake_git[str(h / "clones/c1")] = "https://github.com/o/one"
    fake_git[str(h / "clones/c2")] = "https://github.com/o/two"
    sandbox("graphify_merge_direct.py")
    assert index(sandbox)["repos"] == {"c1": 1, "c2": 2}                    # failed clone and missing graph skipped


def test_no_remote_falls_back_to_realpath_key(sandbox, fake_git):
    h = sandbox.home
    write_graph(h, "norem", [{"id": "a"}])
    write_graph(h, "boom", [{"id": "b"}, {"id": "c"}])
    setup(sandbox, [{"repo": "norem", "status": "ok"}, {"repo": "boom", "status": "ok"}])
    fake_git[str(h / "boom")] = "ERR"                       # git raising is treated as 'no remote'
    sandbox("graphify_merge_direct.py")
    assert index(sandbox)["repos"] == {"norem": 1, "boom": 2}


def test_market_pipeline_included_by_path(sandbox, fake_git):
    h = sandbox.home
    write_graph(h, "market-pipeline", [{"id": "a"}, {"id": "b"}])
    setup(sandbox, [])
    sandbox("graphify_merge_direct.py")
    assert index(sandbox)["repos"] == {"market-pipeline": 2}


def test_corrupt_graph_is_skipped(sandbox, fake_git, capsys):
    h = sandbox.home
    write_graph(h, "good", [{"id": "a"}])
    bad = h / "bad" / "graphify-out"
    bad.mkdir(parents=True)
    (bad / "graph.json").write_text("{not json")
    setup(sandbox, [{"repo": "good", "status": "ok"}, {"repo": "bad", "status": "ok"}])
    fake_git[str(h / "good")] = "https://github.com/o/good"
    fake_git[str(h / "bad")] = "https://github.com/o/bad"
    sandbox("graphify_merge_direct.py")
    assert index(sandbox)["repos"] == {"good": 1}
    assert "skip bad:" in capsys.readouterr().out


def test_shared_symbols_sorted_by_repo_count_and_capped(sandbox, fake_git):
    h = sandbox.home
    batch = []
    for i in range(4):
        labels = [{"id": f"x{i}", "label": "everywhere()"}]
        if i < 2:
            labels.append({"id": f"y{i}", "label": "in_two()"})
        write_graph(h, f"r{i}", labels)
        batch.append({"repo": f"r{i}", "status": "ok"})
        fake_git[str(h / f"r{i}")] = f"https://github.com/o/r{i}"
    setup(sandbox, batch)
    sandbox("graphify_merge_direct.py")
    shared = index(sandbox)["shared_symbols"]
    assert list(shared) == ["everywhere()", "in_two()"] and shared["everywhere()"] == ["r0", "r1", "r2", "r3"]


def test_repo_names_use_graph_directory_not_remote(sandbox, fake_git):
    h = sandbox.home
    write_graph(h, "BazaarTalks-cpp", [{"id": "a"}])
    setup(sandbox, [{"repo": "BazaarTalks-cpp", "status": "ok"}])
    fake_git[str(h / "BazaarTalks-cpp")] = "https://github.com/o/Bazartalks_Py2Cplus.git"
    sandbox("graphify_merge_direct.py")
    assert list(index(sandbox)["repos"]) == ["BazaarTalks-cpp"]


def test_remote_of_normalisation(sandbox, fake_git):
    h = sandbox.home
    setup(sandbox, [])
    ns = sandbox("graphify_merge_direct.py")
    for url, want in [("git@github.com:Owner/Repo.git", "owner/repo"), ("https://github.com/Owner/Repo/", "owner/repo"),
                      ("https://gitlab.com/a/b/c.git", "b/c"), ("", None)]:
        fake_git["/d"] = url
        assert ns["remote_of"]("/d") == want
    fake_git["/d"] = "ERR"
    assert ns["remote_of"]("/d") is None


def test_offer_prefers_lower_priority_and_ignores_missing_graph(sandbox, fake_git, tmp_path):
    setup(sandbox, [])
    ns = sandbox("graphify_merge_direct.py")
    gj = tmp_path / "g.json"
    gj.write_text("{}")
    fake_git["/d"] = "https://github.com/o/r"
    ns["offer"]("clone", "/d", str(gj), 1)
    ns["offer"]("local", "/d", str(gj), 0)
    ns["offer"]("late-clone", "/d", str(gj), 1)
    ns["offer"]("ghost", "/d", str(tmp_path / "missing.json"), 0)
    assert ns["by_remote"]["o/r"][2] == "local" and len(ns["by_remote"]) == 1
