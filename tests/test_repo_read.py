"""tools/repo_read.sh argument guards and local-root confinement, with a fake
HOME and a fake `gh` on PATH (no network). The script is run unmodified."""
import os
import subprocess

import pytest

from conftest import TOOLS

SCRIPT = TOOLS / "repo_read.sh"


@pytest.fixture
def rr(sandbox):
    root, home, env = sandbox
    (home / "market-pipeline" / "research").mkdir(parents=True)
    (home / "market-pipeline" / "research" / "notes.md").write_text("alpha NEEDLE\n")
    (home / "secret.txt").write_text("NEEDLE outside the roots\n")
    (home / ".config").mkdir()
    (home / ".config" / "creds.env").write_text("KEY=NEEDLE\n")
    fakebin = root / "bin"
    fakebin.mkdir()
    gh = fakebin / "gh"
    gh.write_text("#!/bin/bash\necho \"GH $*\"\n")
    gh.chmod(0o755)
    env = dict(env, PATH=f"{fakebin}:{env['PATH']}")

    def run(*args):
        return subprocess.run(["bash", str(SCRIPT), *args], env=env, capture_output=True,
                              text=True, timeout=30, stdin=subprocess.DEVNULL)
    run.home = home
    return run


def test_usage_errors(rr):
    assert rr("tree").returncode == 2
    assert rr("localgrep", "x").returncode == 2


@pytest.mark.parametrize("repo", ["../etc", "a;rm", "a b", "x/y"])
def test_bad_repo_names_rejected(rr, repo):
    r = rr("tree", repo)
    assert r.returncode == 2 and "bad repo name" in r.stderr


@pytest.mark.parametrize("repo", ["personal-profile", "working-files"])
def test_personal_repos_off_limits(rr, repo):
    r = rr("file", repo, "README.md")
    assert r.returncode == 2 and "off-limits" in r.stderr


@pytest.mark.parametrize("path", ["../secret", "a/../../b", "a b", "x;y"])
def test_bad_file_paths_rejected(rr, path):
    r = rr("file", "karz", path)
    assert r.returncode == 2 and "bad path" in r.stderr


def test_file_and_tree_call_only_gh_get(rr):
    r = rr("file", "karz", "docs/README.md")
    assert r.stdout.strip() == ("GH api -H Accept: application/vnd.github.raw "
                                "repos/herrrickshaw/karz/contents/docs/README.md")
    assert rr("tree", "karz").stdout.startswith("GH api repos/herrrickshaw/karz/git/trees/HEAD?recursive=1")


def test_localgrep_inside_roots(rr):
    r = rr("localgrep", "NEEDLE", str(rr.home / "market-pipeline"))
    assert r.returncode == 0 and "notes.md" in r.stdout and "secret" not in r.stdout


def test_localgrep_and_ls_outside_roots_denied(rr):
    for args in (("localgrep", "NEEDLE", str(rr.home)), ("ls", str(rr.home / ".config")),
                 ("localgrep", "NEEDLE", str(rr.home / "market-pipeline" / ".." / ".config"))):
        r = rr(*args)
        assert r.returncode == 2 and "outside the allowed folders" in r.stderr, args


@pytest.mark.parametrize("suffix", ["..", "research/../.."])
def test_trailing_dotdot_cannot_escape_roots(rr, suffix):
    """inroots() resolves only the dirname and re-appends the basename, so a
    path ENDING in '..' (e.g. ~/market-pipeline/..) still matched the
    '~/market-pipeline/*' pattern while actually naming $HOME."""
    target = str(rr.home / "market-pipeline") + "/" + suffix
    for args in (("localgrep", "NEEDLE", target), ("ls", target)):
        r = rr(*args)
        assert r.returncode == 2, (args, r.stdout[:300])
        assert "creds.env" not in r.stdout and "secret.txt" not in r.stdout


def test_symlinked_dir_inside_root_cannot_escape(rr):
    link = rr.home / "market-pipeline" / "escape"
    os.symlink(rr.home / ".config", link)
    for args in (("ls", str(link) + "/"), ("localgrep", "NEEDLE", str(link) + "/")):
        r = rr(*args)
        assert "creds.env" not in r.stdout and "KEY=NEEDLE" not in r.stdout, args
