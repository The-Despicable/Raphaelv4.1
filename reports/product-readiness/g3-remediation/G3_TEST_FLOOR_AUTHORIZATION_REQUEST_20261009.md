# RAPHAEL — G3 Test-Floor Authorization Request and Execution Preflight

**NON-AUTHORITATIVE PREPARATION DOCUMENT.** Nothing here has been executed. No test was run
during this task. This document asks the operator for authorization; it does not grant it.

**G3 remains NOT ACCEPTED. P4 and P10 remain NOT AUTHORIZED.**

---

## 1. Verified repository baseline

Read-only verification performed at the start of this task. **No divergence from the expected
baseline.**

| Field | Expected | Verified | Match |
|---|---|---|---|
| Repository root | `/home/yaser/external-audits/raphael-2` | same | ✅ |
| Branch | `governance/rsi-1-provenance-correction` | same | ✅ |
| HEAD | `fc3e2c132591eab7edaa12e97e13fe2d01619411` | same | ✅ |
| Tree | `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061` | same | ✅ |
| Commits on HEAD | — | 188 | — |
| Staged changes | 0 | **0** | ✅ |
| `requires-python` | `>=3.11,<3.13` | `>=3.11,<3.13` (`pyproject.toml:10`) | ✅ |

Nothing was reset, cleaned, switched, stashed, committed, or pushed. No other revision was
substituted.

### 1.1 Linked worktrees

| Path | HEAD | Branch | Note |
|---|---|---|---|
| `/home/yaser/external-audits/raphael-2` | `fc3e2c132` | `governance/rsi-1-provenance-correction` | primary |
| `/home/yaser/audit-rsi1/ratification-wt` | `fc3e2c132` | `governance/rsi-1-operator-ratification-draft` | pre-existing, not touched |
| `/tmp/rbase-b6ef24` | `b6ef24bdb` | detached | **pre-existing stale/prunable — deliberately NOT pruned** |

### 1.2 Current local changes

**Modified tracked files — 3 (matches expectation):**
`README.md`, `evidence/DEFECT_REGISTER.md`, `evidence/phases/P3_0_reinventory/WELD_SET.md`
(aggregate +193 / −23).

**Untracked — one counting difference to record explicitly:**

> The prior report states "ten newly created files or directories". Verified actual:
> **10 untracked *status entries*, expanding to 26 individual files.**
> The difference is counting granularity (git collapses directories into one entry), **not new
> drift**. `git status --porcelain --untracked-files=all` returns 26 `??` files.

| Untracked file | Origin |
|---|---|
| `RAPHAEL_RSI1_INDEPENDENT_AUDIT_FC3E2C132.md` | pre-existing, not ours |
| `docs/adr/ADR-013-am4-r3-status-and-precedence-conflict.md` | G3 remediation task |
| `evidence/GOVERNANCE_DECISIONS_20261009.jsonl` | G3 remediation task |
| `evidence/frozen_instrument_drift/UNVERIFIABLE_DRIFT_20261009.json` | G3 remediation task |
| `evidence/frozen_instrument_drift/UNVERIFIABLE_DRIFT_20261009.md` | G3 remediation task |
| `evidence/governance/P4_RSI_FREEZE_NOTICE_20261009.md` | G3 remediation task |
| `reports/product-readiness/RAPHAEL_PRODUCT_READINESS_2026-10-09.json` | readiness audit |
| `reports/product-readiness/RAPHAEL_PRODUCT_READINESS_2026-10-09.md` | readiness audit |
| `reports/product-readiness/g3-remediation/G3_BLOCKER_RESOLUTION_PACKET_20261009.json` | blocker packet |
| `reports/product-readiness/g3-remediation/G3_BLOCKER_RESOLUTION_PACKET_20261009.md` | blocker packet |
| `reports/product-readiness/g3-remediation/G3_REMEDIATION_REPORT_20261009.md` | G3 remediation task |
| `reports/product-readiness/g3-remediation/G3_REMEDIATION_SUMMARY_20261009.json` | G3 remediation task |
| `reports/product-readiness/g3-remediation/hashes/` — 9 files (8 manifests + README) | G3 remediation task |
| `scripts/gen_governance_decision_seeds.py` | G3 remediation task |
| `src/arena/tests/conftest.py` | G3 remediation task |
| `src/orchestrator/rsi/governance_registry.py` | G3 remediation task |
| `tests/test_rsi1_governance_registry.py` | G3 remediation task |
| `tests/test_rsi1_governance_registry_adversarial.py` | G3 remediation task |

*(After this task's two deliverables are written the count becomes 28 files / 12 entries.)*

### 1.3 Governance state confirmed

| Artifact | State | Label |
|---|---|---|
| `evidence/governance/P4_RSI_FREEZE_NOTICE_20261009.md` | **ACTIVE** | `IMPLEMENTED` |
| `evidence/GOVERNANCE_DECISIONS_20261009.jsonl` | 6 records, **all `PROPOSED`**, all `authority_principal: ""`, all `decided_at: ""` | `PROVEN` |
| G3 acceptance artifact | none exists | `PROVEN` (absence) |

### 1.4 Pytest configuration (defines default inclusion)

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]              # ← already excludes src/arena/tests
pythonpath = ["src"]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
```
`testpaths = ["tests"]` means a bare `pytest` invocation **excludes** `src/arena/tests`.
The protocol must make that exclusion an explicit, recorded decision rather than an accident.

---

## 2. The seven historical figures and their limitations

| # | Figure | Source:line | Revision | Distance to HEAD | Interpreter | Transcript | Limitation |
|---|---|---|---|---|---|---|---|
| 1 | **357** | `RAPHAEL_STATE.md:10` | none claimed | — | none recorded | **No** | `REPORTED` — unverifiable; no revision, no interpreter, no transcript |
| 2 | **369** | `evidence/g3_remediation/STATUS.md:23` | `07fad8c1` | 39 commits | 3.14.4 | Yes — `369 passed, 32 warnings in 21.09s` | Out of declared range; 39 commits stale |
| 3 | **385** | `evidence/p311_mvp/P311_EVIDENCE.md:88` | `fc83a6179` | 37 commits | 3.14.4 | Yes — `385 passed, 33 warnings in 11.99s` + clean-checkout `14.03s` | Out of range; 37 commits stale |
| 4 | **552** | `evidence/g3_remediation/F2_PERIMETER_RECORD.md:31` | 001R6 era | ~35 | none recorded | **No** | `REPORTED` — prose assertion only |
| 5 | **621** | `REVIEWER_GUIDE.md:28` | none | — | 3.14.4 | **No** | `REPORTED`; the file itself states the frozen pin "is NOT satisfiable" |
| 6 | **1218** | `reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md:22,110,122,374` | `c1eab3dd2` era | — | 3.12.15 | **No** | In range, but no transcript |
| 7 | **1318** | `evidence/phase3_readiness/REMEDIATION_MANIFEST.json:13` | `1fd7cda76`, tree `49237b06` **`git rev-parse` verified** | 8 commits | 3.12.15, pytest 9.1.1 | Yes — `1318 passed, 44 warnings in 103.38s` | **Best-evidenced, but 8 commits stale and transcript carries a CUDA driver-mismatch warning** |

**Cross-cutting limitations:**

- **No figure describes HEAD `fc3e2c132`.** `[PROVEN]`
- Three of four transcript-backed runs used **Python 3.14.4, outside `>=3.11,<3.13`**. `[PROVEN]`
- **Hardware has changed since the 1318 run.** That transcript records
  *"NVIDIA driver … too old (found version 12080)"*; the current host reports driver
  **573.71** (GeForce MX130). 1318 is therefore **not reproducible on this machine as
  currently configured**. The version-number mapping is `INFERRED`; the two recorded values
  are `PROVEN`.
- A prior task collected **1509** tests — that is a **collection** count, not a pass count,
  and it included 57 tests from then-untracked files. Not comparable to any figure above.
  `[REPORTED]`, **not reproduced in this task** (no tests run).

**Conclusion: zero of seven figures satisfy the eight authoritative-floor criteria. A run is
required before any floor can be designated.**

---

## 3. Decision A — Which repository state should the floor describe?

### Option A — Committed baseline (disposable detached worktree)

Create `git worktree add --detach <path> fc3e2c132…`; run there.

- **Advantages.** Unambiguous revision identity — commit *and* tree SHA both resolvable;
  clean checkout reproduces exactly what a reviewer cloning the commit gets; the 26 untracked
  remediation files are structurally excluded, so the count is not polluted; easiest to
  independently re-verify.
- **Consequences.** The floor does **not** validate the governance registry, the 57 new
  governance tests, ADR-013, the freeze notice, or the documentation edits. Those remain
  unmeasured until a separate candidate run.
- **Committed suite size:** `tests/` = **75** `.py` files (77 on disk − 2 untracked).
  Nested suite = 6 committed `.py` files. `[PROVEN]`

### Option B — Remediation candidate

- **Advantages.** Measures the candidate that includes the latest governance work.
- **Blocker that must be stated plainly:** an uncommitted candidate **has no git tree SHA.**
  A tree identity exists only for committed content. Therefore Option B requires *either*
  (a) operator authorization to commit the candidate (changing the very thing being
  measured), or (b) a **manifest-defined identity** — a `sha256` manifest of the candidate
  file set plus an explicit inclusion policy, with no VCS revision to fall back on.
- **Consequences.** Without (a) or (b), a candidate floor is not independently reproducible:
  a reviewer cannot reconstruct "the candidate" from any revision. Comparison against
  historical counts additionally requires an explicit scope-difference statement.

### Recommendation

**Adopt Option A for the authoritative floor; treat Option B as a separate validation target.
Do not combine their counts.**

Rationale: the purpose is reproducible evidence for AM-8 and the G3 package. An unambiguous
tree SHA is worth more than coverage of uncommitted work, and combining a 75-file count with a
77-file count would produce a number that describes neither. Candidate validation is a
follow-on authorization, and it should be preceded by an explicit decision on whether the
candidate gets committed.

**No commit or stash is proposed or performed.** Option A requires none.

---

## 4. Decision B — Which suites are included?

| Suite | Inclusion in the authoritative root-suite floor | Rationale |
|---|---|---|
| **1. Configured root suite — `tests/`** | **INCLUDED** | This is the AM-8 object. `testpaths=["tests"]` already scopes it. 75 committed files. |
| **2. Guardrail suites — `tests/test_p2_guardrail_*.py`** (10 files) | **RECOMMEND SEPARATE, REPORTED SEPARATELY** | They are a strict subset of `tests/` and are already counted in the root figure. Running them again yields a second number that must not be added to the first. Report as a corroborating sub-result with its own exit code. |
| **3. Nested Arena suite — `src/arena/tests`** (6 committed files) | **EXCLUDED — and must not run in the primary worktree** | Separate authorization required. Contamination risk documented in `evidence/arena_contamination_20261004/README.md` (14 directories rewritten 2026-10-04). Four legacy failures are `REPORTED`, not fixed. |

### Collection vs execution — never conflate

Four distinct phases, four distinct numbers:

| Phase | Command class | Yields | Is it a floor? |
|---|---|---|---|
| Collection | `--collect-only -q` | collected count + collection errors | **No** |
| Execution | `-q` | passed / failed / skipped / **errored** / warnings / duration | **Yes** |
| Guardrail (optional) | targeted paths | its own five counts + exit code | No — corroborating only |
| Nested (excluded) | — | — | Not in this run |

A collection count is **never** a floor. A run that collects 1,400 and reports 0 executed has
established nothing about pass state.

### The 57 untracked governance tests

They live in `tests/test_rsi1_governance_registry.py` and
`tests/test_rsi1_governance_registry_adversarial.py`, both **untracked**. Under Option A they
are structurally absent from the worktree — **not merely deselected**. They must not be assumed
present, and they must not be counted. `[PROVEN]` that both are untracked.

---

## 5. Integrity safeguards — assessment and required protocol

### 5.1 Current in-suite guard (`src/arena/tests/conftest.py`)

```python
PROTECTED_TREES = (arena/results, src/arena/results,
                   src/arena/arena/results, evidence)
fingerprint: dict[str, (size, mtime_ns)]   # os.walk, skips __pycache__
```
Session-scoped; fails the session on any added/removed/changed entry. **Not modified in this
task.**

**Verdict: tripwire, not integrity proof.** Defects the protocol must compensate for:

| Defect | Consequence for the floor |
|---|---|
| `(size, mtime_ns)` is not content | A write restoring `mtime_ns` (`os.utime`, `copy2`, `rsync -t`, `cp -p`, a VCS checkout) is invisible |
| Only 4 trees guarded | `evaluations/`, `failures/`, `baseline/`, `Report_Raphael/`, `policies/`, `configs/` unprotected |
| Within-session comparison only | Pre-session modifications undetected |
| Missing tree → empty mapping, no error | A vanished tree reads as "clean" |
| mtime touch with identical content | False positive |

### 5.2 Required content-level protocol

SHA-256 manifests before and after, covering the four named trees **and the whole tracked
tree**. The prior task demonstrated this works: `BEFORE_protected.sha256` and
`AFTER_all_tracked.sha256` each hold **67,641** entries.

**Prior manifests re-verified during this task** (read-only):

| Manifest | Lines | Manifest SHA-256 |
|---|---|---|
| `BEFORE_protected.sha256` | 67,641 | `5a672359b52c0a005ca9a63fef8311e989f786e079b1dbf8b8db02f63bc0f384` |
| `AFTER_all_tracked.sha256` | 67,641 | `2c11be6a6d69c44028016becba576286cb84bb69e7029393c2bb8880f1778da9` |
| `AFTER_final.sha256` | 67,641 | `2c11be6a6d69c44028016becba576286cb84bb69e7029393c2bb8880f1778da9` |
| `C2_BEFORE_wt.sha256` | 58,929 | `aea6970c2dcde9ca07b53d95ea7078dfceb92bc9a6bb4363d7a7b119cde725a6` |
| `C2_AFTER_wt.sha256` | 58,929 | `aea6970c2dcde9ca07b53d95ea7078dfceb92bc9a6bb4363d7a7b119cde725a6` |
| `C2_DIFF.txt` | 0 bytes | — |

`AFTER_all_tracked` and `AFTER_final` hash **identically**, and the two C2 manifests hash
**identically** — the prior run's determinism and isolation claims are reproducible.

### 5.3 Manifest anomalies — required reporting rules

| Condition | Required handling |
|---|---|
| **Missing file** (in BEFORE, absent in AFTER) | Report explicitly as `REMOVED`. Never silently drop from the diff. |
| **Added file** | Report as `ADDED`. |
| **Changed digest** | Report as `CHANGED` with both digests. |
| **Broken symlink** | 4 tracked symlinks (`cai_service`, `cloak_service`, `mcp_hub`, `mhddos_service` → `/home/yaser/raphael-2.0/…`, which does not exist) are **unreadable by `sha256sum`**. Enumerate them in a **separate symlink list** and exclude identically from both manifests. `[PROVEN]` they are broken. |
| **Unreadable file** | Record path + errno. Do not substitute a partial hash. |
| **Scope mismatch** | **Never compare manifests built from different file sets.** Before diffing, assert `wc -l` equality and that both were built from the same `git ls-files` output (record that list's digest). A prior task made exactly this mistake and had to regenerate — the check prevents recurrence. |
| **Manifest's own digest** | Record `sha256sum BEFORE.sha256` and `sha256sum AFTER.sha256`. An "unchanged" verdict is only meaningful alongside the scope and the manifest digest. |

---

## 6. Environment fingerprint — required metadata

Collected read-only **during this task** (pre-flight observation, not a run):

| Item | Value | Label |
|---|---|---|
| In-range interpreter | `Python 3.12.15 (main, Oct 3 2026, 01:03:07) [Clang 22.1.3]` | `PROVEN` |
| Interpreter symlink | `.venv/bin/python` → `/home/yaser/.local/share/uv/python/cpython-3.12-linux-x86_64-gnu/bin/python3.12` | `PROVEN` |
| Interpreter realpath | `/home/yaser/.local/share/uv/python/cpython-3.12.15-linux-x86_64-gnu/bin/python3.12` | `PROVEN` |
| Interpreter executable SHA-256 | `0886fb76ceec8ff568d23079b5da6342bb41675e216e11525d4d6a9e65988d10` | `PROVEN` |
| venv provenance | `uv 0.12.23`; `include-system-site-packages = false`; CPython 3.12 | `PROVEN` |
| Out-of-range interpreter | `Python 3.14.4 (main, Aug 20 2026) [GCC 15.2.0]` | `PROVEN` |
| OS | Ubuntu 26.04 LTS | `PROVEN` |
| Kernel | `6.6.87.2-microsoft-standard-WSL2` x86_64 (WSL2) | `PROVEN` |
| CPU | Intel Core i7-8565U @ 1.80GHz, 8 logical | `PROVEN` |
| RAM | 3,930,336 kB ≈ **3.75 GiB** | `PROVEN` |
| GPU | NVIDIA GeForce MX130, driver **573.71** | `PROVEN` |
| Lockfile | **None** — `poetry.lock`, `uv.lock`, `Pipfile.lock`, `constraints.txt`, `setup.py` all absent | `PROVEN` |
| Installed packages | 117 `*.dist-info` in `.venv/lib/python3.12/site-packages` | `PROVEN` |
| pytest / pytest-asyncio | 9.1.1 / 1.4.0 | `PROVEN` |

### 6.1 ⚠️ `pip` is not installed in the in-range interpreter — the specified fingerprint method is BLOCKED

```console
$ .venv/bin/python -m pip --version
/home/yaser/external-audits/raphael-2/.venv/bin/python: No module named pip
$ python3 -m pip --version
pip 25.1.1 from /usr/lib/python3/dist-packages/pip (python 3.14)
```

The requested `python -m pip freeze` **cannot be produced by the interpreter the run must
use**. The system `pip` belongs to Python 3.14 — out of range — and using it would fingerprint
the wrong interpreter. `[PROVEN]`

**Options for the operator (this is a decision, not a default):**

| Option | Method | Consequence |
|---|---|---|
| **F1 (recommended)** | Read `Name:` and `Version:` from each installed distribution's own `METADATA` file, emit `Name==Version`, record the inventory's own digest | Zero environment change; no install, no network. Validated read-only in this repository: **117 `.dist-info` directories → 117 inventory entries, 0 missing fields.** Uses the distribution's **declared** metadata rather than a filename heuristic. |
| **F2** | Operator authorizes installing `pip` into `.venv` before the run | Full `pip freeze`, but **modifies the environment being measured** — the fingerprint then records a post-installation state, and the change must itself be declared. |
| **F3** | Use the system `pip` with `--python .venv/bin/python` | Fingerprints the wrong interpreter; **not recommended**. |

> **Why F1 does not parse directory names.** An earlier revision of this protocol derived the
> inventory from `.dist-info` directory names with
> `sed -E 's/-py3.*//; s/\.dist-info//'`. That regex only strips a tag that literally begins
> `-py3`. It happens to yield correct `name-version` output **in this particular `uv`-created
> environment**, where all 117 directories are named `name-version.dist-info` — but it is
> **environment-dependent, not robust**. A `pip`-installed wheel produces e.g.
> `torch-2.14.1-cp312-cp312-manylinux_2_28_x86_64.dist-info`, which this regex leaves as
> `torch-2.14.1-cp312-cp312-manylinux_2_28_x86_64`. It therefore does **not** consistently
> capture name and version. F1 was corrected to read `METADATA`.

**Explicit limitations of F1 — these remain true after the correction:**

- A distribution inventory is **not a lockfile**. It does not pin hashes, and it says nothing
  about artifact integrity.
- It is **not a dependency-graph proof**. It records what is *installed*, not what was
  *resolved* from `requirements.txt`, and cannot show whether the installed set satisfies the
  declared requirements.
- It records **installed state only**; it cannot distinguish a direct dependency from a
  transitive one, nor detect an extra package that was never declared.
- `METADATA` yields **canonical** distribution names (`Jinja2`, `PyYAML`); a filename-based
  method yields filesystem-normalized names (`jinja2`, `pyyaml`). Both are valid identifiers,
  but only the former is authoritative — which matters when this inventory is compared with
  `requirements.txt`.
- The repository still has **no lockfile of any kind**. This is a standing reproducibility
  gap; F1 mitigates it for measurement purposes but does not close it.

`pip freeze` output is **not** required to be identical to the manifest digest — it is required
to *exist*. With F1 it exists as a `METADATA`-derived distribution inventory.

### 6.2 Additional fingerprint items to capture at run time

- `git rev-parse HEAD` and `git rev-parse HEAD^{tree}` — captured twice (pre- and post-run)
- `git status --porcelain` — must be empty in a clean worktree
- `git worktree list`
- `date -u +%Y-%m-%dT%H:%M:%SZ` at start and end
- `nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv`
- `/proc/meminfo` `MemAvailable` at start and end
- **Container image digests** — only if a future authorized run explicitly requires containers. Not required for this floor; recorded as `NOT APPLICABLE` for the root suite.
- **Environment variable NAMES only** — e.g. `env | cut -d= -f1 | sort`. **Never values.**

### 6.3 RAM is a live risk

3.75 GiB RAM with `torch` installed and the 1318-test run taking 103 s. `MemAvailable` must be
captured pre/post, and the protocol carries an explicit timeout. An OOM kill is an
**environmental** result, never a test failure. `[PROVEN]` for the RAM figure; `[INFERRED]`
for the OOM risk.

---

## 7. Execution protocol — ten phases

**NOT EXECUTED.** Requires explicit operator authorization (see §11).

Work happens in a disposable worktree so the primary worktree is never the measurement target.
**Every generated artifact is written to an external scratch directory, never into the
repository and never into the worktree.**

### 7.0 Artifact-isolation rule (defect corrected 2026-10-09)

The earlier revision of this protocol `cd`-ed into the worktree and then wrote every `FP_*`
file with a **relative** path. Those files would have landed inside the worktree, making the
Phase-7 `git status --porcelain` non-empty and **triggering this protocol's own stop condition
S13** — the run would have invalidated itself.

Corrected rules, binding on every phase:

1. **All output paths are absolute and rooted at `$ART`.**
2. **No `FP_*` file may ever be created inside `$REPO` or `$WT`.**
3. Where a command must resolve *repository-relative* paths (hashing, `sha256sum -c`, lockfile
   probing, the `test_p2_guardrail_*.py` glob), it runs inside an explicit subshell
   `( cd "$WT" && … )` so the working directory is unambiguous **while stdout/stderr still go
   to `$ART`**.
4. Exit codes are captured into a variable **immediately** after the command, before any other
   command can overwrite `$?`, and written to a dedicated `.exit` file.
5. **S13 is not weakened.** The worktree must be clean at run end. Misplaced output is a
   protocol defect to be fixed, not an expected exception.

### 7.1 Command set

```bash
# ============================================================================
# ILLUSTRATIVE ONLY — DO NOT EXECUTE. Requires authorization (A-1, R-1, R-2).
# ============================================================================

REPO=/home/yaser/external-audits/raphael-2
WT=/home/yaser/audit-rsi1/g3-floor-wt
ART=/home/yaser/audit-rsi1/g3-floor-artifacts          # external scratch, see R-2
PY="$REPO/.venv/bin/python"                            # interpreter lives in $REPO, NOT $WT
EXPECT_HEAD=fc3e2c132591eab7edaa12e97e13fe2d01619411
EXPECT_TREE=e24d42bf7f7655293f3eb3a273c9ce4d94b1e061

# ---- Phase 0: external artifact directory preconditions ----------------------
# (0a) ART must be OUTSIDE both the repository and the worktree.
case "$ART/" in
  "$REPO"/*|"$WT"/*) echo "FATAL: ART is inside the repo or worktree" >&2; exit 1 ;;
esac

# (0b) Refuse to reuse a directory that already holds a previous run's evidence.
if [ -d "$ART" ] && [ -n "$(ls -A "$ART" 2>/dev/null)" ]; then
  echo "FATAL: $ART is not empty — refusing to overwrite previous run evidence" >&2
  exit 1
fi

# (0c) Creating it may touch the user's filesystem -> requires R-2 authorization.
mkdir -p "$ART"
FP="$ART/FP_start.txt"

# ---- Phase 1: baseline and tree verification ---------------------------------
git -C "$REPO" rev-parse --show-toplevel        > "$ART/FP_phase1_toplevel.txt"
git -C "$REPO" worktree list                    > "$ART/FP_worktrees_pre.txt" 2>&1
git -C "$REPO" worktree add --detach "$WT" "$EXPECT_HEAD" 2> "$ART/FP_worktree_add.err"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_worktree_add.exit"
[ "$rc" -eq 0 ] || { echo "STOP: worktree add failed" >&2; exit 1; }

git -C "$WT" rev-parse HEAD       > "$ART/FP_phase1_head.txt"
git -C "$WT" rev-parse HEAD^{tree} > "$ART/FP_phase1_tree.txt"
git -C "$WT" status --porcelain   > "$ART/FP_phase1_status.txt"

test "$(cat "$ART/FP_phase1_head.txt")"  = "$EXPECT_HEAD" || { echo "STOP S1" >&2; exit 1; }
test "$(cat "$ART/FP_phase1_tree.txt")"  = "$EXPECT_TREE" || { echo "STOP S2" >&2; exit 1; }
test ! -s "$ART/FP_phase1_status.txt"                     || { echo "STOP S3" >&2; exit 1; }

# ---- Phase 2: environment fingerprint ----------------------------------------
date -u +%Y-%m-%dT%H:%M:%SZ                      >  "$FP"
"$PY" -VV                                         >> "$FP" 2>&1
readlink -f "$PY"                                 >> "$FP"
sha256sum "$PY"                                   >> "$FP"
cat "$REPO/.venv/pyvenv.cfg"                      >> "$FP"

# dependency inventory (E-1 / F1; pip is absent from the in-range interpreter).
# Read Name/Version from each distribution's own METADATA — NOT from the .dist-info
# directory name, which carries installer-specific ABI/build tags (see 6.1).
: > "$ART/FP_packages_missing.txt"
for d in "$REPO"/.venv/lib/python3.12/site-packages/*.dist-info; do
  if [ ! -f "$d/METADATA" ]; then
    printf 'MISSING_METADATA %s\n' "$(basename "$d")" >> "$ART/FP_packages_missing.txt"
    continue
  fi
  awk '/^Name: /{if(!n){n=substr($0,7)}}
       /^Version: /{if(!v){v=substr($0,10)}}
       END{printf "%s==%s\n", (n?n:"MISSING_NAME"), (v?v:"MISSING_VERSION")}' \
      "$d/METADATA"
done | sort > "$ART/FP_packages.txt"
sha256sum "$ART/FP_packages.txt"                  >> "$FP"
wc -l < "$ART/FP_packages.txt" > "$ART/FP_packages_count.txt"

# lockfile names are repo-relative -> probe from $WT
( cd "$WT" && ls poetry.lock uv.lock Pipfile.lock constraints.txt ) \
    > "$ART/FP_lockfile_state.txt" 2>&1
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_lockfile_state.exit"

uname -a                                          >> "$FP"
head -3 /etc/os-release                           >> "$FP"
grep -m1 'model name' /proc/cpuinfo               >> "$FP"
grep -E 'MemTotal|MemAvailable' /proc/meminfo     >> "$FP"
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv >> "$FP" 2>&1
env | cut -d= -f1 | sort > "$ART/FP_env_names.txt"      # NAMES ONLY — never values

# ---- Phase 3: pre-run content hashes -----------------------------------------
git -C "$WT" ls-files -z > "$ART/FP_tracked.z"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_tracked_lsfiles.exit"
sha256sum "$ART/FP_tracked.z" > "$ART/FP_tracked_list_digest.txt"

# manifest paths are worktree-relative -> hash with cwd=$WT, output to $ART
( cd "$WT" && xargs -0 -a "$ART/FP_tracked.z" sha256sum ) \
    > "$ART/FP_BEFORE.sha256" 2> "$ART/FP_BEFORE_unreadable.txt"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_BEFORE.exit"
# NOTE: a NON-ZERO exit here is EXPECTED — 4 tracked symlinks are broken and
# sha256sum cannot read them. The check is the CONTENT of FP_BEFORE_unreadable.txt
# (must name exactly the 4 known symlinks), not the exit status.

wc -l < "$ART/FP_BEFORE.sha256" > "$ART/FP_BEFORE_count.txt"
sha256sum "$ART/FP_BEFORE.sha256" >> "$FP"
git -C "$WT" ls-files -s | grep 120000 > "$ART/FP_symlinks.txt"

# ---- Phase 4: collection only (NOT the floor) ---------------------------------
( cd "$WT" && PYTHONPATH=src "$PY" -m pytest tests/ --collect-only -q --no-header ) \
    > "$ART/FP_collect.out" 2> "$ART/FP_collect.err"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_collect.exit"

# ---- Phase 5: configured root suite (THE FLOOR) -------------------------------
date -u +%Y-%m-%dT%H:%M:%SZ > "$ART/FP_run_start.txt"
( cd "$WT" && PYTHONPATH=src "$PY" -m pytest tests/ -q --no-header ) \
    > "$ART/FP_suite.out" 2> "$ART/FP_suite.err"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_suite.exit"
date -u +%Y-%m-%dT%H:%M:%SZ > "$ART/FP_run_end.txt"
grep -E 'MemAvailable' /proc/meminfo >> "$ART/FP_run_end.txt"

# ---- Phase 6: guardrails (subset of tests/ — corroborating only, never summed) --
( cd "$WT" && PYTHONPATH=src "$PY" -m pytest tests/test_p2_guardrail_*.py -q --no-header ) \
    > "$ART/FP_guard.out" 2> "$ART/FP_guard.err"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_guard.exit"

# ---- Phase 7: post-run hashes + comparison ------------------------------------
git -C "$WT" rev-parse HEAD HEAD^{tree} > "$ART/FP_post_identity.txt"
git -C "$WT" status --porcelain          > "$ART/FP_post_status.txt"
git -C "$WT" worktree list               > "$ART/FP_worktrees_post.txt" 2>&1

( cd "$WT" && xargs -0 -a "$ART/FP_tracked.z" sha256sum ) \
    > "$ART/FP_AFTER.sha256" 2> "$ART/FP_AFTER_unreadable.txt"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_AFTER.exit"

wc -l < "$ART/FP_AFTER.sha256" > "$ART/FP_AFTER_count.txt"
sha256sum "$ART/FP_AFTER.sha256" > "$ART/FP_AFTER_manifest_digest.txt"

# ASSERT equal scope BEFORE diffing — never diff mismatched file sets
nb=$(cat "$ART/FP_BEFORE_count.txt"); na=$(cat "$ART/FP_AFTER_count.txt")
if [ "$nb" -ne "$na" ]; then
  printf 'SCOPE_MISMATCH before=%s after=%s\n' "$nb" "$na" > "$ART/FP_diff_summary.txt"
  echo "STOP S6: manifest scopes differ; refusing to diff" >&2; exit 1
fi

diff <(sort "$ART/FP_BEFORE.sha256") <(sort "$ART/FP_AFTER.sha256") > "$ART/FP_HASH_DIFF.txt"
diff_rc=$?                                   # captured BEFORE any other command
diff_lines=$(wc -l < "$ART/FP_HASH_DIFF.txt")
{
  printf 'scope_before=%s\n' "$nb"
  printf 'scope_after=%s\n'  "$na"
  printf 'diff_exit=%s\n'    "$diff_rc"
  printf 'diff_lines=%s\n'   "$diff_lines"
} > "$ART/FP_diff_summary.txt"
# diff_exit=0 AND diff_lines=0  =>  protected evidence byte-identical

diff "$ART/FP_BEFORE_unreadable.txt" "$ART/FP_AFTER_unreadable.txt" \
    > "$ART/FP_unreadable_diff.txt" 2>&1
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_unreadable_diff.exit"

# ---- Phase 8: independent verification (second party, NOT the runner) ---------
# manifest paths are worktree-relative -> verify with cwd=$WT
( cd "$WT" && sha256sum -c "$ART/FP_BEFORE.sha256" ) \
    > "$ART/FP_verify_BEFORE.out" 2> "$ART/FP_verify_BEFORE.err"
rc=$?; printf 'exit=%s\n' "$rc" > "$ART/FP_verify_BEFORE.exit"
grep -v ': OK$' "$ART/FP_verify_BEFORE.out" > "$ART/FP_verify_BEFORE_failures.txt"

sha256sum "$ART/FP_BEFORE.sha256"    > "$ART/FP_verify_manifest_digest.txt"
git -C "$WT" rev-parse HEAD^{tree}   > "$ART/FP_verify_tree.txt"
cat "$ART/FP_suite.exit" "$ART/FP_collect.exit" "$ART/FP_guard.exit" \
    > "$ART/FP_all_exit_codes.txt"

# ---- Phase 9: report generation (authored inside $ART) ------------------------
# Records collected / passed / failed / skipped / errors / warnings / duration
# as DISTINCT fields, plus commit SHA, tree SHA, interpreter hash, package-inventory
# digest, BOTH manifest digests, both scope counts and the diff verdict.
```

**Restoration (after the run, regardless of outcome):**

```bash
git -C "$REPO" worktree remove --force "$WT"
git -C "$REPO" worktree list > "$ART/FP_worktrees_post_removal.txt" 2>&1
# MUST match FP_worktrees_pre.txt with only the disposable $WT entry removed
```

The pre-existing stale entry `/tmp/rbase-b6ef24` is **not** pruned — it predates this work.

### 7.2 Commands that may only appear inside `( cd "$WT" && … )`

| Command | Why the working directory matters |
|---|---|
| `xargs -0 -a FP_tracked.z sha256sum` | manifest records **worktree-relative** paths |
| `sha256sum -c FP_BEFORE.sha256` | `-c` resolves each recorded path relative to cwd |
| `ls poetry.lock uv.lock …` | lockfile names are repo-relative |
| `pytest tests/…` and the `test_p2_guardrail_*.py` glob | suite paths and glob are repo-relative |

All other commands use `git -C`, `python -VV`, `/proc`, `/etc`, or absolute paths and do not
depend on the working directory.

---

## 8. Stop conditions and rollback

### Stop immediately and report — do not continue

| # | Condition | Classification |
|---|---|---|
| S1 | `git rev-parse HEAD` ≠ `EXPECT_HEAD` | revision mismatch |
| S2 | `git rev-parse HEAD^{tree}` ≠ `EXPECT_TREE` | revision mismatch |
| S3 | `git status --porcelain` non-empty at run start | dirty worktree |
| S4 | Interpreter outside `>=3.11,<3.13` | environment |
| S5 | Dependency inventory digest differs between fingerprint and expected | environment |
| S6 | `FP_BEFORE.sha256` line count ≠ `FP_AFTER.sha256` line count | **scope mismatch — never diff** |
| S7 | Unreadable-file set changes between before and after | manifest integrity |
| S8 | Any `ADDED`/`REMOVED`/`CHANGED` in `FP_HASH_DIFF.txt` | **protected evidence modified** |
| S9 | Collection phase exits non-zero | collection error, not a test result |
| S10 | Execution exceeds a pre-declared wall-clock budget | environment |
| S11 | OOM kill / process killed by signal | environment, **not** a test failure |
| S12 | Non-zero exit with an import/network/GPU cause | environment, **not** a test failure |
| S13 | `git status --porcelain` non-empty at run end | worktree mutated by the run |
| **S14** | `$ART` is inside `$REPO` or `$WT` | **artifact-isolation violation** |
| **S15** | `$ART` exists and is non-empty | refusing to overwrite previous run evidence |
| **S16** | Any `FP_*` file found inside `$WT` or `$REPO` | **artifact-isolation violation — the run has contaminated its own measurement target** |
| **S17** | `FP_diff_summary.txt` reports `SCOPE_MISMATCH` | manifests built from different file sets |

> **S13 is not weakened.** Because all artifacts now go to `$ART`, a dirty worktree at run end
> can only mean the run genuinely mutated tracked content. That is exactly what S13 exists to
> catch, and the fix is to find the leak — never to permit it.

> **Expected non-zero exits.** `FP_BEFORE.exit` and `FP_AFTER.exit` are **expected** to be
> non-zero, because 4 tracked symlinks (`cai_service`, `cloak_service`, `mcp_hub`,
> `mhddos_service`) are broken and `sha256sum` cannot read them. The correct check is that
> `FP_BEFORE_unreadable.txt` names exactly those 4 and that `FP_unreadable_diff.exit` is 0.
> Treating this exit as a failure would be a false stop; ignoring it entirely would be a false
> pass.

### Prohibitions during the measurement run

- **No test may be edited, skipped, xfailed, weakened, deleted, or added** to alter the result. Under roadmap **AM-6** this is evidence tampering and an automatic gate failure.
- No dependency install/upgrade.
- No `git add`/`commit`/`stash`/`checkout` inside the worktree.
- No performance benchmark.
- No Docker start, external network, or target interaction.

### Rollback

A measurement run mutates nothing tracked, so rollback is limited to: **remove the disposable
worktree and verify `git worktree list` is restored.** Every captured artefact (`FP_*`) is
written under the external scratch directory `$ART` (`/home/yaser/audit-rsi1/g3-floor-artifacts`
as an example), which is outside both the repository and the worktree — **never** into protected
trees, and never into the measurement target.

**Any code repair is a separate, authorized task followed by a NEW validation run against a
newly identified candidate.** Repairs never happen inside a measurement run.

---

## 9. Expected outputs and acceptance criteria

### Artifacts to be produced — all under `$ART`, none inside the repository or worktree

| Group | Files |
|---|---|
| Preconditions | `FP_worktrees_pre.txt`, `FP_worktree_add.{err,exit}` |
| Identity | `FP_phase1_{toplevel,head,tree,status}.txt` |
| Fingerprint | `FP_start.txt`, `FP_packages.txt`, `FP_packages_count.txt`, `FP_packages_missing.txt`, `FP_lockfile_state.{txt,exit}`, `FP_env_names.txt` |
| Pre-run hashing | `FP_tracked.z`, `FP_tracked_lsfiles.exit`, `FP_tracked_list_digest.txt`, `FP_BEFORE.sha256`, `FP_BEFORE_unreadable.txt`, `FP_BEFORE.exit`, `FP_BEFORE_count.txt`, `FP_symlinks.txt` |
| Collection | `FP_collect.{out,err,exit}` |
| Floor | `FP_run_start.txt`, `FP_suite.{out,err,exit}`, `FP_run_end.txt` |
| Guardrails | `FP_guard.{out,err,exit}` |
| Post-run hashing | `FP_post_identity.txt`, `FP_post_status.txt`, `FP_worktrees_post.txt`, `FP_AFTER.sha256`, `FP_AFTER_unreadable.txt`, `FP_AFTER.exit`, `FP_AFTER_count.txt`, `FP_AFTER_manifest_digest.txt` |
| Comparison | `FP_HASH_DIFF.txt`, `FP_diff_summary.txt`, `FP_unreadable_diff.{txt,exit}` |
| Independent verification | `FP_verify_BEFORE.{out,err,exit}`, `FP_verify_BEFORE_failures.txt`, `FP_verify_manifest_digest.txt`, `FP_verify_tree.txt`, `FP_all_exit_codes.txt` |
| Restoration | `FP_worktrees_post_removal.txt` |
| Report | hand-authored floor report in `$ART` |

### Eight criteria — all must hold before a floor may be designated

| # | Criterion |
|---|---|
| C1 | Transcript exists with **exit code** and UTC start/end timestamps |
| C2 | Bound to a specific commit **and** tree SHA, verified with `git rev-parse` |
| C3 | Interpreter satisfies `>=3.11,<3.13` |
| C4 | Full environment fingerprint captured, including a dependency inventory that exists |
| C5 | collected / passed / failed / skipped / **errored** / warnings / duration as **distinct** fields |
| C6 | `FP_BEFORE.sha256` ≡ `FP_AFTER.sha256`, same scope, same manifest digest recorded |
| C7 | Describes the baseline tree under measurement, or names its delta explicitly |
| C8 | Independently re-verified per Phase 8 by a party other than the runner |

**On today's evidence, zero of seven historical figures satisfy C1–C8.**

---

## 10. Gate implications — stated accurately

A successful run of this protocol would:

- ✅ establish reproducible validation evidence for **AM-8** and one criterion of the G3
  evidence package;
- ❌ **not** prove every G3 security criterion;
- ❌ **not** constitute GLM adversarial review (roadmap §14.12 remains outstanding — 13
  automated probes exist but the authority review has not occurred);
- ❌ **not** accept G3;
- ❌ **not** authorize P4 or P10;
- ❌ **not** resolve the **AM-4-R3** provenance question;
- ❌ **not** establish the validity of the historical effect sizes;
- ❌ **not** resolve the substantive status of the 78 `welded` classifications or the
  dead-by-import-failure question — both remain for authority review;
- ❌ **not** lift the P4/RSI freeze notice.

> **Note on the 78-file census.** The prior blocker packet found the apparent 78-file
> discrepancy was a **revision/scope misreading**, not an arithmetic inconsistency
> (`NO_CONFLICT_EXISTS`): F2 record 001R2 describes a 140-file census (68/6/5/61) while 001R6
> and WELD_SET U-3 both describe the 150-file census (78/6/4/62), and `CENSUS.md` empirically
> tallies 78/6/4/62 = 150. **This packet does not reintroduce that as an unresolved
> inconsistency.** The substantive questions — whether `welded` is verified rather than merely
> labelled, and whether "dead by import failure" counts as deleted — remain open and are GLM's
> to rule.

---

## 11. Operator decisions — recorded

**Decisions were received explicitly from the operator and are recorded below exactly as stated.
They were not inferred, and nothing was selected on the operator's behalf.**

**State vocabulary.**

- `RESOLVED` — the operator explicitly decided.
- `RESOLVED_NOT_APPLICABLE` — the decision does not apply under the selected branch.
- `RESOLVED_CONDITIONAL` — the operator authorized it **subject to named preconditions that must
  hold at run time**.
- `PENDING` — **no operator decision received.**

**These decisions do not authorize execution.** The operator stated: *"It must not begin the
test-floor run until I provide a separate explicit execution instruction."* No phase may begin.

| # | Item | State | Operator selection | Blocks |
|---|---|---|---|---|
| **A-1** | Select the baseline | `RESOLVED` | **Option A** — frozen committed baseline, HEAD `fc3e2c132591eab7edaa12e97e13fe2d01619411`, tree `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061` | Phase 1 |
| **A-2** | If Option B: candidate identity | `RESOLVED_NOT_APPLICABLE` | **Not applicable** — Option A selected | any candidate run |
| **B-1** | Include root `tests/` suite | `RESOLVED` | **Include** | Phases 4–5 |
| **B-2** | Guardrails separately | `RESOLVED` | **Yes** — run separately and report **without adding to the root-suite total** | Phase 6 |
| **B-3** | Exclude `src/arena/tests` | `RESOLVED` | **Exclude** — any future run requires separate authorization | Phases 4–5 |
| **E-1** | Dependency-inventory method | `RESOLVED` | **F1** — read `Name`/`Version` from `.dist-info/METADATA` without modifying the environment. Operator **acknowledged** this is not a lockfile or complete dependency-graph proof | Phase 2 |
| **E-2** | Wall-clock budget | `RESOLVED` | **Minimum 20 minutes** | Phase 5 |
| **R-1** | Create `/home/yaser/audit-rsi1/g3-floor-wt` | `RESOLVED_CONDITIONAL` | **Authorized**, subject to all baseline and protocol preconditions. Worktree **not yet created** | worktree creation + all subsequent phases |
| **R-2** | Approve `/home/yaser/audit-rsi1/g3-floor-artifacts` | `RESOLVED_CONDITIONAL` | **Approved**, subject to verification it is external to repo and worktree and empty before use. No unrelated files may be modified or cleaned up. Directory **not yet created** | Phase 0 |
| **R-3** | Independent reviewer identity | `RESOLVED_CONDITIONAL` | **ChatGPT** — appointed **Independent Technical Evidence Reviewer** by explicit operator authorization in the current conversation. Reviewer is an **AI system** and is **not the OpenCode test runner**. Subject to the governing process permitting AI review — see **§11.3** | Phase 8 |

**10 of 10 addressed — 9 `RESOLVED`, 1 `RESOLVED_NOT_APPLICABLE`, 0 `PENDING`.**

**Recording integrity.** The **operator's own** identity (name, role, principal) was **not
supplied**, and none was manufactured; it remains recorded as `NOT SUPPLIED`. For R-3 the
operator supplied a **reviewer** identity, not their own. **No signature, attestation, or
timestamp was supplied for either, and none was manufactured.** The reviewer's organizational
affiliation was not supplied and none was invented. The original engineering recommendations
are preserved unaltered in the JSON block
`recommendations_preserved_not_converted_to_approvals` for audit trail; they were **not**
converted by engineering — the operator granted them explicitly.

### 11.1 R-2 — external scratch location and existing files

The parent directory `/home/yaser/audit-rsi1/` is **already in use**: it contains a live linked
git worktree (`ratification-wt`, at the same HEAD), a separate clone (`target/`), and scratch
files from unrelated sessions. **Neither this correction nor the operator's approval authorized
inspecting, moving, deleting, renaming, or cleaning any of them**, and no such action was taken.

The operator **approved the specific location**, subject to conditions that are **not yet
satisfied**:

| Condition | Status | Satisfied at run time by |
|---|---|---|
| Explicit operator approval of the location | ✅ **satisfied** | — |
| Location is external to `$REPO` and the disposable worktree | ⬜ outstanding | protocol Phase 0 precondition `0a` |
| Location contains no prior run evidence; refuse to overwrite | ⬜ outstanding | protocol Phase 0 precondition `0b` |

- **The directory must not be created** until the separate execution instruction is given.
- **Any future cleanup is restricted to artefacts known to belong to the authorized run.**
  Broad cleanup or removal of unrelated content in `/home/yaser/audit-rsi1/` is **not permitted**.
- **The absence of the proposed directory does not constitute authorization to create it.**

### 11.2 Blocking dependencies — status after the recorded decisions

| Decision | Blocks | Status now |
|---|---|---|
| **R-2** | Phase 0 — artifact-directory preconditions | 🔶 approved, conditions outstanding |
| **R-1** | Worktree creation, **and every subsequent execution phase** | 🔶 authorized, preconditions outstanding |
| **A-1** | Baseline preparation and Phase 1 | ✅ resolved |
| **E-1** | Phase 2 — dependency inventory | ✅ resolved |
| **B-1**, **B-3** | Phases 4–5 — suite selection | ✅ resolved |
| **E-2** | Phase 5 — execution time budget | ✅ resolved |
| **B-2** | Phase 6 — guardrail sub-run | ✅ resolved |
| **R-3** | Phase 8 — independent verification | 🔶 **appointed subject to governance** — ChatGPT, AI system; see §11.3 |

**R-3 consequence, revised.** A reviewer is now appointed, so Phase 8 can be performed once
execution is authorized — **subject to the governance condition in §11.3**. If that condition
is not met, **Phase 8 cannot be performed, acceptance criterion C8 cannot be satisfied, and no
floor produced by a run could be designated `AUTHORITATIVE`.**

**Sequencing rules — unchanged:**

1. The external artifact-directory preconditions (Phase 0) must **pass before** the disposable
   worktree is created. No worktree may be created first and the artifact location discovered
   invalid afterwards.
2. **No phase may begin before its own blocking decisions are answered** and its prerequisites
   satisfied. No blocker was removed to simplify the sequence.
3. **R-1 and A-1 gate everything.**

**Execution status: NOT AUTHORIZED. A separate explicit operator instruction is required before
any phase begins.**

### 11.3 R-3 — Independent reviewer appointment

| Field | Value |
|---|---|
| **Reviewer** | **ChatGPT** |
| **Kind** | **AI system** (large language model assistant). **Not a natural person.** Recorded as such deliberately. |
| **Role** | Independent Technical Evidence Reviewer |
| **Appointment authority** | Explicitly authorized by the operator in the current conversation |
| **Appointment timestamp** | **NOT SUPPLIED** — none was given and none was manufactured |
| **Signature / attestation** | **NONE** — none exists and none was manufactured |
| **Organizational affiliation** | **NONE RECORDED** — none was supplied and none was invented |
| **Independence requirement** | The reviewer is **not** the OpenCode test runner |
| **Scope** | Independent review of the G3 test-floor evidence and acceptance criteria **C1–C8** |
| **State** | `RESOLVED_CONDITIONAL` |
| **Findings** | **NONE** — an appointment is not a review; no verdict exists |

**Review responsibilities.** The reviewer is asked to examine the evidence package, including:
baseline commit and tree identity; environment fingerprint and interpreter identity; pre-run and
post-run hash manifests; tracked-file scope and unreadable-file records; test collection and
execution logs; stdout, stderr, exit codes, timestamps and duration; guardrail results reported
separately from root-suite totals; stop-condition handling and worktree restoration; and
acceptance criteria C1–C8.

**Reviewer obligations.** The reviewer must **distinguish verified artefacts from agent-reported
claims and from unavailable evidence**, and the review must be **reproducible from the submitted
artefacts to the extent possible**.

**The reviewer does NOT:** execute the test floor · alter results · authorize roadmap progression
· accept G3 on the operator's behalf.

**Authorization ≠ findings.** The operator's *authorization of the reviewer* and the reviewer's
*eventual findings* are separate matters. This record captures only the former. Any later
recorded finding must stand on its own evidence and **must not be inferred from this
appointment**.

#### Governance limitations on using an AI reviewer (recorded, not waived)

1. **AI reviewer.** The reviewer is an AI system, not a natural person or an independent
   organization. "Independence" here therefore means *a different system from the runner* — a
   **weaker** form of independence than an unaffiliated human or third-party reviewer.
2. **Governing process.** Whether the repository's governance **permits AI review for gate
   evidence is not established by any repository record**, and engineering has not ruled on it.
   This is R-3's condition: *if the governing process does not permit AI review, this appointment
   does not satisfy R-3.*
3. **Not a substitute for roadmap §14.12.** This appointment covers the **test-floor evidence
   review only**. It does **not** perform or satisfy the roadmap **§14.12 GLM adversarial
   review**, which remains outstanding and separately required for G3.
4. **No gate authority.** This reviewer holds no authority to accept G3, promote a floor, or
   authorize P4/P10.
5. **Same-session authorship.** The operator authorized the reviewer within the same
   conversational session in which engineering runs. The reviewer's independence of the runner
   is **asserted by role; it has not been independently evidenced**.

---

## 12. Summary of evidence labels used

| Claim | Label |
|---|---|
| Baseline HEAD/tree/branch, status, worktrees, symlinks broken | `PROVEN` |
| Environment figures (interpreter, hash, OS, CPU, RAM, GPU, 117 packages, no lockfile, no pip in venv) | `PROVEN` |
| Committed suite sizes (75 root, 6 nested, 10 guardrail files) | `PROVEN` |
| Prior manifest digests and their mutual identity | `PROVEN` |
| Registry state (6 × PROPOSED, authorities empty) | `PROVEN` |
| Freeze notice ACTIVE | `IMPLEMENTED` |
| Seven historical figures and their transcripts | `REPORTED` (not reproduced — no tests run) |
| `pip` absent from the in-range interpreter | `PROVEN` |
| OOM risk at 3.75 GiB with torch | `INFERRED` |
| Driver-version mapping between the 1318 run and now | `INFERRED` |
| Whether the candidate (Option B) has any untested regression | `UNKNOWN` |
| Nested-suite behaviour on a compliant interpreter | `UNKNOWN` — never run under the declared range |
| Any prospective floor value | `UNKNOWN` — **does not exist until an authorized run** |

---

*Ends here. No test was executed. No commit, push, merge, signature, ratification, promotion,
or phase authorization occurred. G3 remains NOT ACCEPTED; P4 and P10 remain NOT AUTHORIZED;
the P4/RSI freeze notice remains ACTIVE.*
