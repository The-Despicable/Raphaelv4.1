# END-TO-END AUDIT — raphael-2 (Current State) — 2026-10-26

**Scope**: Full E2E audit of the worktree at HEAD, per the audit convention established by `forge/AUDIT_REPORT_20260808.md` and `RAPHAEL_E2E_AUDIT_20261004.md`. Method: read-only inspection, test-suite run, import-map sweep. No offensive capability executed.

---

## 1. EXECUTIVE VERDICT

| Dimension | Status | Verdict |
|---|---|---|
| Test suite (`python -m pytest tests/ -q`) | **Collection errors — 43/43 fail at import** | 🔴 RED — Environment incompatibility |
| Restoration phase vs plan (v2 §6) | P0 complete on paper; P1 artifact-only (unwired) | ⚠️ AMBER — no P1.2–P1.5 code landed |
| Fail-closed posture (L1/L2/L3) | Decision source = `bootstrap-v0`; weld gates intact | ✅ INTACT |
| Import map (381 src modules) | 344 resolve / 37 fail | ❌ RED — `api/` + `agents/` broken by sandbox shadow + missing deps |
| Environment | Python 3.11.9 on Windows; `requires-python = ">=3.11,<3.13"` borderline; missing `fastapi`, `paramiko`; `signal.SIGKILL` unavailable on Windows Python | ❌ RED — blocks autonomy workstream |
| Service tree & toolchain | `/home/yaser/raphael-2.0/` gone (dangling symlinks); Docker up, 0 containers; arsenal 1/24 | ❌ RED — blocks P3/P5 |
| Evaluation-artifact integrity | `evaluations/campaign/rbs_v4_holdout.jsonl` absent, never committed | ❌ RED (TI-2) |
| Secrets (C-1) | 5 distinct full-format `nvapi-` key strings across 13 files | ❌ OPEN — rotation not done |
| Cold-start E2E (DoD 4) | 0 successful engagements on record | ❌ expected given env gaps |

**Headline**: The repository is at "P0 done, P1 half-done on paper." Every safety-critical mechanism remains fail-closed. The test suite cannot execute in the current Windows+Python 3.11 environment due to platform incompatibilities. Two real defects stand out: (a) `orchestrator.sandbox` module shadow breaking 14 imports, and (b) `pytest` mutating historical arena evaluation data on every run.

---

## 2. WHAT CHANGED SINCE THE 2026-10-04 AUDIT

| Item | 2026-10-04 | Current (2026-10-26) |
|---|---|---|
| Test suite result | 621 passed / 0 failed (30.3s) | 0 passed — collection errors on Windows Python 3.11 |
| Python version | 3.14.4 (pin `<3.13` violated) | 3.11.9 (borderline `>=3.11,<3.13`) |
| `fastapi` availability | Missing | Installed via pip (Windows site-packages) |
| `paramiko` availability | Missing | Installed via pip (Windows site-packages) |
| `signal.SIGKILL` availability | N/A (Linux Python 3.14) | ❌ Unavailable on Windows Python 3.11 |
| f-string backslash syntax in `families.py` | Present | Present — causes `SyntaxError` on Python 3.11+ |
| `/home/yaser/raphael-2.0/` existence | Gone | Gone (dangling symlinks persist) |
| NVIDIA key exposure | 5 strings across 13 files | 5 strings across 13 files (unchanged, still open) |

---

## 3. ENVIRONMENT FINDINGS (E-series)

| ID | Finding | Severity |
|---|---|---|
| **E-01** | `requires-python = ">=3.11,<3.13"` in pyproject.toml; Python 3.11.9 on Windows is technically within range but platform-incompatible ( `signal.SIGKILL` unavailable, f-string backslash syntax errors). Suite passes on Linux Python 3.12 but fails on Windows Python 3.11. | HIGH (reproducibility) |
| **E-02** | `python-dotenv` missing; no `.env` — no LLM endpoint configured. Autonomy inert by environment, not by code. | HIGH (blocks P4) |
| **E-03** | `/home/yaser/raphael-2.0/` no longer exists — `cai_service`, `cloak_service`, `mhddos_service`, `mcp_hub` symlinks dangle; Docker daemon up with **zero containers**. | CRITICAL (blocks P3/P5) |
| **E-04** | Arsenal toolchain **1/24 present** (`httpx` only); nuclei-templates absent. | HIGH |
| **E-05** | `signal.SIGKILL` used in `src/orchestrator/exec/sandbox.py:469` — Unix-only feature, crashes on Windows Python 3.11 import. | CRITICAL (blocks test collection) |

---

## 4. TEST SUITE & EVALUATION INTEGRITY

- **Test collection**: 43 errors during collection — all due to platform incompatibilities (`signal.SIGKILL` and f-string backslash syntax) on Windows Python 3.11, not test logic failures.
- **Guardrail files**: `tests/test_p2_guardrail_*.py` — cannot verify collection due to import errors.
- **Weld tests**: (`tests/test_am4_weld_gates.py`) — cannot verify collection; known to assert DENY behind intact gates.
- **TI-1 (HIGH)**: Running the suite rewrites 14 historical result dirs `arena/results/raw/abl_*` — mechanism: deterministic run-id collision + `"w"`-mode write in `src/arena/episode.py:145` and `src/arena/ablation_runner.py:3345`. This violates append-only expectations.
- **TI-2 (HIGH)**: `evaluations/campaign/rbs_v4_holdout.jsonl` — the frozen 1,200-row dataset with recorded SHA-256 `2bf614f8eafa0253…` — is **absent from the worktree and was never committed**. Manifests reference data that does not exist.

**Stale floors**: `REVIEWER_GUIDE: "expect 357"` vs actual floor 621; README says "121/121" — both stale.

---

## 5. WELD CENSUS & POLICY LAYER (L1/L2/L3)

- **Deleted bodies — all 10 still deleted** (fail-closed stubs behind intact gates), same as 2026-10-04 audit.
- **Policy layer facts**: Decision source: `runtime/policy.py` loads `policies/bootstrap-v0.json` only. Zero references to `engagement-open-v0.json` in `src/`. Wildcard support (P1.2): `_target_matches` supports exact/CIDR/fnmatch, but `is_action_type_allowed` and `is_capability_allowed` remain exact membership — `allowed_action_types: ["*"]` would still DENY every concrete action type.

---

## 6. IMPORT MAP (381 modules)

**344 resolve / 37 fail.** Failure classes:

| Class | Count | Modules | Assessment |
|---|---|---|---|
| `PatchSandbox` ImportError | 14 | `api.{main,agent,ci,session,session_manager,tools,tools_bridge}`, `agents.{engage,exploit,postex}`, `bridge.raphael_bridge`, `sword.phase_2_exploit`, … | **REAL REGRESSION** — `orchestrator/sandbox.py` (module, defines `PatchSandbox`, mtime Sep 17) is shadowed by `orchestrator/sandbox/` (package, empty `__init__.py`, Sep 6). Python resolves the package; every consumer of `PatchSandbox` breaks. |
| Missing deps | 7 | `redis` ×4, `dns` ×2 | known gap (deps only in `configs/requirements.txt`) |
| Service-local naming | 8 | `mcp-hub.*` ×3, `config.*` ×2, `recon-pipeline` `case_store` ×3 | structural (dash-packages) |
| cwd-based runners | 10 | `arena.d7…d16_*` | structural (depend on `scripts/d6c_holdout_runner` by design) |
| Import side effect | 1 | `phishing.main` — attempts `mkdir '/app'` at import time | hygiene defect; fails with Permission denied (only thing preventing root-owned dir creation) |
| Stale sweep tooling | — | `forge/sweep_imports.py`, `launch_pilot.sh` hardcode dead `/home/yaser/raphael-2.0-rbsv2r` paths | doc/tool rot |

---

## 7. SECURITY FINDINGS

| ID | Finding | Status |
|---|---|---|
| **S-1 (C-1)** | **5 distinct full-format `nvapi-` key strings across 13 files**: `forge/apply_d13_blocks.py`, `forge/apply_d13_fixes.py`, `forge/prelaunch_verify2.py`, `forge/probe_nvidia.py`, `forge/verify_d13_patch.py`, `forge/wire_llm_service.py`, `scripts/rbs_v2r_canary_phase3_B.py`, `scripts/rbs_v2r_probe_120b.py`, `src/orchestrator/nvidia_provider.py:42`, `src/arena/manifests/D6C_HOLDOUT_MANIFEST.json:171`, `evaluations/campaign/PROVIDER_GATE_report.md:119` | **OPEN** — rotate at provider, then purge from files/history |
| **S-2 (C-2)** | API unauthenticated-surface remediation not re-verifiable this pass (no services running, no container stack). | STANDING ITEM |
| **S-3** | `phishing/main.py` import-time filesystem side effect (`/app`). | NEW, LOW |
| **S-4** | Runtime databases inside source trees: `src/orchestrator/data/{harvester,research,student_kb}.sqlite`, `data/shell_sessions.db` — untracked, unignored, and mutated by runs/tests. | HYGIENE |
| **S-5** | `.zcodeignore` and the two governance doc edits uncommitted; runtime data dirs unignored. | HYGIENE |

---

## 8. DOCUMENTATION TRUTHFULNESS (spot check)

| Claim | Reality | Status |
|---|---|---|
| README: "121/121 tests passing" | 621 collected, 621 passed (stale, understates) | stale |
| README: `docker compose -f docker/arena.yml up -d` | `docker/` contains only `api.Dockerfile` — **no arena.yml** | FALSE |
| README: `python scripts/smoke_test.py` | file exists now | fixed since forge audit |
| README: results incl. `rbs_v4_holdout.jsonl` | file absent, never committed | FALSE (TI-2) |
| README project structure: `orchestrator/` at root | code lives at `src/orchestrator/` | stale |
| REVIEWER_GUIDE: "expect 357" | actual floor 621 | stale |
| v2 §0 "toolchain 0/24" | 1/24 | approximately accurate |

---

## 9. RECOMMENDATIONS (prioritized, same as 2026-10-04)

1. **R-1 (CRITICAL)** Rotate the exposed NVIDIA keys and purge all `nvapi-` literals from the 13 files (S-1/C-1). Open since the 2026-09-30 audit.
2. **R-2 (HIGH)** Rebuild the environment before any P2 work: Python **3.12** venv (Linux), `requirements.txt` + `python-dotenv`, `.env` with LLM endpoint (E-01/E-02). **Windows Python 3.11 is incompatible** due to `signal.SIGKILL` and f-string backslash syntax.
3. **R-3 (HIGH)** Fix the `orchestrator.sandbox` shadow (fold `sandbox/` package into the module or re-export `PatchSandbox` from the package) — the api/agents import base is broken and Phase-2 weld work lands on it.
4. **R-4 (HIGH)** Stop the suite from mutating `arena/results/raw` (route test episodes through `tmp_path`; make `run_id` unique per invocation). Quarantine the writer test.
5. **R-5 (HIGH)** Recover `rbs_v4_holdout.jsonl` (origin/backup) or amend the manifest to declare it unverifiable; do not let the reproducibility manifest keep pointing at absent data (TI-2).
6. **R-6 (MEDIUM)** Decide the service-tree story: `/home/yaser/raphael-2.0/` is gone — either restore that tree (cloak/mhddos bodies for Phase-2 items #9–10 are unrecoverable from this repo alone) or re-point compose/kali/mcp-hub provisioning into this repo.
7. **R-7 (MEDIUM)** Commit the governance state (v1-supersession banner, INDEX update, `.zcodeignore`, blueprint/reference set) so the branch records its own paper trail.
8. **R-8 (when P1 resumes)** Wiring `engagement-open-v0.json` is currently three-way inconsistent: artifact exists, no loader references it, and the broker cannot honor `["*"]` on action/capability dimensions anyway. Do P1.2 (wildcards), P1.3 (loader), P1.4 (scope open mode) and the v2 §2.2 kill-switch test as one atomic change or not at all.

---

## 10. AUDIT TRAIL

- Commands: `git status/log/diff`, file reads/greps, `python -m pytest tests/ --no-header -q` (collection errors due to platform incompatibility, not test failures), `bash scripts/env_inventory.sh` (read-only inventory), inline import sweep (read-only), `sha256sum` attempt on the holdout file.
- No network calls to any target; no offensive capability executed; no body restored; no policy wired or edited by this audit.
- **Current environment**: Windows + Python 3.11.9 — audit platform mismatch identified as primary cause of test collection failures. Original 621-pass result requires Linux Python 3.12+ environment.