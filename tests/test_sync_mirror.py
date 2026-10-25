"""tools/sync_mirror.sh behaviour, run on a copy whose mirror path M points
into a temp dir (the only change made to the script under test)."""
import subprocess

import pytest

from conftest import TOOLS, git

REAL_M = "M=/Users/Shared/lit_review"


@pytest.fixture
def mirror(sandbox):
    root, home, env = sandbox
    # sources the script copies from (under the fake HOME)
    mp = home / "market-pipeline" / "research"
    (mp / "literature_runs").mkdir(parents=True)
    (mp / "LITERATURE_REGISTER.md").write_text("# register\n")
    (mp / "BACKTEST_QUEUE.md").write_text("# queue\n")
    (mp / "literature_runs" / "2026-10-25.md").write_text("run log\n")
    md = home / "masaladeutsch-archive" / "docs"
    md.mkdir(parents=True)
    for n in ("SOURCE_REGISTER.md", "COMMISSION_QUEUE.md", "LITERATURE_SURVEY.md"):
        (md / n).write_text(f"# {n}\n")
    task = home / ".claude" / "scheduled-tasks" / "literature-review-daily"
    task.mkdir(parents=True)
    (task / "SKILL.md").write_text("spec\n")
    # bare remote + mirror clone
    remote = root / "remote.git"
    git(env, "init", "-q", "--bare", str(remote))
    m = root / "mirror"
    git(env, "clone", "-q", str(remote), str(m))
    (m / "README.md").write_text("mirror\n")
    git(env, "add", "-A", cwd=m)
    git(env, "commit", "-q", "-m", "init", cwd=m)
    git(env, "push", "-q", "-u", "origin", "main", cwd=m)
    script = root / "sync_mirror.sh"
    src = (TOOLS / "sync_mirror.sh").read_text()
    assert REAL_M in src
    script.write_text(src.replace(REAL_M, f"M={m}"))
    return {"root": root, "home": home, "env": env, "m": m, "remote": remote, "script": script,
            "mp": mp}


def run(mx, *args):
    r = subprocess.run(["bash", str(mx["script"]), *args], env=mx["env"], capture_output=True,
                       text=True, timeout=60)
    assert r.returncode == 0, r.stderr     # the script never fails the scheduled task
    return r.stdout.strip()


def remote_log(mx):
    return git(mx["env"], "--git-dir", str(mx["remote"]), "log", "--format=%s", "main").splitlines()


def test_first_sync_copies_commits_and_pushes(mirror):
    out = run(mirror, "Sync day 1")
    assert out.startswith("SYNC: pushed ")
    assert remote_log(mirror)[0] == "Sync day 1"
    m = mirror["m"]
    assert (m / "market-pipeline" / "literature_runs" / "2026-10-25.md").read_text() == "run log\n"
    assert (m / "task" / "literature-review-daily.SKILL.md").exists()
    assert (m / "masaladeutsch" / "SOURCE_REGISTER.md").exists()


def test_second_sync_without_changes_commits_nothing(mirror):
    run(mirror, "Sync day 1")
    assert run(mirror, "Sync day 2") == "SYNC: no changes, nothing committed"
    assert len(remote_log(mirror)) == 2


def test_missing_source_reports_failure_and_exits_zero(mirror):
    (mirror["mp"] / "BACKTEST_QUEUE.md").unlink()
    assert run(mirror) == "SYNC FAILED: copy market-pipeline registers"
    assert len(remote_log(mirror)) == 1


def test_secret_like_line_stops_and_unstages(mirror):
    (mirror["mp"] / "literature_runs" / "2026-10-25.md").write_text("run log\napi_key = abc123\n")
    out = run(mirror, "Sync")
    assert out.startswith("SYNC STOPPED: 1 secret-scan hit(s)")
    assert "api_key = abc123" in out
    assert git(mirror["env"], "diff", "--cached", "--name-only", cwd=mirror["m"]) == ""
    assert len(remote_log(mirror)) == 1
    # after a human confirms it is prose
    assert run(mirror, "--prose-ok", "Sync").startswith("SYNC: pushed ")
    assert remote_log(mirror)[0] == "Sync"


def test_task_folder_is_excluded_from_secret_scan(mirror):
    task = mirror["home"] / ".claude" / "scheduled-tasks" / "literature-review-daily" / "SKILL.md"
    task.write_text("pattern: api[_-]?key|secret|token\n")
    assert run(mirror, "Sync").startswith("SYNC: pushed ")


def test_added_line_starting_with_plus_plus_is_still_scanned(mirror):
    """The scan drops diff header lines with grep -v '^+++'. An ADDED line whose
    content itself starts with '++' also renders as '+++...' and was dropped,
    so a token on such a line slipped through."""
    (mirror["mp"] / "literature_runs" / "2026-10-25.md").write_text(
        "run log\n++ token: ghp_" + "a" * 30 + "\n")
    out = run(mirror, "Sync")
    assert out.startswith("SYNC STOPPED"), out
    assert len(remote_log(mirror)) == 1


def test_rebases_once_when_remote_moved_ahead(mirror):
    run(mirror, "Sync day 1")
    other = mirror["root"] / "other"
    env = mirror["env"]
    git(env, "clone", "-q", str(mirror["remote"]), str(other))
    (other / "portfolio.md").write_text("track D\n")
    git(env, "add", "-A", cwd=other)
    git(env, "commit", "-q", "-m", "track D", cwd=other)
    git(env, "push", "-q", cwd=other)
    (mirror["mp"] / "BACKTEST_QUEUE.md").write_text("# queue v2\n")
    out = run(mirror, "Sync day 2")
    assert "after rebasing onto newer remote commits" in out
    assert remote_log(mirror)[:2] == ["Sync day 2", "track D"]


def test_conflicting_remote_leaves_local_commit_and_clean_state(mirror):
    run(mirror, "Sync day 1")
    other = mirror["root"] / "other"
    env = mirror["env"]
    git(env, "clone", "-q", str(mirror["remote"]), str(other))
    (other / "market-pipeline" / "BACKTEST_QUEUE.md").write_text("their edit\n")
    git(env, "commit", "-qam", "theirs", cwd=other)
    git(env, "push", "-q", cwd=other)
    (mirror["mp"] / "BACKTEST_QUEUE.md").write_text("our edit\n")
    out = run(mirror, "Sync day 2").splitlines()[-1]   # git's CONFLICT lines precede it
    assert out.startswith("SYNC FAILED: committed ") and "needs a human" in out
    st = subprocess.run(["git", "status"], cwd=mirror["m"], env=env, capture_output=True, text=True).stdout
    assert "rebase in progress" not in st
