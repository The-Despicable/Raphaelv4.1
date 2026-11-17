"""src/arena/tests/conftest.py — contamination guard for the nested Arena suite.

Background (historical, preserved)
----------------------------------
`arena.ablation_runner.RESULTS_BASE` is the module-global
``Path("arena/results")`` (``src/arena/ablation_runner.py:202``), resolved
**relative to the current working directory**. Run IDs are deterministic by
design — the same ``(config, template, seed, split)`` always yields the same
``run_id`` — so any test that constructs an ``AblationRunner`` without an
explicit ``output_dir`` overwrites the corresponding historical run directory.

That is not hypothetical. `tests/conftest.py:4-9` records that on 2026-10-04
fourteen ``arena/results/raw/abl_*_dev`` directories were rewritten by a test
run; see `evidence/arena_contamination_20261004/README.md`. The top-level suite
was fixed with an autouse fixture. **This nested suite was not**, which is why it
must not be run in the primary worktree until this file exists.

Two independent layers
----------------------
1. **Prevention** — an autouse fixture redirects ``RESULTS_BASE`` to a per-test
   temporary directory, exactly mirroring ``tests/conftest.py``. The writers
   (``AblationRunner.save()``/``ensure_run_dir()``, ``EpisodeRecorder``,
   ``EventsRecorder``) inherit it, so production behaviour is unchanged.

2. **Detection** — a session-scoped guard fingerprints the protected historical
   trees before the first nested test and again after the last, and **fails the
   session** if anything changed. Prevention alone is not evidence: a green suite
   does not by itself demonstrate that history was preserved. This layer is what
   turns "the suite passed" into "the suite passed *and* nothing it touched
   moved".

Layer 2 uses ``(size, mtime_ns)`` per file rather than full content hashing: it
is fast enough to run unconditionally over ~58k tracked artifacts, and any write
— including a same-length rewrite — changes ``mtime_ns``.
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest

#: Repository root, derived from this file (src/arena/tests/conftest.py -> ../../..)
REPO_ROOT = Path(__file__).resolve().parents[3]

#: Historical evidence trees the nested suite must never modify. These are the
#: paths that hold tracked evaluation evidence; ``git ls-files`` counts them at
#: roughly 58k files.
PROTECTED_TREES = (
    REPO_ROOT / "arena" / "results",
    REPO_ROOT / "src" / "arena" / "results",
    REPO_ROOT / "src" / "arena" / "arena" / "results",
    REPO_ROOT / "evidence",
)

#: Set by the session guard; surfaced to tests that want to assert isolation.
_PROTECTED_SNAPSHOT: dict = {}


def _fingerprint(root: Path) -> dict:
    """Map of ``relative-path -> (size, mtime_ns)`` for every file under *root*.

    A missing tree yields an empty mapping rather than an error: a repository
    that has never produced that tree has nothing to protect.
    """
    snapshot: dict = {}
    if not root.is_dir():
        return snapshot
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        base = Path(dirpath)
        for name in filenames:
            path = base / name
            try:
                stat = path.stat()
            except OSError:
                # Unreadable/vanished mid-walk: record a sentinel so the change
                # is visible as a difference rather than silently dropped.
                snapshot[str(path)] = (-1, -1)
                continue
            snapshot[str(path)] = (stat.st_size, stat.st_mtime_ns)
    return snapshot


def _diff(before: dict, after: dict) -> dict:
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(p for p in (set(before) & set(after)) if before[p] != after[p])
    return {"added": added, "removed": removed, "changed": changed}


@pytest.fixture(autouse=True)
def _isolate_arena_results_base(tmp_path, monkeypatch):
    """Layer 1 — point ``arena.ablation_runner.RESULTS_BASE`` at a temp dir."""
    try:
        monkeypatch.setattr(
            "arena.ablation_runner.RESULTS_BASE", tmp_path / "arena-results"
        )
    except (ImportError, AttributeError):
        # The writer module cannot be imported, so the contamination vector does
        # not exist in this session. Not a failure: there is nothing to isolate.
        pass


@pytest.fixture(scope="session", autouse=True)
def _protected_evidence_guard():
    """Layer 2 — fail the session if the nested suite touched historical evidence."""
    before = {root: _fingerprint(root) for root in PROTECTED_TREES}
    _PROTECTED_SNAPSHOT.clear()
    _PROTECTED_SNAPSHOT.update(before)

    yield

    report = {}
    for root in PROTECTED_TREES:
        delta = _diff(before[root], _fingerprint(root))
        if delta["added"] or delta["removed"] or delta["changed"]:
            report[str(root.relative_to(REPO_ROOT))] = delta

    if report:
        detail = "\n".join(
            f"  {tree}: +{len(d['added'])} added, -{len(d['removed'])} removed, "
            f"~{len(d['changed'])} changed"
            for tree, d in report.items()
        )
        pytest.fail(
            "CONTAMINATION GUARD: the nested Arena suite modified protected "
            "historical evidence while running.\n"
            f"{detail}\n"
            "First changed paths (up to 10):\n"
            + "\n".join(
                f"    {p}"
                for d in report.values()
                for p in (d["added"] + d["removed"] + d["changed"])[:10]
            )
            + "\nHistorical evaluation evidence must never be rewritten by a test "
            "run. See evidence/arena_contamination_20261004/README.md.",
            pytrace=False,
        )


def protected_snapshot() -> dict:
    """Pre-run fingerprint of the protected trees, for tests to assert against."""
    return dict(_PROTECTED_SNAPSHOT)
