"""Run the tools/*.py programs against a sandbox HOME.

All three scripts execute at import time and read/write under `~` (and, for build_lit_graph,
a hard-coded /Users/Shared/lit_review). We point HOME at tmp_path, substitute the one
absolute path in the source text before compiling, and compile under the real filename so
coverage is attributed to the repo files.
"""
import json
import os
import pathlib

import pytest

REPO = pathlib.Path(__file__).resolve().parents[1]


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    home = tmp_path / "home"
    lit = tmp_path / "lit_review"
    (home / ".graphify").mkdir(parents=True)
    (home / ".ruflo/logs").mkdir(parents=True)
    lit.mkdir()
    monkeypatch.setenv("HOME", str(home))

    def run(name, **replacements):
        real = REPO / "tools" / name
        src = real.read_text(encoding="utf-8")
        src = src.replace('"/Users/Shared/lit_review"', repr(str(lit)))
        ns = {"__name__": f"tools_{real.stem}", "__file__": str(real)}
        exec(compile(src, str(real), "exec"), ns)
        return ns

    run.home, run.lit = home, lit
    run.write_json = lambda p, obj: (pathlib.Path(p).parent.mkdir(parents=True, exist_ok=True),
                                      pathlib.Path(p).write_text(json.dumps(obj)))
    return run
