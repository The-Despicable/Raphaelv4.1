# RAPHAEL — Product Readiness & Final-Gate Audit

**NON-AUTHORITATIVE AUDIT ARTIFACT.** This report records evidence and findings only. It does
not accept, ratify, or authorize any gate, phase, promotion, or release. Gate acceptance requires
the named architecture authority (GLM) or the operator; this audit cannot and does not perform it.

| Field | Value |
|---|---|
| Audit date (UTC) | 2026-10-09 |
| Repository root | `/home/yaser/external-audits/raphael-2` (also `~/raphael-2.0-rbsv2r`) |
| Branch | `governance/rsi-1-provenance-correction` |
| HEAD | `fc3e2c132591eab7edaa12e97e13fe2d01619411` |
| Tree SHA | `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061` |
| Commit count on HEAD | 188 |
| Working tree | **Dirty — 1 untracked file**: `RAPHAEL_RSI1_INDEPENDENT_AUDIT_FC3E2C132.md` |
| Remotes | `origin` → `The-Despicable/raphael-2.0-rbsv2r`; `canonical` → `The-Despicable/Raphaelv4.1`; `audit-target` → `The-Despicable/raphael-audit-target` |
| Host OS | Windows host / WSL2 Ubuntu (Linux) |
| Python (project venv) | 3.12.15 |
| Python (system) | 3.14.4 |
| Commands executed | Read-only only: `git`, `grep`, `find`, `ls`, `cat`, `sha256sum`, `wc`, `--version`, package-metadata listing, 2 web searches/fetches |
| Tests executed | **NONE — operator permission was "read-only git/grep/list + version probes"** |

---

## 1. Executive verdict

### Overall verdict: `NOT_READY`

### Is P10/G10 fulfilled? **NO — not fulfilled, and not admissible.**

Two independent reasons, either of which alone is decisive:

1. **The gate chain stops at G3.** G0/G1/G2 are recorded as historically passed. **G3 is NOT
   ACCEPTED** — no GLM acceptance ruling exists anywhere in the repository at the audited commit.
   The canonical roadmap (Appendix D) states `G3: BLOCKED`, `AM-4-R3: NOT EXECUTED`,
   `RSI IMPLEMENTATION: NOT STARTED`. P4 and RSI-1 implementation commits nonetheless exist on
   top of that unaccepted gate. G10 is therefore unreachable, not merely unproven.
2. **Confirmed product-critical defects exist independently of the gate.** The frozen evaluation
   instrument has drifted (5 of 9 pinned digests do not match the audited tree; the pinned commit
   does not exist in the object database), the reproducibility manifest internally conflates two
   different campaigns, there is no LICENSE and no lockfile, the package metadata omits 16 runtime
   dependencies, and the repository's own "canonical state" document pins a stale commit.

`NOT_READY` is chosen over `BLOCKED` because the defects above are confirmed product facts, not
merely an external dependency. Within the roadmap, the gate disposition **is** `BLOCKED at G3`.

### Why not `READY` / `CONDITIONALLY_READY`
No gate beyond G2 has been accepted; multiple P0-severity evaluation-integrity findings are
independently reproduced; the declared support envelope has never been satisfied by any recorded
run; and no formal operator-authority artifact for the six open governance decisions exists at
the audited commit.

### Single most important sentence in this report
> The repository contains a large, unusually honest governance-evidence apparatus that
> **documents its own blocked state accurately**, and simultaneously contains post-gate
> implementation, a self-contradicting authoritative weld record, and a pinned evaluation
> instrument that no longer matches the code it claims to have measured.

---

## 2. Audited state, environment, and method

### 2.1 Commands actually run (reproduction set)

```bash
# identity
git -C /home/yaser/external-audits/raphael-2 rev-parse --show-toplevel --abbrev-ref HEAD HEAD 'HEAD^{tree}'
git -C /home/yaser/external-audits/raphael-2 log -1 --date=iso
git -C /home/yaser/external-audits/raphael-2 remote -v
git -C /home/yaser/external-audits/raphael-2 status --short
git -C /home/yaser/external-audits/raphael-2 worktree list --porcelain
git -C /home/yaser/external-audits/raphael-2 merge-base --is-ancestor 07fad8c1 dd fc3e2c13 dd   # exit 0
git -C /home/yaser/external-audits/raphael-2 log --oneline 07fad8c1..fc3e2c132
git -C /home/yaser/external-audits/raphael-2 cat-file -t 74e52eddff698919e5776d8b6cb1ee75dc3159f8  # fatal

# evidence integrity (READ-ONLY, reproduced)
cd evidence/f_split_1_audit_bundle_20261009 && sha256sum -c SHA256SUMS     # 3/3 OK
cd <repo root> && sha256sum -c evidence/phase3_readiness/SHA256SUMS        # 6/6 OK

# frozen-instrument drift (READ-ONLY, reproduced) — see EVAL-001
sha256sum src/arena/d6_manifest.py src/arena/environment.py src/arena/ablation_runner.py \
          src/orchestrator/brain/action.py src/orchestrator/student/stack_matcher.py \
          src/orchestrator/brain/capability_broker.py \
          src/orchestrator/brain/candidate_generators/student_generator.py \
          src/arena/ablation.py src/arena/runner.py

# environment
.venv/bin/python --version          # Python 3.12.15
python3 --version                   # Python 3.14.4
ls .venv/lib/python3.12/site-packages | grep dist-info
```

### 2.2 Method limits (must be read before trusting any PASS in this report)

- **No test was executed.** Operator permission for this audit was explicitly limited to
  "read-only git/grep/list + version probes". Consequently **no claim in this report is labelled
  `[PROVEN]` on the basis of a test run.** Every suite number quoted from repository evidence is
  `[REPORTED]`.
- `src/arena/tests` was **not** executed (prohibited by both operator instruction and by the
  repository's own contamination analysis — see ARCH-002).
- No file in the audited tree was modified. The only write was this report directory.
- Static conclusions are labelled `[INFERRED]` where they rest on reading code rather than
  executing it.

---

## 3. Source-of-truth register and precedence

Precedence is taken verbatim from `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` **Appendix E** (line ~4659):

```
1. Explicit superseding ADR / governance ruling
2. RAPHAEL MASTER ROADMAP v4.2 — this document
3. v4.1 AM-1…AM-14 inheritance summarized in §0.2
4. Earlier v4 roadmap wording
5. Historical audit reports / repository comments
6. Individual model suggestions
```

| # | Path | Rev | Authority level | Date | Status at audit |
|---|---|---|---|---|---|
| S1 | `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` | file as of `fc3e2c132` | **2** (canonical) | Sep 19 2026 header; state block 2026-09-19 | Authoritative. Says G3 BLOCKED, AM-4-R3 NOT EXECUTED, RSI NOT STARTED |
| S2 | `docs/adr/ADR-001…ADR-012` | `fc3e2c132` | 1 (if superseding) | Sep 6 2026 (file mtimes) | **No ADR addresses AM-4-R3, G3 acceptance, or RSI ratification.** Duplicate ADR number 011 (see GOV-005) |
| S3 | `RAPHAEL_STATE.md` | `fc3e2c132` | 5 (repo doc) | Sep 7 2026 | **STALE** — declares itself "Canonical State", pins HEAD `b676d819`, actual HEAD is `fc3e2c132` |
| S4 | `REVIEWER_GUIDE.md` | `fc3e2c132` | 5 | Sep 7 2026 | Contradicts S3: floor "357 passed" (S3) vs "621 passed" (S4) |
| S5 | `evidence/g3_remediation/STATUS.md` | `fc3e2c132` | 5 | Sep 7 2026 | "**G3 NOT ACCEPTED** (no GLM ruling yet)" — consistent with S1 |
| S6 | `evidence/phases/P3_0_reinventory/WELD_SET.md` | `fc3e2c132` | 5 | Oct 4 2026 | **Self-contradictory** (see GOV-002). Claims "ALL 15 WELDED" |
| S7 | `evidence/phase3_readiness/REMEDIATION_MANIFEST.json` | `fc3e2c132` | 5 | Oct 9 2026 | "Phase 3 remains unauthorized"; holdout UNVERIFIABLE; `operator_ratification_complete: false` |
| S8 | `evaluations/campaign/HOLDOUT_CLASSIFICATION_20261009.json` | `fc3e2c132` | 5 | Oct 9 2026 | `classification: UNVERIFIABLE`, `reconstruction_permitted: false` — excellent, self-correcting |
| S9 | `evaluations/campaign/rbs_v4_reproducibility_manifest.json` | `fc3e2c132` | 5 | Sep 3 2026 | **Digest-pinned anchor; internally inconsistent and drifted** (EVAL-001/002). Deliberately not modified per S7 policy |
| S10 | `reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md` | `fc3e2c132` (ancestor `915a66abe`) | 5 | Oct 9 2026 | Accurate account of open blockers; 8 to-do items, several still open at HEAD |
| S11 | `RAPHAEL_RSI1_INDEPENDENT_AUDIT_FC3E2C132.md` | **untracked** | 5 | Oct 9 2026 | Not part of the audited commit. Excluded from gate reasoning |
| S12 | `audit/f-split-1` @ `c1eab3dd2` | `fc3e2c132` | candidate branch | Oct 9 2026 | Bundle hashes verify 3/3 `[PROVEN]`. **Unadjudicated** — transmission to reviewer is an operator act, not performed |
| S13 | `~/audit-rsi1/ratification-wt` | linked worktree, `fc3e2c132` | out-of-tree | Oct 9 2026 | 5 **untracked** files incl. `operator_ratification.py`, `OPERATOR_RATIFICATION_20261009.{json,md}`, 2 test files. **Not in the audited tree → not accepted state** |
| S14 | `*_v5*` roadmap | — | — | — | **Does not exist in the tree.** A "v5 patch" is `[UNKNOWN]`/absent at this commit |

### 3.1 Precedence conflict (unresolved, by design)

S6 (level 5) asserts `AM-4 STATUS: ALL 15 WELDED`. S1 (level 2) asserts `AM-4-R3: NOT EXECUTED`.
S2 contains no superseding ADR. Under Appendix E, **S1 wins and the conflict is a governance
question that must be adjudicated, not silently reconciled by an implementer.** This audit does
not reconcile it.

---

## 4. Criterion-level gate matrix (P0–P10 / G0–G10)

Status vocabulary: `PASS` / `FAIL` / `BLOCKED` / `UNKNOWN` / `DEFERRED` / `NOT_APPLICABLE`.
Evidence labels: `[PROVEN]` (reproduced in this audit) / `[IMPLEMENTED]` / `[REPORTED]` /
`[INFERRED]` / `[UNKNOWN]` / `[BLOCKED]`.

> Distinction enforced throughout: (a) code present, (b) locally tested, (c) independently
> reviewed, (d) formally gate-accepted. Only (d) is a gate PASS. Nothing beyond G2 reaches (d).

### 4.1 Gate summary

| Gate | Criterion source | Status | Basis |
|---|---|---|---|
| **G0** | Roadmap §11.5 | `PASS` (historical) | `[REPORTED]` in `evidence/g3_remediation/STATUS.md:51` |
| **G1** | Roadmap §12.6 | `PASS` (historical) | `[REPORTED]` same source |
| **G2** | Roadmap §13.6 | `PASS` (recorded) | `[REPORTED]` `evidence/phases/P3_0/EVIDENCE.md:16`; also `evidence/phases/G2_RC/` |
| **G3** | Roadmap §14.1–14.12 | **`NOT ACCEPTED` / `BLOCKED`** | `[PROVEN]` absence of any acceptance record; `[REPORTED]` `STATUS.md:17,54`; roadmap lines 25-28, 3508, 3627-3631, 4657-4660 |
| **G4** | Roadmap §15.9 | **NOT REACHED** (P4.1–P4.5 implemented out of order, unaccepted) | `[IMPLEMENTED]` commits 9527ed033, 6f4bd5207, 6f49483a7, 5ba213ac0, d2abdc7fa, 0fa5fa8a3 |
| **G5** | Roadmap §16.7 | `NOT STARTED` | `[IMPLEMENTED]` only `brain/{falsification,contradiction}.py`-level fragments exist; no P5 contract |
| **G6** | Roadmap §17.6 | `NOT STARTED` | No bounded-learning authority; Student learning not activated |
| **G7** | Roadmap §18.6 | `NOT STARTED` | No governed deployment/rollback mechanism |
| **G8** | Roadmap §19.9 | `NOT STARTED / BLOCKED` | Holdout `UNVERIFIABLE`; measurement contract unadopted; statistics policy undefined |
| **G9** | Roadmap §20.5 | `NOT STARTED` | Legacy plane (≈78 not-yet-mediated files) still present; P9 deletion not begun |
| **G10** | Roadmap §21.7 | **NOT FULFILLED** | Neither branch of the gate is satisfiable: no advanced-capability admission note exists, and no RSI admission package exists |

### 4.2 G3 criterion-level detail (the decisive gate)

| # | Criterion (roadmap §14) | Status | Evidence | Label |
|---|---|---|---|---|
| G3.1 | Re-verify all bypasses (P3.1) | `UNKNOWN` | `WELD_SET.md` claims 15/15; F2 record census 150 files; no independent audit at HEAD | `[REPORTED]` |
| G3.2 | Planner request-only (P3.2) | `IMPLEMENTED` | `tests/test_p2_guardrail_*.py` (10 files) exist | `[IMPLEMENTED]` |
| G3.3 | Close Head-1 subprocess paths (P3.3) | `UNKNOWN` | W-15 row: "main.py legacy branch DELETED"; unverified here | `[REPORTED]` |
| G3.4 | Close direct tool path (P3.4) | `UNKNOWN` | W-01…W-13 rows; unverified | `[REPORTED]` |
| G3.5 | Gate capability constructors (P3.5) | `UNKNOWN` | W-13 row; unverified | `[REPORTED]` |
| G3.6 | Fix ExecutionEngine ownership (P3.6) | `UNKNOWN` | not separately evidenced | `[UNKNOWN]` |
| G3.7 | Fold/deprecate mode-local execution (P3.7) | `UNKNOWN` | W-12 row; unverified | `[REPORTED]` |
| G3.8 | Static guardrail (P3.8) | `IMPLEMENTED` | `src/orchestrator/exec/inv1_guard.py` (38 KB) + `tests/test_inv1_effect_lexicon_fixtures.py` | `[IMPLEMENTED]` |
| G3.9 | Dynamic bypass tests (P3.9) | `IMPLEMENTED` | `tests/test_am4_weld_gates.py` — 47 test functions `[PROVEN]` (static count) | `[IMPLEMENTED]` |
| G3.10 | Native sandbox + safe capability (P3.10) | `IMPLEMENTED` | `src/orchestrator/exec/sandbox.py`, `safe_capability.py`, `evidence/phases/P3_0/SANDBOX-V0_EVIDENCE.md` | `[IMPLEMENTED]` |
| G3.11 | MVP demonstration (P3.11) | `IMPLEMENTED` | `evidence/p311_mvp/P311_EVIDENCE.md:98` — "G3: NOT ACCEPTED" | `[IMPLEMENTED]` |
| G3.12 | §14.11 MVP failure criteria (8 items) | `UNKNOWN` | Cannot be evaluated without executing the MVP path; not permitted this audit | `[BLOCKED]` |
| G3.13 | §14.12 GLM adversarial review (10 attack classes) | **`NOT PERFORMED`** | No GLM ruling artifact exists in the repository at `fc3e2c132` | `[PROVEN]` (absence) |
| G3.14 | AM-4-R3 execution record | **`ABSENT`** | `grep -rn 'AM-4-R3' evidence/phases/P3_0_reinventory` → **no matches**; roadmap §40.0.1 declares it "NOT YET EXECUTED" | `[PROVEN]` |

**G3 conclusion:** the *implementation-shaped* criteria are largely `[IMPLEMENTED]`, but the two
criteria that actually constitute the gate — §14.12 adversarial review and the AM-4-R3 execution
record — are **absent**, and the roadmap's own gate-acceptance authority has not ruled.
Per AM-6/AM-12 discipline, `[IMPLEMENTED]` never converts to gate PASS.

### 4.3 G4 criterion-level detail (roadmap §15.9 — evaluated despite non-entry, to show why it fails)

| Criterion | Status | Evidence |
|---|---|---|
| mission/scope actually enforced | `IMPLEMENTED` | `runtime/scope.py`, `runtime/mission_spec.py` | 
| receipts persist | `IMPLEMENTED` | `exec/receipt_store.py` (12 KB) |
| provenance machine-verifiable | **`FAIL`** | EVAL-001: 5/9 frozen digests mismatch; pinned commit absent |
| assertions cannot silently become findings | `UNKNOWN` | falsification module exists; unverified |
| ledger complete and redacted | `UNKNOWN` | no governance decision ledger exists (GOV-003) |
| ExperienceNode durable and lineage-valid | `IMPLEMENTED` | `rsi/experience.py` |
| ExplorationPolicy with stable identity/hash/lineage | `IMPLEMENTED` | `rsi/exploration_policy.py` |
| protected/evolvable boundary explicit and enforced | `UNKNOWN` | not evidenced |
| no candidate improvement deployed yet | `PASS` | `[PROVEN]` by absence of promotion artifacts |
| no AGPL source incorporated | **`FAIL`/UNKNOWN** | No LICENSE anywhere; no SBOM; third-party wrappers (sliver, hashcat, netexec, evilginx, gophish) present; ADR-007 legal-review trigger never discharged |

### 4.4 P10 / G10 admission checklist

Roadmap §21.7: *"PASS requires either (1) justified advanced-capability admission with
security/evaluation/rollback evidence, or (2) an explicit RSI admission package demonstrating the
claimed level without overstating evidence. No L2/L3/L4/L5 claim is accepted merely because the
code contains learning, versioning, or self-modification."*

| Admission requirement | Present? |
|---|---|
| Capability name | No |
| Mission class requiring it | No |
| Evidence existing capabilities are insufficient | No |
| Security and authorization boundary | No |
| Expected evidence output | No |
| Evaluation slot + measurable success/failure criterion | No |
| Dependencies | No |
| Rollback/disablement plan | No |
| Owner and required approvals | No |
| Explicit RSI admission package | No |

**Result: 0 of 10 admission-note fields exist. P10 is not merely unimplemented — it has no
admission request. P10/G10 must not be entered.** Correct current state is `BLOCKED`, with the
next authorized task defined in §14.

---

## 5. Architecture and trust-boundary map

### 5.1 Canonical chain (verified statically)

```
OPERATOR → CLI (src/raphael/main.py)
  → RaphaelRuntime            src/orchestrator/runtime/loop.py:52   "Thin sequencer"   [IMPLEMENTED]
  → STAGE_ORDER (exactly 10)  src/orchestrator/runtime/stages.py:1354                 [PROVEN — counted]
      observe, worldmodel_read, student_candidate, planner_request, broker,
      pep, receipt, worldmodel_integrate, contradiction, replan
  → CapabilityBroker (PDP)    src/orchestrator/brain/capability_broker.py             [IMPLEMENTED]
  → PEP → exec/               src/orchestrator/exec/                                   [IMPLEMENTED]
  → SandboxResult (mechanism) src/orchestrator/exec/sandbox.py                          [IMPLEMENTED]
  → Evidence v1               runtime/evidence_v1.py, exec/evidence_store.py            [IMPLEMENTED]
  → EvidenceGraph             brain/evidence.py                                         [IMPLEMENTED]
Policy artifact: policies/bootstrap-v0.json (3,573 B)                                  [IMPLEMENTED]
```

`run_episode(mission, max_iterations, action_cap, require_scope, episode_outputs)` — loop.py:195.
The born-gating contract is present in code and in the docstring ("No Runtime-wide OFF mode (v4 L8)").

### 5.2 INV-1 — the important scoping truth

`REVIEWER_GUIDE.md:9` asserts `exec/` is the **sole owner** of process/network/file primitives.

Reproduced statically: `grep -rn --include=*.py -E 'subprocess\.(run|Popen|call|check_output)|os\.system|os\.popen|socket\.socket' src/orchestrator | grep -v '/tests/'` → **80 hits across 36 files**; only ~6 of those files are inside `exec/`.

**Resolution (not a hidden defect, but must be stated precisely):** INV-1 is enforced *within the
canonical Runtime import closure* (34 static / 53 loaded orchestrator modules, 0 Arena), not across
`src/orchestrator/` as a whole. `F2_PERIMETER_RECORD.md:91-120` scopes every "no bypass" claim to
that perimeter and is explicit that the legacy plane remains intact. The 001R6 census records
**150 effect files: 78 not-yet-mediated / 6 mediated / 4 reachable notes / 62 dead.**

**Risk:** "dead" is partly established by *import failure* rather than by removal —
`evidence/DEFECT_REGISTER.md:20-24` admits `sword.phase_2_exploit` fails to import and counts as
"1 of the 19 remaining fresh-process import failures". Deadness that depends on a broken import is
fragile: repairing the import can silently resurrect an unmediated primitive.

---

## 6. End-to-end product journey trace

| # | Stage | Result | Label |
|---|---|---|---|
| 1 | Clone | `git clone https://github.com/The-Despicable/raphael-2.0-rbsv2r.git` — README:80 | `[REPORTED]` |
| 2 | Python envelope | README says "3.12+"; `pyproject`/`requirements` pin `>=3.11,<3.13`; recorded suite ran on **3.14.4** (outside range) and on 3.12.15 | **CONFLICT** `[PROVEN]` |
| 3 | venv create | `.venv` present at 3.12.15 | `[PROVEN]` |
| 4 | Install | README:86 `pip install -r requirements.txt`. **No lockfile.** `pip` is **not installed** in `.venv` (`No module named pip`) | **FAIL (reproducibility)** `[PROVEN]` |
| 5 | Configure | `.env.example` (46 lines) → `.env`. `.env` exists, is gitignored (`.gitignore:74`), not read by this audit | `[IMPLEMENTED]` |
| 6 | Validate config | `scripts/validate_env.py` exists (3,595 B) | `[IMPLEMENTED]` — not executed |
| 7 | Bring up stack | README:92-94 admits *"stack bring-up has **not yet been validated** in this working tree"* | **`FAIL` (ops)** `[PROVEN]` |
| 8 | Smoke test | `scripts/smoke_test.py` exists (3,964 B) | `[IMPLEMENTED]` — not executed |
| 9 | Governed demo | `scripts/run_demo_d1.sh` — **well designed**: `set -u`, verifies dvwa container identity + image + network membership before acting, runs governed positive + 3 denial controls, requires verified artifact digest | `[IMPLEMENTED]` (best artifact found) |
| 10 | Canonical run | `run_episode(require_scope=True)` via `src/raphael/main.py` | `[IMPLEMENTED]` |
| 11 | Evidence | `evidence/p311_mvp/`, `evidence/phases/P3_0/` | `[IMPLEMENTED]` |
| 12 | Gate | G3 **NOT ACCEPTED** | **`BLOCKED`** `[PROVEN]` |
| 13 | Evaluation campaign | `scripts/run_rbs_v4_holdout_frozen.py`; canonical JSONL **MISSING**; classification `UNVERIFIABLE` | **`FAIL`** `[PROVEN]` |
| 14 | Shutdown/rollback | No documented shutdown or rollback runbook found | `[UNKNOWN]` |

**Journey verdict:** steps 1-6 are plausible but not reproducible; steps 7-8 are self-declared
unvalidated; step 9 is the strongest single artifact; steps 12-13 are hard failures.

---

## 7. Test / command log (observed results)

No test suite was executed (permission). What *was* reproduced:

| Check | Command | Observed |
|---|---|---|
| F-SPLIT-1 bundle integrity | `sha256sum -c SHA256SUMS` (in bundle dir) | **3/3 OK** `[PROVEN]` |
| Phase-3 readiness bundle integrity | `sha256sum -c evidence/phase3_readiness/SHA256SUMS` (repo root) | **6/6 OK** `[PROVEN]` |
| Frozen instrument commit exists | `git cat-file -t 74e52edd…` | **`fatal: could not get object info`** `[PROVEN]` |
| Frozen tag exists | `git tag -l v4-benchmark-frozen` | **empty** `[PROVEN]` |
| Frozen instrument digests | `sha256sum` on the 9 pinned files | **4 match / 5 MISMATCH** `[PROVEN]` |
| Weld-gate test inventory | `grep -c 'def test_'` on `tests/test_am4_weld_gates.py` | **47** `[PROVEN]` |
| Stage order | read `stages.py:1354-1365` | **exactly 10** `[PROVEN]` |
| Compose hardening | `grep -c healthcheck / read_only / user:` | **0 / 0 / 0**; `cap_add` ×5; `depends_on` ×8 `[PROVEN]` |
| Environment | `.venv/bin/python -V`; `python3 -V` | 3.12.15 / 3.14.4 `[PROVEN]` |
| AMR ratification drafts | `git status` in linked worktree | 5 untracked files, not in audited tree `[PROVEN]` |

**Reported-but-unverified suite numbers** (all `[REPORTED]`, mutually inconsistent across
documents and across dates): 357 (`RAPHAEL_STATE.md:10`), 369 (`evidence/g3_remediation/STATUS.md:23`),
552 (F2 record 001R6), 621 (`REVIEWER_GUIDE.md:28`), 1218 (blocker report §2), 1318
(`REMEDIATION_MANIFEST.json:13`). The configured suite grew across remediation, which is expected —
but **no single authoritative floor is recorded at HEAD**, and none was reproduced here.

---

## 8. Defect register (prioritized)

### P0 — Critical

---

**EVAL-001 — Frozen evaluation instrument has drifted from the audited tree**
`P0 Critical · Confidence High · [PROVEN] · Blocks G3/G4 and every published effect size`

`evaluations/campaign/rbs_v4_reproducibility_manifest.json` pins a "frozen instrument" by 9 sha256
digests and commit `74e52eddff698919e5776d8b6cb1ee75dc3159f8`.

*Expected:* every pinned digest matches; pinned commit and tag resolve.
*Actual:* the commit **does not exist** in the object database; tag `v4-benchmark-frozen` **does
not exist**; **5 of 9 digests mismatch**:

| File | Manifest digest (prefix) | Actual at `fc3e2c132` (prefix) | Result |
|---|---|---|---|
| `src/arena/d6_manifest.py` | `1059bb34` | `1059bb34` | MATCH |
| `src/arena/environment.py` | `a12f7c42` | `c9d3b2b1` | **MISMATCH** |
| `src/arena/ablation_runner.py` | `22a4617c` | `f016e20c` | **MISMATCH** |
| `src/orchestrator/brain/action.py` | `e3e8cdba` | `c450595e` | **MISMATCH** |
| `src/orchestrator/student/stack_matcher.py` | `de67061b` | `de67061b` | MATCH |
| **`src/orchestrator/brain/capability_broker.py`** (canonical PDP) | `0906db74` | `8e0603be` | **MISMATCH** |
| `.../student_generator.py` | `22282327` | `22282327` | MATCH |
| `src/arena/ablation.py` | `678c997a` | `5eb4a853` | **MISMATCH** |
| `src/arena/runner.py` | `9f1bb108` | `9f1bb108` | MATCH |

*Impact:* the instrument that produced the cited campaign results is not the instrument in this
tree, and cannot be reconstructed. **The canonical PDP itself has drifted**, so any authorization
semantics claimed by the historical results are not attributable to today's code.
*Why existing controls missed it:* the integrity gate (`rbs_v4_holdout_integrity_gate.json`) checks
the frozen hash **at the manifest's own commit** (check 8, `mismatches: []`, PASS) — a
self-referential check. There is no re-verification at consumption time.
*Remediation:* mark the manifest's frozen-instrument block `UNVERIFIABLE_DRIFT` (a new, separately
reviewed change — the current policy forbids silently editing the digest-pinned anchor); decide with
the operator whether this invalidates README "Key Results"; add a CI-time re-verification that
compares pinned digests to HEAD and fails closed.
*Regression test:* a manifest-vs-tree digest assertion test, run in the configured suite.
*Rollback:* revert the classification commit; the anchor itself is never auto-rewritten.

---

**EVAL-002 — Reproducibility manifest conflates two different campaigns and certifies the wrong dataset**
`P0 Critical · Confidence High · [PROVEN] · Blocks G4/G8`

Same manifest file:
* `dataset` block: `rbs_v4_holdout.jsonl`, **1200 rows**, sha256 `2bf614f8…`, timestamps
  `2026-08-07T12:11Z → 20:34Z`, `bytes: 2463488` — **Campaign B**.
* `design` block: 12 templates × 9 configs × 30 seeds, `total_runs_expected: 3240`, seeds
  `1072-1101` — **Campaign A**.
* `model_provider`: `gpt-oss:20b-cloud` — Campaign A's provider (Campaign B used
  `nvidia/llama-3.3-nemotron-super-49b-v1`).
* `reproducibility_command`: `scripts/run_rbs_v4_holdout.py` — the **Campaign A** script, not the
  frozen Campaign B script.
* `verification`: gate PASS at `2026-08-05T23:23:13Z` — **~1.5 days BEFORE the declared dataset's
  own start timestamp** — and `rbs_v4_holdout_integrity_gate.json` certifies
  `total_rows_expected: 3240 / found: 3240`, i.e. **Campaign A**, not the declared 1200.

*Expected:* dataset, design, provider, command and gate all describe one campaign.
*Actual:* the manifest is a merge of two, and its "verification" attests to a dataset it does not
declare — and neither dataset is present in the repository.
*Independently corroborated:* `RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md:189-199` reached
the same root cause analytically; `HOLDOUT_CLASSIFICATION_20261009.json` records both campaigns as
`ABSENT_AND_UNVERIFIABLE`.
*Why missed:* the digest-pinned anchor is deliberately protected from modification, so the
inconsistency persists by policy while being documented — but no machine-enforced *consistency*
check between the manifest's own blocks exists.
*Remediation:* add a cross-block consistency validator to `evaluation_gate` (dataset rows ==
design total; gate row count == dataset rows; gate timestamp within dataset window; provider ==
campaign script) that **fails closed** and is run by the configured suite.
*Blocks:* G4 provenance criterion, G8 evaluation validity.

---

**GOV-001 — G3 is unaccepted while P4 and RSI-1 implementation sits on top of it**
`P0 Critical · Confidence High · [PROVEN] · Blocks all phase advancement`

*Expected (roadmap §10 line 698, §36 lines 3508-3528, Appendix D):* no RSI implementation work
before G3; next engineering action is AM-4-R3.
*Actual:* `git merge-base --is-ancestor 07fad8c1 fc3e2c132` → exit 0. Between the G3 remediation
status commit and HEAD there are **37 commits**, including P4.1→P4.5 implementation
(`9527ed033`, `6f4bd5207`, `6f49483a7`, `5ba213ac0`, `d2abdc7fa`, `0fa5fa8a3`) and 20+ `RSI-1:` commits.
No commit, file, or ADR records a G3 acceptance ruling; `git log --all --grep=ACCEPT -i` surfaces
none.
*Corroborating (self-declared):* `evidence/g3_remediation/STATUS.md:17` "G3 **NOT ACCEPTED** (no
GLM ruling yet)"; `REMEDIATION_MANIFEST.json:59` "Phase 3 remains unauthorized"; roadmap lines
3508 / 3627-3631 / 4657-4660.
*Why missed:* the implementer was candid (all the above say so), but the discipline that should
have stopped the sequence was not enforced by any gate check.
*Remediation:* **do not add more RSI-1/P4 work.** Escalate to GLM/operator for a G3 ruling. Add a
machine check that refuses new `rsi/` or P4-phase commits while `G3 != ACCEPTED`.
*Rollback:* RSI-1 work is confined to `src/orchestrator/rsi/`, `evaluations/`, `tests/test_rsi1_*`,
`reports/`, `evidence/`; it can be shelved on a branch without touching the control plane.

---

### P1 — High

---

**GOV-002 — The authoritative weld record contradicts itself**
`P1 High · Confidence High · [PROVEN] · Directly undermines the G3 submission`

`evidence/phases/P3_0_reinventory/WELD_SET.md`:
* **Two identical headings** `## Post-weld status (AM-4; all 15 WELDED under Scope v0)` at **lines 35 and 49** — an append that failed to replace.
* Line 45 says `tests/test_am4_weld_gates.py` (**26 tests**); line 60 says (**47 tests**). The file actually contains **47** test functions `[PROVEN]` — so the stale first copy is the incorrect one.
* Line 12 header: "**AM-4 STATUS: ALL 15 WELDED**"; line 78 (W-14) says "WELDED (gate + deletion; **P9-delete ruling still owed**)"; line 81 says "Remaining not-yet paths: **none (0)**".
* `git log -- <file>` shows only 3 commits; the duplication was introduced by append, not by a reviewed rewrite.

*Impact:* the single artifact a GLM adjudicator would rely on to rule G3 is internally
inconsistent on its face. Under Appendix E it is level-5 evidence and cannot override the roadmap,
but its incoherence weakens the submission.
*Remediation:* produce a single, reviewed `WELD_SET.md` with one status table and one test count,
in a dedicated commit; keep the prior revision in git history as the record of the correction.

---

**GOV-003 — No operator-authority mechanism exists at the audited commit**
`P1 High · Confidence High · [PROVEN] · Blocks G4 ledger criterion and all promotion`

Blocker to-do item 4 specified `src/orchestrator/rsi/governance_registry.py` (append-only
`OperatorDecisionRecord`; engineering writes PROPOSED, ADOPTED requires a distinct authority
principal) and `evidence/GOVERNANCE_DECISIONS_20261009.jsonl`. **Neither exists.**

Instead: `REMEDIATION_MANIFEST.json:55-56` — `"ruling_status": "PENDING_OPERATOR_RATIFICATION"`,
`"operator_ratification_complete": false`. The only ratification package
(`operator_ratification.py`, `OPERATOR_RATIFICATION_20261009.{json,md}` + 2 test files) exists as
**5 untracked files in a secondary worktree** (`~/audit-rsi1/ratification-wt`), outside the audited
tree.

*Impact:* the six operator decisions (holdout recovery-vs-unverifiable, policy-identity mode,
denominator/exclusion semantics, adoption authority, statistical policy, snapshot/replay semantics)
have **no authority ledger and no ratification mechanism**. There is no append-only record, so a
decision cannot be shown to have been made, only inferred from a report.
*Remediation:* implement the registry as specified, seed the six decisions as PROPOSED, then
require the operator to ratify through it. **Do not** adopt any decision via this audit.

---

**EVAL-003 — README publishes statistical results derived from an artifact classified as UNVERIFIABLE**
`P1 High · Confidence High · [PROVEN]`

`README.md:141-150` presents a "Key Results" table — `FULL vs NO_WORLD_MODEL Δ=+0.149, d=+0.773,
**p=3.16e-30**` etc. — sourced from `FINAL_VERDICT_RECORD.md`, and `README.md:118` describes "a
1,200-run holdout evaluation". `HOLDOUT_CLASSIFICATION_20261009.json` classifies that dataset
`UNVERIFIABLE` / `MISSING`. Blocker to-do item 2 required exactly this truth-sync.

*Partially done:* `README.md:133-137` and the Evaluation Artifacts table (`README.md:178`) now mark
the file "**NOT PRESENT in this working tree**". **Not done:** the Key Results table still presents
derived effect sizes as `DEMONSTRATED` with no UNVERIFIABLE marker.
*Impact:* a reader scanning the README sees strong, significant, "demonstrated" results that the
project's own governance record says cannot be verified from this repository.
*Remediation:* add an explicit `SOURCE DATASET: UNVERIFIABLE (see HOLDOUT_CLASSIFICATION_20261009.json)`
banner to the Key Results table and to §Reproduction Steps.

---

**EVAL-004 — Snapshot origin binding is not implemented**
`P1 High · Confidence High · [IMPLEMENTED-absent] · Blocks G8`

Blocker to-do item 5 required `ExperimentSnapshot` to bind authoritative evaluator content identity,
gate-config digest, and anchor identity (the current `evaluator_version` is, by its own docstring, a
non-authoritative label). `src/orchestrator/rsi/snapshot.py` is **7,096 bytes, last modified
2026-10-07T12:03** — i.e. untouched by the 2026-10-09 remediation wave. Item remains open.

---

**SEC-001 — No lockfile; installed environment is many major versions ahead of every declared floor**
`P1 High · Confidence High · [PROVEN] · Blocks G0 reproducibility intent and G4 provenance`

No `poetry.lock` / `uv.lock` / `Pipfile.lock` / `constraints.txt`. All constraints are open lower
bounds (`>=`). Installed (`.venv/lib/python3.12/site-packages`) vs declared:

| Package | Declared | Installed | Delta |
|---|---|---|---|
| transformers | `>=4.41.0` | **5.18.0** | **+1 major** |
| paramiko | `>=3.4.0` | **5.0.0** | **+1 major** |
| mcp | `>=1.27.0` | **2.3.0** | **+1 major** |
| numpy | `>=1.26.0` | **2.5.3** | **+1 major (ABI break)** |
| pandas | `>=2.2.0` | **3.0.6** | **+1 major** |
| cryptography | `>=42.0.0` | **50.0.2** | +8 minor |
| aiohttp | `>=3.9.0` | **3.14.3** | +5 minor |
| fastapi | `>=0.115.0` | **0.142.2** | +27 minor |
| sqlalchemy | `>=2.0.30` | **2.1.3** | ok |
| torch | `>=2.3.0` | **2.14.1** | +11 minor |

Also installed but undeclared: `cuda-toolkit 13.0.3.0`, `nvidia-cudnn-cu13`, `nvidia-nccl-cu13`,
`triton 3.8.0`, `httpx2 2.13.1`, `requests-ntlm`, `pyjwt`, `pywinrm`.

*Impact:* the environment is **not reconstructible**. Every `[REPORTED]` suite number is valid only
for this one machine. A fresh `pip install -r requirements.txt` can silently change major versions
of the LLM stack. `.venv` has **no `pip`** — the documented provisioning path cannot even be
re-run in place.
*Note — positive:* the packages I *could* verify against current advisories are **patched**:
`aiohttp 3.14.3` ≥ fixes for CVE-2026-69244 (3.14.3), CVE-2026-69243 (3.14.2), CVE-2026-54275
(3.14.1), CVE-2026-50269 (3.14.0); `starlette 1.7.0` ≥ fixes for CVE-2026-54283 (1.3.1),
CVE-2026-48817 (1.1.0), CVE-2026-48710 (1.0.1, in CISA KEV); `python-multipart 0.0.32` >
CVE-2024-53981 fix (0.0.18). Sources: NVD + GitHub Security Advisories (see §11).
`[UNKNOWN]` for torch/transformers/numpy/pandas/mcp/paramiko/cryptography/neo4j/pywinrm/requests/jinja2.
*Remediation:* commit a lockfile with hashes; add upper bounds; add a scheduled dependency scan.

---

**SEC-002 — Package metadata omits 16 runtime dependencies**
`P1 High · Confidence High · [PROVEN] · Blocks install/entry gate`

`pyproject.toml:11-27` declares 15 dependencies. `requirements.txt:22-40` adds `fastapi`, `uvicorn`,
`httpx`, `mcp`, `python-multipart`, `dnspython`, `neo4j`, `pywinrm`, `aiofiles`, `jinja2`,
`python-dotenv`, plus test deps. `pip install .` therefore yields a package that cannot import its
own API services. README:86 correctly instructs `pip install -r requirements.txt`, so the metadata
and the documented path disagree.

---

**SEC-003 — No LICENSE, no license metadata, and active offensive payloads shipped in-tree**
`P1 High · Confidence High · [PROVEN] · Blocks G4 "no AGPL source incorporated" and any distribution`

No `LICENSE`/`COPYING`; no `license` field in `pyproject.toml`. Meanwhile the tree contains
first-class offensive capability: `src/orchestrator/c2/sliver_backend.py`, `src/mhddos-service/`,
`src/phishing/` (evilginx / gophish), `src/sword/`, `src/cai-service/`, `src/c2-server/`, and
`failures/CVE-2025-69212-PoC/` whose README documents **webshell deployment, interactive RCE,
reverse shells, and "Download and execute a payload"**.

*Context that raises rather than lowers the severity:* `origin/main` history contains
`7272880f7 chore: purge offensive payloads from working tree (W0.5 scope)`; the audited branch is
named `offensive-restore` and restores them. ADR-007 declares a legal-review trigger for
T3MP3ST-derived concepts; no such record exists.
*Impact:* no license grant for RAPHAEL itself; no license inventory for bundled wrappers
(sliver, hashcat, netexec, evilginx, gophish, sqlmap, hydra, nuclei); no operator-authorization
artifact for offensive use. This is a distribution and legal-exposure risk that must be resolved by
a human authority, not by an auditor.
*Remediation (operator decisions, not engineering):* (a) choose and add a license; (b) produce a
third-party license/SBOM inventory; (c) record an explicit authorized-use posture; (d) decide
whether the PoC directory belongs in the product repository at all.

---

**ARCH-001 — INV-1 is perimeter-scoped, not global; ~78 files remain unmediated and "deadness" is partly import-failure-based**
`P1 High · Confidence High · [IMPLEMENTED] · Accepted-as-scoped, but the gate depends on it`

See §5.2. 80 raw-primitive call sites across 36 non-test files in `src/orchestrator`; 6 are in
`exec/`. Project records 150 effect files: **78 not-yet-mediated / 6 mediated / 4 reachable /
62 dead**. `evidence/DEFECT_REGISTER.md:20-24` states `sword.phase_2_exploit` fails to import and is
"1 of the 19 remaining fresh-process import failures".
*Impact:* the security claim "all execution is Broker-mediated" is true **only for the canonical
Runtime closure**. Any future entry point, service bring-up, or import repair can reach a raw
primitive. A large offensive-capability surface is importable.
*Remediation:* keep the perimeter scoping explicit in every product-facing claim; complete AM-4
welding and the P9 deletion; treat "dead-by-import-failure" as **not deleted**.

---

### P2 — Medium

**GOV-004 — `RAPHAEL_STATE.md` is a stale document that self-designates as canonical**
`[PROVEN]` Line 3: "Canonical HEAD: `b676d8198df003873f52b96c83896d65593a77a2`" — actual HEAD is
`fc3e2c132…`. Line 4 states "Current Phase: §14.5 Evidence v1 IMPLEMENTED / EVIDENCE READY (NOT
accepted)"; line 30 says "Next Gate: §14.5 acceptance (GLM authority)". It also contradicts
`REVIEWER_GUIDE.md` on the floor (357 vs 621). *Remediation:* regenerate or delete; a stale
canonical-state doc is worse than none.

**GOV-005 — Duplicate ADR number 011 with two unrelated subjects**
`[PROVEN]` `docs/adr/ADR-011-arena-clause-addendum.md` ("ADR | 011 (arena-clause addendum) … Status
Accepted") and `docs/adr/ADR-011-sandbox-layer-mechanisms-not-authorization.md`. ADR numbering is
the top precedence level; a collision makes "which ADR-011 applies" ambiguous.

**SEC-004 — Compose stack: no healthchecks, no container hardening, weak committed default credentials**
`[PROVEN]` 15 services, **0 `healthcheck`** despite 8 `depends_on` (start-order only, so readiness
races are expected — the demo script works around this by polling `docker inspect`); **0
`read_only`**, **0 `security_opt`/`no-new-privileges`**, **0 `user:`**; `cap_add` on 5 services
(NET_ADMIN/NET_RAW). Credentials: `TOR_CONTROL_PASS:-changeme` (line 232),
`DB_PASSWORD=p@ssw0rd` (326), `MYSQL_PASSWORD=p@ssw0rd` (341), `MYSQL_ROOT_PASSWORD=rootp@ssw0rd`
(342) — directly contradicting `.env.example:24,43` ("REQUIRED: set a strong password (min 16
chars)"). *Strength (keep):* **all 18 published ports are bound to `127.0.0.1`* — a genuinely good
default.

**SEC-005 — `scripts/JUDGE.py` raises at import on Python ≥3.13, and the system Python is 3.14.4**
`[PROVEN]` `JUDGE.py:51-56` is a module-level `raise RuntimeError`. On this host `python3` is 3.14.4,
so the project's primary evaluator cannot be imported without explicitly activating `.venv`.
README:72 says "Python 3.12+" with no upper bound. Module-level raise also breaks tooling that
imports the module to inspect it.

**SEC-006 — Packaging metadata references packages that do not exist; four service dirs are unpackageable**
`[PROVEN]` `[tool.setuptools.packages.find] include` lists `config*` and `benchmarks*`; neither
`src/config` nor `src/benchmarks` exists. `src/{c2-server,cai-service,mcp-hub,recon-pipeline}` are
not valid Python identifiers and are excluded from the wheel.

**ARCH-002 — The legacy evidence-contamination path is still open**
`[PROVEN]` `tests/conftest.py` installs an autouse fixture redirecting
`arena.ablation_runner.RESULTS_BASE` to `tmp_path` — the top-level suite **is** isolated.
`src/arena/tests/conftest.py` **does not exist** (blocker to-do item 6, unimplemented). Because
`arena` run IDs are deterministic by design (`tests/conftest.py:4-9`), running the nested suite
still overwrites tracked historical evidence — the exact incident recorded in
`evidence/arena_contamination_20261004/README.md` (14 directories rewritten on 2026-10-04).
*This is the documented reason the nested suite must not be run in the primary worktree.*

**COR-001 — Defect register incomplete**
`[PROVEN]` `evidence/DEFECT_REGISTER.md` contains only `DR-001`. Blocker to-do item 7 required
`DR-002` (F1 — second pinned-anchor read) and `DR-003` (F4 — schema-v2 digest-semantics span).

**OPS-001 — Deployment is self-declared unvalidated; no reproducible clean-install record**
`[PROVEN]` `README.md:92-93`: *"stack bring-up has not yet been validated in this working tree"*;
`launch_pilot.sh` refuses to run without a pre-provisioned `.venv`.

**OPS-003 — No CI binding for the configured suite at this commit**
`[IMPLEMENTED]` `ci-templates/.gitlab-ci.yml` + `Jenkinsfile` exist; there is **no `.github/`** and
no evidence of any CI run bound to `fc3e2c132`. The floor numbers are self-reported transcripts.

**DOC-001 — Three-way contradiction on the supported Python environment**
`[PROVEN]` README "3.12+" (line 72) vs `pyproject` `>=3.11,<3.13` (line 10) vs recorded evidence on
**3.14.4** (`evidence/g3_remediation/STATUS.md:42-47`, which explicitly flags the mismatch and says
"NOT concealed"). The *declared frozen pin has never been satisfied by any recorded run.*

### P3 — Low

**OPS-002** — `scripts/run_help.sh` hardcodes `cd /home/yaser/raphael-2.0`, a path that does not
exist in this worktree (the repo is at `/home/yaser/external-audits/raphael-2`). This is exactly the
"hard-coded path assumptions" class roadmap P0.2 requires recording.

**GOV-006** — No ADR or roadmap amendment records any change to the AM-4-R3/G3 status implied by
`WELD_SET.md`. Under Appendix E the discrepancy must become a governance question; it has not.

---

## 9. Performance findings

### Classification: **PERFORMANCE IS UNCHARACTERIZED.** Not PASS, not FAIL.

Evidence:
* `grep -rln -iE 'p50|p95|p99|latency benchmark|throughput' evidence reports` → **zero matches**
  across the entire evidence and report corpus.
* `benchmarks/` contains only **scenario / security / target** benchmarks (`RBS-v1`, `RBS-v2`,
  `RBS-v4`, `RQ-015`, `targets/`) — no timing harness, no load profile, no percentile reporting.
* No hardware fingerprint, model/provider latency profile, concurrency assumption, or accepted
  service target exists anywhere in the repository.
* The **only** performance statement in the project is `docs/LIMITATIONS.md` **L-001 "Cognitive loop
  latency 30–120 s/cycle" (Severity MEDIUM)**, surfaced in `README.md:161`. `[REPORTED]` — never
  instrumented, never given a distribution, sample size, environment, or confidence interval.

I did not run a benchmark: permission was read-only, no baseline exists to compare against, and
inventing a target would be exactly the failure mode this audit is meant to prevent.

### Proposed benchmark protocol (requires operator approval before execution)

1. **Workload model** — three missions derived from `evidence/p311_mvp/p311_mvp_mission.json`:
   *W-small* (1 episode, safe capability, no LLM), *W-typical* (1 episode, Student + Planner + one
   LLM call), *W-large* (5 episodes, action cap 5, LLM per iteration).
2. **Fixed environment** — commit SHA + tree SHA, `.venv` interpreter hash, `pip freeze` output,
   CPU model/count/RAM/GPU, container image digests, model ID + provider + temperature 0.
3. **Instrumentation** — per-stage wall time in `run_episode`; report p50/p95/p99 **only if n ≥ 100**
   (otherwise min/median/max with n stated); separate cold-start (first episode) from warm.
4. **Secondary counters** — LLM tokens/cost per episode, queue wait, artifact bytes written,
   evidence-store entries, receipt count.
5. **Acceptance** — propose (for human approval, not as a roadmap requirement) p95 stage-latency
   budgets per stage; do **not** adopt until GLM/operator ratify.
6. **Isolation** — run in a disposable worktree with before/after `sha256sum` manifests of
   `arena/results/` and `evidence/` (see ARCH-002) — non-negotiable.

---

## 10. Security, reliability, operations, evaluation-validity, deployment, docs gaps

| Area | Finding | Severity |
|---|---|---|
| Authentication | `.env.example` requires `API_KEY` ≥32 chars; compose services exist for 15 back-ends. Not audited at runtime (no execution permitted) | `[UNKNOWN]` |
| Authorization | Single canonical Broker; perimeter-scoped. **Strength**: `enforce_broker_mediation` + `WeldNotAuthorized` fail-closed pattern is explicit and tested-by-design | `[IMPLEMENTED]` |
| Sandbox | Mechanism-not-authorization layering is documented in a dedicated ADR-011 and honoured by `exec/sandbox.py` | `[IMPLEMENTED]` |
| Fail-closed | Strongly present in measurement/holdout/policy-identity paths — `HOLDOUT_MISSING`, `derived=False`, `PENDING_OPERATOR_RATIFICATION` all fail closed | `[IMPLEMENTED]` — **project strength** |
| Container isolation | None beyond `cap_add`; all services root, no `read_only`/`no-new-privileges` | P2 |
| Secrets | `.env` correctly gitignored (`.gitignore:74`) and untracked `[PROVEN]`; **but** compose ships weak fallback credentials in-repo | P2 |
| Network | All published ports loopback-bound `[PROVEN]` — **strength** | — |
| Dependency CVEs | Verified patched for aiohttp / starlette / python-multipart; **no scan exists**, no SBOM, no lockfile | P1 |
| Audit-log integrity | `audit_trail.py` exists; append-only guarantee not verified | `[UNKNOWN]` |
| Reliability | No timeouts/retries/backoff/rate-limit policy found for canonical Runtime; `MAX_SPEND_TOKENS`/`RAPHAEL_COST_CONTROL` exist in `.env.example` but enforcement not traced | `[UNKNOWN]` |
| Migrations | None needed (no DB schema layer found) | N/A |
| Backups / DR | None documented; `evidence/` and `evaluations/` have no retention policy | P2 |
| Telemetry | `safety_telemetry.py`, `token_telemetry.py` tests exist; no metrics/tracing backend | P2 |
| Data retention | `.gitignore:87` blocks `evaluations/campaign/*.jsonl` — this is why the canonical holdout **cannot be committed**; a governance rule has become a data-loss mechanism | P2 |
| Docs | README/S1/S3/S4 mutually contradictory on HEAD, floor, and Python version | P2 |

---

## 11. External research (primary sources, versions actually installed)

| Finding | Version installed | Source | Applicability |
|---|---|---|---|
| CVE-2026-69244 aiohttp out-of-bounds heap read in C response parser (DoS); fixed **3.14.3** | aiohttp **3.14.3** | SUSE CVE-2026-69244; aio-libs GHSA-cq5v-8q36-5273 | Installed version **is the fix** — not affected |
| CVE-2026-69243 aiohttp HTTP request smuggling via WebSocket upgrade; fixed **3.14.2** | aiohttp **3.14.3** | NVD CVE-2026-69243; GHSA-mfx4-hv73-q22v | Not affected |
| CVE-2026-54275 aiohttp TLS SNI check bypass on connection reuse; fixed **3.14.1** | aiohttp **3.14.3** | NVD CVE-2026-54275 | Not affected |
| CVE-2026-50269 aiohttp CRLF/header injection via MultipartWriter headers; fixed **3.14.0** | aiohttp **3.14.3** | NVD CVE-2026-50269 | Not affected (low likelihood anyway) |
| CVE-2026-34993 aiohttp `CookieJar.load()` deserialization RCE; fixed **3.14** | aiohttp **3.14.3** | GHSA-jg22-mg44-37j8 | Not affected |
| CVE-2026-54283 starlette `request.form()` limits ignored for urlencoded (CVSS 7.5); fixed **1.3.1** | starlette **1.7.0** | NVD CVE-2026-54283; GHSA-82w8-qh3p-5jfq | Not affected |
| CVE-2026-48817 starlette HTTPEndpoint unsafe `getattr` dispatch (auth bypass); fixed **1.1.0** | starlette **1.7.0** | NVD CVE-2026-48817; GHSA-x746-7m8f-x49c | Not affected |
| CVE-2026-48710 starlette Host-header request smuggling; fixed **1.0.1**; **in CISA KEV** (added 2026-09-02) | starlette **1.7.0** | NVD CVE-2026-48710 | Not affected |
| CVE-2024-53981 python-multipart boundary-deformation DoS; fixed **0.0.18** | python-multipart **0.0.32** | GHSA-59g5-xgcq-4qw3 | Not affected |

**Honest limit:** I verified only these packages. `torch 2.14.1`, `transformers 5.18.0`,
`numpy 2.5.3`, `pandas 3.0.6`, `mcp 2.3.0`, `paramiko 5.0.0`, `cryptography 50.0.2`,
`neo4j 6.3.1`, `pywinrm 0.5.0`, `requests 2.34.2`, `jinja2 3.1.6` are **`[UNKNOWN]`** — not
checked. Given no lockfile exists, this check is a point-in-time snapshot of one machine and does
**not** substitute for a scheduled scan. Note also that `pywinrm 0.5.0` is a long-unmaintained
package performing privileged remote execution; that is an architectural exposure worth an
explicit operator decision regardless of CVE status.

---

## 12. Known limitations of this audit

1. **No test executed** — by operator restriction. No behavioural claim in this report is
   independently proven by execution. Every suite number is `[REPORTED]`.
2. **No import/runtime check** — the reported "19 fresh-process import failures" could not be
   reproduced; it is `[REPORTED]`.
3. **Static analysis only for control flow** — I confirmed the *presence* of Runtime/Broker/PEP/
   exec/ artifacts and the exact 10-stage order, but did **not** prove the absence of a second
   cognitive loop or a bypass by exhaustive call-graph analysis. Treat "no bypass found" as
   `[UNKNOWN]`, not PASS.
4. **Single-repository scope** — `raphael-redteam`, `chimera`, `Vesper`, and the out-of-tree
   ratification drafts were excluded per operator scope decision.
5. **Advisory coverage partial** — see §11.
6. **Performance** — not measured at all; see §9.
7. I did not read `.env` (secret-handling rule) and did not access any network target.

---

## 13. Prioritized remediation plan (dependency-ordered)

**Phase A — Stop the bleeding (no new feature work; do first)**
1. `A1` Freeze further RSI-1 / P4-phase commits until G3 is ruled. *(GOV-001)*
2. `A2` Reconcile `WELD_SET.md` into one reviewed status table with one test count; keep the old
   revision in history. *(GOV-002)*
3. `A3` Publish an `AM-4-R3` execution record or a formal statement that the weld work already
   landed under a different task ID — either way, make the roadmap's §40.0.1 block consistent with
   reality via an explicit ADR. *(GOV-002, GOV-006)*
4. `A4` Mark the frozen-instrument block `UNVERIFIABLE_DRIFT`; **do not rewrite the pinned anchor**.
   *(EVAL-001)*
5. `A5` README truth-sync: banner the Key Results table as derived from an UNVERIFIABLE dataset.
   *(EVAL-003)*

**Phase B — Close the reproducibility and supply-chain gaps**
6. `B1` Commit a hashed lockfile; add upper bounds to all `>=` constraints; add `pip` to `.venv`.
   *(SEC-001)*
7. `B2` Reconcile `pyproject` dependencies with `requirements.txt`; fix the `packages.find`
   include list; decide the fate of the four hyphenated service packages. *(SEC-002, SEC-006)*
8. `B3` Add dependency scanning + SBOM generation to CI. *(SEC-001)*
9. `B4` Add compose `healthcheck` to all services, `read_only`/`no-new-privileges`/`user:` where
   feasible; remove the `changeme` / `p@ssw0rd` fallbacks so missing secrets fail closed.
   *(SEC-004)*

**Phase C — Governance machinery (must exist before any gate can be honestly accepted)**
10. `C1` Implement `governance_registry.py` + seed the six decisions as PROPOSED. *(GOV-003)*
11. `C2` Add `src/arena/tests/conftest.py` + before/after sha256 manifest proof. *(ARCH-002)*
12. `C3` Add DR-002 / DR-003 to the defect register. *(COR-001)*
13. `C4` Regenerate or delete `RAPHAEL_STATE.md`; reconcile the floor number across all documents;
    resolve the duplicate ADR-011. *(GOV-004, GOV-005)*
14. `C5` Implement snapshot origin binding. *(EVAL-004)*
15. `C6` Add the manifest cross-block consistency validator (EVAL-002) and a
    manifest-vs-HEAD digest re-verification (EVAL-001) to the configured suite.

**Phase D — Gate submission**
16. `D1` Assemble the G3 evidence package from A1-A6 + B + C, with one authoritative floor number,
   one environment fingerprint, and an explicit scope-deviations field (AM-8).
17. `D2` Submit to GLM for the §14.12 adversarial review and a **G3 ruling**.
18. `D3` Only after G3 PASS: begin P4 per a new phase contract.

**Phase E — Later (explicitly NOT authorized now)**
19. P5–P10, benchmark execution per §9 protocol, license/authorization posture.

---

## 14. The single next authorized task

**Task: prepare and submit the G3 gate package for architecture-authority adjudication — and
obtain the G3 ruling. Nothing else.**

*Why this and not P10:* the roadmap's Appendix D names `NEXT ENGINEERING STEP: AM-4-R3` and
`G3: BLOCKED`. P10 admission has **0 of 10** required fields and is unreachable through seven
unaccepted gates. Implementing any further RSI-1 capability now would compound GOV-001.

**Engineering prerequisite (authorized now):** items `A1`–`A5` and `C1`–`C3` above.

**Required evidence for acceptance:**
1. A single internally consistent `WELD_SET.md` with one status table and one verified test count.
2. An explicit ADR or amendment recording the true AM-4-R3 / weld status, and its relationship to
   the roadmap's Appendix D block.
3. One authoritative test floor with an environment fingerprint (commit SHA, tree SHA, interpreter
   hash, `pip freeze`) — the five mutually inconsistent numbers must be resolved to one.
4. `sha256sum` manifests proving `arena/results/` and `evidence/` are byte-identical before and
   after the configured suite, plus after the nested suite (post-`src/arena/tests/conftest.py`).
5. A `governance_registry` with the six operator decisions recorded as PROPOSED and **none** adopted.
6. A manifest-vs-HEAD digest re-verification result (expected to FAIL per EVAL-001) and a
   documented decision on the consequence for published effect sizes.

**Independent-review owner:** GLM (architecture authority, per roadmap §1.1) for the G3 ruling;
operator for all ratification and legal/licensing decisions.

**Acceptance criteria:** §14.11's eight MVP failure criteria all demonstrated, and §14.12's ten
adversarial attack classes attempted and shown to fail per policy with traceable evidence.

**Rollback:** all remediation commits are additive to `evidence/`, `reports/`, `docs/`, and
`src/orchestrator/rsi/`; the control plane (`runtime/`, `brain/capability_broker.py`, `exec/`) is
untouched, so the whole G3 package can be shelved on a branch without architectural risk.

---

## 15. Explicit operator decisions required (I will not fill these in)

1. **G3 ruling** — accept / reject / conditional. Blocks everything.
2. **Holdout** — authorize provenance recovery outside this repository, or formally accept permanent
   `UNVERIFIABLE`?
3. **Frozen-instrument drift (EVAL-001)** — do the published README effect sizes stand, or are they
   withdrawn? This is a research-claims decision, not an engineering one.
4. **22 historical `split="validation"` call sites** — per-site intent ruling (DEV-as-run vs
   mislabelled validation). No mass rewrite.
5. **Six PROPOSED governance decisions** — holdout policy, `require_policy_identity` in adopted
   configs, denominator/exclusion semantics, adoption authority, statistical policy, snapshot/replay
   semantics.
6. **F-SPLIT-1 bundle transmission** — send `evidence/f_split_1_audit_bundle_20261009/` to the
   independent reviewer and record their verdict; then adjudicate `audit/f-split-1`.
7. **License & authorized-use posture (SEC-003)** — RAPHAEL's own license; third-party license
   inventory; whether offensive-capability modules and the CVE PoC directory belong in the product
   repository; whether `pywinrm`-style privileged remote execution is acceptable at all.
8. **Performance** — approve or amend the §9 benchmark protocol and any provisional thresholds.
9. **CI** — bind the configured suite to a real runner (`.gitlab-ci.yml` vs Jenkins vs GitHub
   Actions), given `origin/main` has no CI and no `.github/` exists.

---

*End of audit. No gate accepted, no stage authorized, no source modified. Verdict: `NOT_READY`;
P10/G10 **not fulfilled**; roadmap position `BLOCKED` at G3.*
