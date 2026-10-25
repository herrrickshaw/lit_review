"""Shared harness: run the repo's bash tools against a throwaway HOME and,
for sync_mirror.sh, a throwaway mirror + bare remote. The real
/Users/Shared/lit_review and ~/ are never read or written."""
import os
import subprocess
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parent.parent / "tools"


@pytest.fixture
def sandbox(tmp_path):
    root = tmp_path.resolve()
    home = root / "home"
    home.mkdir()
    gitcfg = root / "gitconfig"
    gitcfg.write_text("[user]\n\tname = Test\n\temail = t@example.invalid\n"
                      "[init]\n\tdefaultBranch = main\n[pull]\n\trebase = false\n")
    env = {"PATH": os.environ["PATH"], "HOME": str(home), "GIT_CONFIG_GLOBAL": str(gitcfg),
           "GIT_CONFIG_NOSYSTEM": "1", "LANG": "C", "LC_ALL": "C"}
    return root, home, env


def git(env, *args, cwd=None):
    r = subprocess.run(["git", *args], cwd=cwd, env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()
