# RAPHAEL — G3 Remediation and Evidence Closure

**NON-AUTHORITATIVE.** This is a remediation patch and evidence package prepared for
independent review. It does **not** accept a gate, rule on a gate, ratify an operator
decision, or authorize any phase. G3 remains **NOT ACCEPTED**.

---

## 1. Verified repository identity and starting state

Baseline re-verified before any edit. **No divergence** — the expected values matched.

| Field | Expected | Verified | Match |
|---|---|---|---|
| Root | `/home/yaser/external-audits/raphael-2` | same | ✅ |
| Branch | `governance/rsi-1-provenance-correction` | same | ✅ |
| HEAD | `fc3e2c132591eab7edaa12e97e13fe2d01619411` | same | ✅ |
| Tree | `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061` | same | ✅ |
| Commits on HEAD | — | 188 | — |
| Remotes | origin / canonical / audit-target | all three present | ✅ |
| Linked worktrees | 3 | 3 (`ratification-wt`, stale-prunable `/tmp/rbase-b6ef24`) | ✅ |
| Tracked modifications | none | none | ✅ |
| Staged modifications | none | none | ✅ |
| Untracked at start | — | `RAPHAEL_RSI1_INDEPENDENT_AUDIT_FC3E2C132.md`, `reports/product-readiness/` | recorded |
| Stashes | — | 9 pre-existing, untouched | ✅ |

```console
$ git -C /home/yaser/external-audits/raphael-2 rev-parse --abbrev-ref HEAD HEAD 'HEAD^{tree}'
governance/rsi-1-provenance-correction
fc3e2c132591eab7edaa12e97e13fe2d01619411
e24d42bf7f7655293f3eb3a273c9ce4d94b1e061
$ git status --porcelain      # at start: only the two untracked entries above
```

Because the baseline matched, the "stop and report divergence" condition did not fire.

### Governance state relied upon

Checked for a newer superseding ruling before relying on the blocked status: **none found.**
`git log --all --grep=ACCEPT -i` surfaces no gate acceptance; `docs/adr/` contained no ADR
addressing AM-4-R3 or G3 acceptance before this task. The roadmap Appendix D state
(`AM-4-R3: NOT EXECUTED`, `G3: BLOCKED`, `RSI IMPLEMENTATION: NOT STARTED`) therefore stands
and was treated as authoritative.

---

## 2–3. Changes made, and exact files changed

**3 files modified, 10 files created. No test, policy, code path, or evaluation artifact was
modified except where explicitly authorized below.**

| Item | File | Change | Rationale |
|---|---|---|---|
| **A1** | `evidence/governance/P4_RSI_FREEZE_NOTICE_20261009.md` | **new** | Records the existing roadmap sequencing constraint where someone starting P4/RSI would find it, plus an explicit human review procedure. Deliberately **no** CI gate or pre-commit hook — that would be a new governed surface. |
| **A2** | `evidence/phases/P3_0_reinventory/WELD_SET.md` | **modified** | Removed the stale duplicated status section; added a state-by-state reading guide separating *code present* / *tests present* / *tests executed* / *independent review* / *gate accepted*; de-ambiguated the "ALL 15 WELDED" summary against the still-owed P9 deletion ruling. |
| **A3** | `docs/adr/ADR-013-am4-r3-status-and-precedence-conflict.md` | **new** (180 lines) | Records the true AM-4-R3 status under Appendix E precedence, retains `NOT EXECUTED`, and refers the conflict to the authority. |
| **A4** | `evidence/frozen_instrument_drift/UNVERIFIABLE_DRIFT_20261009.{md,json}` | **new** (174 + 169 lines) | `UNVERIFIABLE_DRIFT` record with reproduced commands/outputs. **The pinned anchor was not touched.** |
| **A5** | `README.md` | **modified** | Verification-status banner + reproduction-step warning + Key Results provenance warning, scoped to the affected claims only. |
| **C1** | `src/orchestrator/rsi/governance_registry.py` | **new** (461 lines) | Minimal decision ledger: PROPOSED/ADOPTED/REJECTED/SUPERSEDED, transition table, content hash, fail-closed, no self-adoption. |
| **C1** | `evidence/GOVERNANCE_DECISIONS_20261009.jsonl` | **new** (6 records) | The six open operator decisions, **all PROPOSED**, no authority identity or date. |
| **C1** | `scripts/gen_governance_decision_seeds.py` | **new** (201 lines) | Generates the seeds reproducibly so hashes are provably correct rather than hand-typed. |
| **C1** | `tests/test_rsi1_governance_registry.py` | **new** (318 lines) | 40 unit tests. |
| **C1** | `tests/test_rsi1_governance_registry_adversarial.py` | **new** (244 lines) | 17 adversarial tests attacking the ability to manufacture authority. |
| **C2** | `src/arena/tests/conftest.py` | **new** (144 lines) | Two-layer guard: prevention (redirect `RESULTS_BASE`) + detection (session-scoped fingerprint of protected trees). |
| **C3** | `evidence/DEFECT_REGISTER.md` | **modified** | Added DR-002 (F1) and DR-003 (F4), each with source citation, code grounding, closure conditions and retained uncertainty. |

---

## 4. Reproduction commands and actual outcomes

All commands run from `/home/yaser/external-audits/raphael-2` unless stated.

### A4 evidence reproduction

```console
$ git cat-file -t 74e52eddff698919e5776d8b6cb1ee75dc3159f8
fatal: git cat-file: could not get object info          # exit 128   [PROVEN]

$ git tag -l v4-benchmark-frozen
(no output)                                             #           [PROVEN]

$ sha256sum evaluations/campaign/rbs_v4_reproducibility_manifest.json
c26ed773ba57d43d53e150acb90db8299aa565f9ea7b2646a7820aa2c9775757   [PROVEN]
  → matches AUTHORITATIVE_ANCHORS.holdout_anchor_sha256 in evaluation_gate.py:174-178
  → THE ANCHOR IS INTACT. Drift is inside the manifest, not in the anchor's bytes.
```

Manifest-frozen digests at this revision: **4 MATCH / 5 MISMATCH**, including the canonical
PDP `src/orchestrator/brain/capability_broker.py` (`0906db74…` pinned vs `8e0603be…` actual).

### C1 targeted tests

```console
$ PYTHONPATH=src .venv/bin/python -m pytest \
    tests/test_rsi1_governance_registry.py \
    tests/test_rsi1_governance_registry_adversarial.py -q --no-header
.........................................................                [100%]
57 passed in 0.97s
```
`[PROVEN]` — observed exit status 0.

```console
$ PYTHONPATH=src .venv/bin/python scripts/gen_governance_decision_seeds.py
wrote 6 records to evidence/GOVERNANCE_DECISIONS_20261009.jsonl
authoritative decisions: 0 (expected 0)
```
Re-run and diffed against the previous output: **identical** → seed generation is
deterministic. `[PROVEN]`

### C2 isolated-worktree proof

Worktree created **outside** the primary worktree, used, and removed:

```console
$ git worktree add --detach /home/yaser/audit-rsi1/g3-verify-wt fc3e2c132
HEAD is now at fc3e2c132 RSI-1: add evidence-based historical split call-site adjudication package
```

Protected-trees fingerprint (58,929 files), before and after running the nested suite in
that worktree:

| | Manifest SHA-256 |
|---|---|
| BEFORE | `aea6970c2dcde9ca07b53d95ea7078dfceb92bc9a6bb4363d7a7b119cde725a6` |
| AFTER | `aea6970c2dcde9ca07b53d95ea7078dfceb92bc9a6bb4363d7a7b119cde725a6` |
| `diff` line count | **0** |

```console
$ git status --short        # inside the worktree, after the nested run
?? src/arena/tests/conftest.py      # only the file I copied in; nothing else touched
```

Nested suite result in the isolated worktree:

```
1 warning, 4 failed, 69 passed in 5.01s
```
The **4 failures are pre-existing legacy failures**, not caused by this task — they are in
`test_evaluator_robustness.py` / `test_runconclusion.py` and are consistent with the recorded
project state that `src/arena/tests` is a legacy suite. **No contamination-guard error was
raised.** Labelled `[PROVEN]` for the isolation property; the suite outcome itself is
`[REPORTED]` as to cause and is **not** claimed as fixed.

### C2 negative control — the guard actually detects contamination

Required, because "the suite passed" is not evidence that history was preserved.

A disposable test wrote one file into `arena/results/raw/` using an absolute path, escaping
the prevention fixture:

```console
$ PYTHONPATH=src .venv/bin/python -m pytest \
    src/arena/tests/test_zz_g3_guard_negative_control.py -q --no-header
.E                                                                       [100%]
==================================== ERRORS ====================================
___ ERROR at teardown of test_negative_control_writes_into_protected_evidence ___
CONTAMINATION GUARD: the nested Arena suite modified protected historical evidence while running.
  arena/results: +1 added, -0 removed, ~0 changed
First changed paths (up to 10):
    .../arena/results/raw/_G3_GUARD_NEGATIVE_CONTROL/planted.jsonl
1 passed, 1 error in 3.92s
```

The test **passed**; the session **errored** and named the exact path. Detection layer proven
to work rather than merely reporting green. `[PROVEN]`

### Other checks

```console
$ git diff --check                # no output — clean            [PROVEN]
$ .venv/bin/python -m py_compile <5 new python files>
PY_COMPILE_OK                                                   [PROVEN]
$ .venv/bin/python -m json.tool evidence/frozen_instrument_drift/UNVERIFIABLE_DRIFT_20261009.json
JSON_OK_drift                                                   [PROVEN]
$ .venv/bin/python -m json.tool reports/product-readiness/RAPHAEL_PRODUCT_READINESS_2026-10-09.json
JSON_OK_audit                                                   [PROVEN]
$ PYTHONPATH=src .venv/bin/python -m pytest tests/ --collect-only -q
1509 tests collected in 12.32s                                # COLLECTION ONLY, NOT A RUN
```

The collect-only result is **not** a pass claim. It only establishes that the new files did
not break collection. **The full suite was not run** — out of authorized scope.

---

## 5. Before/after hashes for protected historical evidence

Scope: **all git-tracked files**, identical before and after (67,641 hashed; the 4 broken
symlinks `cai_service`, `cloak_service`, `mcp_hub`, `mhddos_service` are unreadable and
excluded from both manifests identically — pre-existing, out of scope).

| Manifest | Files | SHA-256 of manifest |
|---|---|---|
| `hashes/BEFORE_protected.sha256` | 67,641 | `5a672359b52c0a005ca9a63fef8311e989f786e079b1dbf8b8db02f63bc0f384` |
| `hashes/AFTER_all_tracked.sha256` | 67,641 | (see file) |
| `hashes/DELTA_tracked.txt` | 12 lines | — |

**Delta: exactly 3 tracked files changed, 0 added, 0 deleted.**

| File | Item | Authorized? |
|---|---|---|
| `README.md` | A5 | ✅ authorized |
| `evidence/DEFECT_REGISTER.md` | C3 | ✅ authorized |
| `evidence/phases/P3_0_reinventory/WELD_SET.md` | A2 | ✅ authorized |

**All other 67,638 tracked files are byte-identical**, including the entire `arena/results`
tree (52,008 files), `src/arena/results` (6,510), `src/arena/arena/results` (30), and every
other evidence, evaluation, failure, baseline, config, policy and docs artifact.

> Historical evidence stayed byte-identical **except** `evidence/DEFECT_REGISTER.md`, whose
> modification is the authorized C3 deliverable. That one file is protected-path *and*
> intentionally changed; it is called out here rather than averaged into the clean figure.

---

## 6. Updated defect and decision registers

### Defect register

`DR-002` (F1 — second pinned-anchor read) and `DR-003` (F4 — schema-v2 digest-semantics
span) added. Both are **`DEFERRED`**, both cite their originating source record, and both
carry an explicit **uncertainty-retained** section because this task did not execute the
tests that would close them.

- **DR-002** grounded in `load_authoritative_anchor()` (`evaluation_gate.py:1285`), the
  one-observation docstring at `:2085–2093`, and public `verify_authoritative_holdout()`
  (`:1482`). *Uncertainty:* whether an existing test already pins one-observation purity
  across operations is `UNKNOWN`.
- **DR-003** grounded in `SCHEMA_VERSION = 2` (`:47`), `is_placeholder()` (`:281–287`),
  `_is_hex_sha256()` (`:202–205`), and the three-path `evaluator_identity_current` gate
  (`:2113–2122`). *Uncertainty:* whether any consumer distinguishes the refusal reasons is
  `UNKNOWN`.

No technical detail was invented beyond what those sources establish.

### Decision register — all six remain PROPOSED

`evidence/GOVERNANCE_DECISIONS_20261009.jsonl`, 6 records, stable IDs `GD-2026-10-09-01…06`:

| ID | Topic | Gate | Options recorded |
|---|---|---|---|
| 01 | holdout-provenance-recovery | G8 | 2 (from source) |
| 02 | policy-identity-mode | G8 | 2 (from source) |
| 03 | denominator-and-exclusion-semantics | G8 | 2 (from source) |
| 04 | configuration-adoption-authority | G8 | **0 — none established by source** |
| 05 | statistical-policy | G8 | **0 — none established by source** |
| 06 | snapshot-and-replay-semantics | G8 | **0 — labels deliberately unimplemented** |

For 04–06 the seed records the **absence** of an option set as
`<no option set established by the source records; defining the options is part of this
decision>` rather than inventing plausible options.

**Every record:** `status=PROPOSED`, `authority_principal=""`, `decided_at=""`.
Verified by `test_committed_seeds_carry_no_authority_identity_anywhere` and
`test_committed_seeds_confer_no_authority_even_after_import`. **No decision was adopted.**

---

## 7. Unresolved questions and explicit authority required

| # | Question | Authority | Why engineering cannot decide it |
|---|---|---|---|
| 1 | Supply the AM-4-R3 task packet, or rule that the AM-4-R2 weld work discharges it | operator + GLM | The packet is not in the repository; its scope is unrecoverable |
| 2 | **G3 ruling** | GLM | Gate acceptance is not an engineering act |
| 3 | Rule on the 78-file relabelling inconsistency (`WELD_SET.md` U-3 vs `F2_PERIMETER_RECORD.md` 001R6) | GLM | Changes a substantive security claim about 78 files; this task had no evidence to decide it and did not |
| 4 | P9 deletion ruling for gated library code (D-1) | GLM + operator | Destructive scope outside this task |
| 5 | Ratify or reject the six PROPOSED decisions | operator | Ratification is operator-owned by definition |
| 6 | Do the published README effect sizes stand, or are they withdrawn? | operator + GLM | Research-claims decision, not engineering |
| 7 | ADR-011 collision (two unrelated documents numbered 011, 68 textual references) | GLM | Renumbering is a wider change than this scope; **left unresolved on purpose** |
| 8 | License / authorized-use posture for the offensive-capability modules | operator | Legal; explicitly out of scope |
| 9 | DR-002 / DR-003 closure conditions | GLM | Each requires a ruling plus a property-pinning test |

---

## 8. Deviations from the authorized scope

**None.** No B1–B4, no C4–C6, no P4/P5/P10 work. No commit, push, merge, sign, ratify, or
release. No full-suite run. No benchmark. No external network. No Docker stack. No external
target contacted. No secret file read.

Two things worth flagging as *additions* rather than deviations, both inside A/C scope:

1. **`scripts/gen_governance_decision_seeds.py`** — a seed file with hand-typed hashes is
   exactly the unverifiable-artifact problem this task exists to reduce, so the seeds are
   generated. It can emit PROPOSED records only; no branch or flag can emit ADOPTED.
2. **A disposable git worktree** was created at `/home/yaser/audit-rsi1/g3-verify-wt` for the
   C2 proof and **removed** afterwards. `git worktree list` was verified restored to its
   original three entries. The pre-existing stale entry `/tmp/rbase-b6ef24` was **not**
   touched.

One self-correction worth recording: an early `git ls-files` invocation used a shell variable
that PowerShell consumed, producing a BEFORE manifest of *all* tracked files (67,641) rather
than the intended protected subset. The AFTER manifest was regenerated at the **identical
all-tracked scope** so the comparison in §5 is valid. Flagging it because a mismatched-scope
before/after comparison would otherwise have looked like "no changes at all".

---

## 9. G3 submission checklist

| Criterion (roadmap §14) | Status | Label | Evidence |
|---|---|---|---|
| §14.1–14.9 weld implementation (gate + deletion at named sites) | recorded per item | `REPORTED` | `WELD_SET.md` status table — **not re-verified by this task** |
| §14.8 static guardrail | present | `IMPLEMENTED` | `src/orchestrator/exec/inv1_guard.py` |
| §14.9 dynamic bypass tests | **47 functions present** | `PROVEN` (count only) | `tests/test_am4_weld_gates.py` |
| §14.9 …executed and passing at this revision | not established | `UNKNOWN` | not run by this task |
| §14.10 native sandbox + safe capability | present | `IMPLEMENTED` | `exec/sandbox.py`, `safe_capability.py` |
| §14.11 MVP demonstration | present | `IMPLEMENTED` | `evidence/p311_mvp/` — records "G3: NOT ACCEPTED" |
| §14.11 eight failure criteria | not established | `UNKNOWN` | requires executing the MVP path |
| §14.12 GLM adversarial review (10 classes) | **NOT PERFORMED** | `PROVEN` (absence) | no GLM ruling artifact exists |
| AM-4-R3 execution record | **ABSENT** | `PROVEN` (absence) | repo-wide search matches only inside the roadmap |
| AM-4-R3 status vs weld records | conflict recorded and referred | `IMPLEMENTED` | ADR-013 |
| Frozen-instrument attribution | `UNVERIFIABLE_DRIFT` recorded | `PROVEN` | drift record §1 |
| Holdout dataset | `UNVERIFIABLE` / `MISSING` | `PROVEN` | `HOLDOUT_CLASSIFICATION_20261009.json` |
| Nested-suite contamination path | **closed and proven** | `PROVEN` | before/after digest equality + negative control |
| Operator decision authority | mechanism exists; 6 decisions PROPOSED | `PROVEN` | 57 tests; seed file |
| **G3 gate acceptance** | **NOT ACCEPTED** | `PROVEN` (absence of ruling) | roadmap Appendix D; `STATUS.md:17,54` |
| P10 admission | 0 of 10 fields | `PROVEN` | unchanged; P10 not entered |

---

## 10. Recommended handoff to GLM

**Submission readiness: NOT ready to submit.** Three blockers must clear first, in order.

1. **Supply or rule on AM-4-R3** (ADR-013 §5). Without the packet, the G3 package's central
   claim cannot be evaluated.
2. **Rule on the 78-file census inconsistency** (ADR-013 §5 item 3). This is a security claim
   about 78 files and it currently reads two ways across two authoritative-looking records.
3. **Decide the README effect-size question** (drift record §5). The package must not be
   reviewed while its headline results carry an unresolved provenance status.

**What GLM receives:** a package in which the contradictions are recorded rather than
papered over, protected evidence is provably intact, the operator-authority mechanism exists
and holds six decisions in `PROPOSED`, the nested-suite contamination path is closed *with a
negative control proving the check works*, and the drift in the frozen evaluation instrument
is documented with reproducible commands — while the pinned anchor remains untouched.

**What GLM should do first on arrival:** perform the §14.12 adversarial review. Ten named
attack classes have never been attempted by anyone; that is the criterion on which the
implementation-shaped evidence cannot help.

**One floor number is still missing.** Six mutually inconsistent suite figures exist across the
corpus (357 / 369 / 552 / 621 / 1218 / 1318). Resolving them to one authoritative figure with
an environment fingerprint is required by AM-8 and was **not** in this task's authorized scope
(it needs a full-suite run).

---

*Ends here. Nothing was committed, signed, ratified, or accepted. G3 remains NOT ACCEPTED;
P4 and P10 remain unauthorized; the P4/RSI freeze notice is ACTIVE.*
