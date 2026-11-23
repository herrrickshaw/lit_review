import pytest


def n(i, repo, label, ft="code", sf=None):
    return {"id": i, "repo": repo, "label": label, "file_type": ft, "source_file": sf}


def setup(sandbox, nodes, edges=(), batch=(), clones=()):
    sandbox.write_json(sandbox.home / ".graphify/global-graph.json", {"nodes": list(nodes), "edges": list(edges)})
    sandbox.write_json(sandbox.home / ".ruflo/logs/graphify_batch.json", list(batch))
    sandbox.write_json(sandbox.home / ".ruflo/logs/graphify_clones.json", list(clones))


def test_header_and_stub_sections(sandbox, capsys):
    nodes = [n("a", "repo-local", "x()"), n("b", "repo-local", "y()"), n("c", "tiny-clone", "z()")]
    batch = [{"repo": "dir/repo-local", "status": "ok"}, {"repo": "broken-repo", "status": "failed"}]
    clones = [{"repo": "repo-local", "status": "ok", "nodes": 13}, {"repo": "tiny-clone", "status": "ok", "nodes": 12},
              {"repo": "big-clone", "status": "ok", "nodes": 40}, {"repo": "zero-clone", "status": "ok", "nodes": 0}]
    setup(sandbox, nodes, batch=batch, clones=clones)
    sandbox("diagnose.py")
    out = capsys.readouterr().out
    assert out.startswith("graph: 3 nodes / 0 edges / 2 repos")
    s1 = out.split("2. DUPLICATED")[0]
    assert "repos with BOTH a local checkout and a gh-clone: 1" in s1
    assert "repo-local" in s1 and "graph=2" in s1 and "clone_had=13" in s1
    assert "     12 nodes  tiny-clone" in s1
    assert "big-clone" not in s1 and "zero-clone" not in s1            # >= 40 nodes and 0 nodes are not 'thin'


def test_thin_clone_listing_boundaries(sandbox, capsys):
    clones = [{"repo": "c39", "status": "ok", "nodes": 39}, {"repo": "c40", "status": "ok", "nodes": 40},
              {"repo": "c1", "status": "ok", "nodes": 1}, {"repo": "c0", "status": "ok", "nodes": 0}]
    setup(sandbox, [n("a", "r", "x()")], clones=clones)
    sandbox("diagnose.py")
    s1 = capsys.readouterr().out.split("2. DUPLICATED")[0]
    thin = s1.split("not real:")[1]
    assert "c39" in thin and "c1" in thin and "c40" not in thin and "c0" not in thin
    assert thin.index("c1") < thin.index("c39")             # sorted ascending by node count


def test_duplicate_symbols(sandbox, capsys):
    nodes = []
    for r in ("r1", "r2", "r3", "r4", "r5"):
        nodes.append(n(f"{r}::pf", r, "parse_frame()"))                          # 5 repos
        nodes.append(n(f"{r}::main", r, "main()"))                               # noise
        nodes.append(n(f"{r}::short", r, "a_b()"))                               # too short (<= 8 chars)
    for r in ("r1", "r2"):
        nodes.append(n(f"{r}::two", r, "only_in_two_repos()"))                   # < 3 repos
    for r in ("r1", "r2", "r3"):
        nodes.append(n(f"{r}::exact", r, "len_9_abc()"))                         # 11 chars: counted
        nodes.append(n(f"{r}::doc", r, "Readme section", ft="document"))         # not code
        nodes.append(n(f"{r}::noparen", r, "plain_name_without_parens"))
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s2 = capsys.readouterr().out.split("2. DUPLICATED SYMBOLS")[1].split("3. GOD FILES")[0]
    assert "named functions defined in >=3 repos: 2" in s2
    assert "5 repos  parse_frame()" in s2 and "3 repos  len_9_abc()" in s2
    assert "main()" not in s2 and "only_in_two_repos" not in s2 and "a_b()" not in s2
    assert "r1, r2, r3, r4 …" in s2                                                # first four then an ellipsis
    assert s2.index("parse_frame") < s2.index("len_9_abc")


def test_duplicate_symbols_length_boundary(sandbox, capsys):
    nodes = [n(f"{r}::x", r, label) for r in ("a", "b", "c") for label in ("abcdef()", "abcdefg()")]
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s2 = capsys.readouterr().out.split("2. DUPLICATED SYMBOLS")[1].split("3. GOD")[0]
    assert "abcdefg()" in s2 and "abcdef()" not in s2.replace("abcdefg()", "")          # 8 chars rejected, 9 accepted


def test_god_files(sandbox, capsys):
    nodes = []
    for i in range(8):                       # 8 files -> eligible repo; median 1 def per file
        nodes.append(n(f"r::f{i}", "r", f"fn{i}()", sf=f"small{i}.py"))
    nodes += [n(f"r::g{i}", "r", f"g{i}()", sf="huge.py") for i in range(45)]         # 45 defs, >= max(40, median*8)
    nodes += [n(f"r::h{i}", "r", f"h{i}()", sf="big.py") for i in range(39)]          # 39 defs: below the 40 floor
    for i in range(7):                       # a repo with < 8 files is skipped entirely
        nodes.append(n(f"q::{i}", "q", f"q{i}()", sf=f"f{i}.py"))
    nodes += [n(f"q::big{i}", "q", f"qb{i}()", sf="f0.py") for i in range(60)]
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s3 = capsys.readouterr().out.split("3. GOD FILES")[1].split("4. ORPHAN")[0]
    assert "45 defs (repo median  1)  r/huge.py" in s3
    assert "big.py" not in s3 and "q/f0.py" not in s3
    assert "total flagged: 1" in s3


def test_god_file_threshold_scales_with_median(sandbox, capsys):
    nodes = []
    for i in range(8):                       # median 10 defs/file -> threshold 80
        nodes += [n(f"r::{i}:{j}", "r", f"fn{i}_{j}()", sf=f"f{i}.py") for j in range(10)]
    nodes += [n(f"r::a{j}", "r", f"a{j}()", sf="at79.py") for j in range(79)]
    nodes += [n(f"r::b{j}", "r", f"b{j}()", sf="at80.py") for j in range(80)]
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s3 = capsys.readouterr().out.split("3. GOD FILES")[1].split("4. ORPHAN")[0]
    assert "at80.py" in s3 and "at79.py" not in s3


def test_orphans_and_ungraphed(sandbox, capsys):
    nodes = [n(f"a{i}", "big-repo", f"f{i}()") for i in range(100)]
    edges = [{"source": f"a{i}", "target": f"a{i + 1}"} for i in range(0, 60)]        # a0..a60 linked -> 39 orphans
    nodes += [n(f"s{i}", "small-repo", f"s{i}()") for i in range(59)]                  # < 60 code nodes: not reported
    nodes += [n("d", "big-repo", "Doc", ft="document")]
    batch = [{"repo": "ok-repo", "status": "ok"}, {"repo": "bad-repo", "status": "timeout"}, {"repo": "gone", "status": "missing"}]
    setup(sandbox, nodes, edges=edges, batch=batch)
    sandbox("diagnose.py")
    out = capsys.readouterr().out
    s4 = out.split("4. ORPHAN DEFINITIONS")[1].split("5. LOCAL REPOS")[0]
    assert "  39.0%     39/100    unreferenced defs  big-repo" in s4
    assert "small-repo" not in s4
    s5 = out.split("5. LOCAL REPOS THAT PRODUCED ZERO NODES")[1]
    assert "[timeout]  bad-repo" in s5 and "[missing]  gone" in s5 and "ok-repo" not in s5


def test_thin_clone_list_capped_at_15(sandbox, capsys):
    clones = [{"repo": f"c{i:02d}", "status": "ok", "nodes": i + 1} for i in range(20)]
    setup(sandbox, [n("a", "r", "x()")], clones=clones)
    sandbox("diagnose.py")
    thin = capsys.readouterr().out.split("not real:")[1].split("2. DUPLICATED")[0]
    assert len([l for l in thin.splitlines() if " nodes  c" in l]) == 15 and "c14" in thin and "c15" not in thin


def test_duplicate_list_capped_at_18(sandbox, capsys):
    nodes = [n(f"{r}::s{i}", r, f"symbol_number_{i:02d}()") for r in ("a", "b", "c") for i in range(25)]
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s2 = capsys.readouterr().out.split("2. DUPLICATED SYMBOLS")[1].split("3. GOD FILES")[0]
    assert "named functions defined in >=3 repos: 25" in s2
    assert len([l for l in s2.splitlines() if " repos  symbol_number_" in l]) == 18


def test_god_file_report_capped_at_14_and_repo_needs_8_files(sandbox, capsys):
    nodes = []
    for repo in ("r1", "r2"):                                      # 8 files each: 7 small + 1 god -> exactly the minimum
        for i in range(7):
            nodes.append(n(f"{repo}::s{i}", repo, f"s{i}()", sf=f"s{i}.py"))
        nodes += [n(f"{repo}::g{i}", repo, f"g{i}()", sf="god.py") for i in range(50)]
    nodes += [n(f"w{j}::{i}", f"w{j}", f"w{j}f{i}()", sf="god.py") for j in range(14) for i in range(50)]
    for j in range(14):                                            # pad each w-repo to 8 files so it is eligible
        nodes += [n(f"w{j}::p{k}", f"w{j}", f"p{k}()", sf=f"p{k}.py") for k in range(7)]
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s3 = capsys.readouterr().out.split("3. GOD FILES")[1].split("4. ORPHAN")[0]
    assert "total flagged: 16" in s3
    assert len([l for l in s3.splitlines() if "defs (repo median" in l]) == 14


def test_orphan_report_floor_60_and_cap_12(sandbox, capsys):
    nodes = []
    for i in range(14):
        nodes += [n(f"o{i}::{k}", f"o{i}", f"f{k}()") for k in range(60)]        # exactly 60 code nodes -> eligible
    nodes += [n(f"s::{k}", "short", f"f{k}()") for k in range(59)]
    setup(sandbox, nodes)
    sandbox("diagnose.py")
    s4 = capsys.readouterr().out.split("4. ORPHAN DEFINITIONS")[1].split("5. LOCAL")[0]
    lines = [l for l in s4.splitlines() if "unreferenced defs" in l]
    assert len(lines) == 12 and "short" not in s4 and "100.0%" in lines[0]


def test_shadowed_requires_ok_status_on_both_sides(sandbox, capsys):
    batch = [{"repo": "dir/a", "status": "ok"}, {"repo": "dir/b", "status": "timeout"}, {"repo": "dir/c", "status": "ok"}]
    clones = [{"repo": "a", "status": "ok", "nodes": 1}, {"repo": "b", "status": "ok", "nodes": 1},
              {"repo": "c", "status": "failed", "nodes": 1}]
    setup(sandbox, [n("x", "a", "f()")], batch=batch, clones=clones)
    sandbox("diagnose.py")
    s1 = capsys.readouterr().out.split("2. DUPLICATED")[0]
    assert "repos with BOTH a local checkout and a gh-clone: 1" in s1
