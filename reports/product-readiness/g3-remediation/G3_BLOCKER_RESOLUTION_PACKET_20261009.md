# RAPHAEL — G3 Blocker Resolution and Decision Packet

**NON-AUTHORITATIVE DECISION PACKET.** This is an evidence-and-options document for
the operator and GLM. It accepts nothing, rules on nothing, ratifies nothing, and
promotes nothing. **G3 remains NOT ACCEPTED. P4 and P10 remain unauthorized.**

---

## 1. Repository identity and change-state confirmation

Verified at the start of this task, before relying on any prior conclusion.

| Field | Expected | Actual | Match |
|---|---|---|---|
| Root | `/home/yaser/external-audits/raphael-2` | same | ✅ |
| Branch | `governance/rsi-1-provenance-correction` | same | ✅ |
| HEAD | `fc3e2c132591eab7edaa12e97e13fe2d01619411` | same | ✅ |
| Tree | `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061` | same | ✅ |
| Commit count | — | 188 | — |
| HEAD subject | — | `RSI-1: add evidence-based historical split call-site adjudication package` (2026-10-09 11:15:51 +0000) | — |
| Remotes | 3 | `origin`, `canonical`, `audit-target` | ✅ |
| Worktrees | 3 | primary, `ratification-wt`, stale-prunable `/tmp/rbase-b6ef24` | ✅ |
| Staged changes | 0 | 0 | ✅ |

**Working-tree changes (unchanged from the preceding task):**

| State | Files |
|---|---|
| Modified (tracked) | `README.md`, `evidence/DEFECT_REGISTER.md`, `evidence/phases/P3_0_reinventory/WELD_SET.md` (+193 / −23 lines) |
| Untracked | `RAPHAEL_RSI1_INDEPENDENT_AUDIT_FC3E2C132.md`, `docs/adr/ADR-013-…md`, `evidence/GOVERNANCE_DECISIONS_20261009.jsonl`, `evidence/frozen_instrument_drift/`, `evidence/governance/`, `reports/product-readiness/`, `scripts/gen_governance_decision_seeds.py`, `src/arena/tests/conftest.py`, `src/orchestrator/rsi/governance_registry.py`, `tests/test_rsi1_governance_registry{,_adversarial}.py` |

**No divergence.** Nothing was reset, cleaned, switched, or altered. This task performed
no writes except the two deliverables named in §8.

**Canonical roadmap:** `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` (133,930 bytes, v4.2). No v5
roadmap exists. No ADR other than the prior task's untracked ADR-013 addresses AM-4-R3 or
G3 acceptance.

---

## 2. Scope and permissions

**Read-only investigation and decision preparation.** Permitted and used: reading files,
git history, local objects, branch/tag/worktree metadata, prior reports, test definitions,
configuration, prior transcripts.

Not performed: source/test/policy/roadmap/gate-record modification; any B1–B4 or C4–C6
implementation; P4/P5/P10 work; any adoption, ratification, rejection or supersession of a
decision; any operator identity/signature/attestation/date; any test execution; any full
suite or nested Arena suite run; any external target, offensive action, Docker start, secret
read, or network fetch; any commit, push, merge, sign, release, promotion.

**Sequence followed:** evidence collection → discrepancy analysis → decision options →
authority review → *(implementation authorization and gate ruling are explicitly NOT
reached — they require the named authority).*

---

## 3. Source-of-truth register with precedence

Precedence verbatim from roadmap **Appendix E**:

```
1. Explicit superseding ADR / governance ruling
2. RAPHAEL MASTER ROADMAP v4.2 — this document
3. v4.1 AM-1…AM-14 inheritance summarized in §0.2
4. Earlier v4 roadmap wording
5. Historical audit reports / repository comments
6. Individual model suggestions
```

| ID | Path | Rev / date | Level | Status used here |
|---|---|---|---|---|
| S1 | `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` | added `69004a231`, 2026-10-07; unchanged since | **2** | Authoritative |
| S2 | `docs/adr/ADR-001…ADR-013` | ADR-013 untracked (prior task) | 1 | **None adopted**; ADR-011 duplicated |
| S3 | `docs/adr/ADR-005-legacy-migration-seam.md` | AM-4.1–AM-4.5 clause semantics | 1 | Authoritative on what "welded" means |
| S4 | `evidence/g3_remediation/STATUS.md` | `07fad8c1`, 2026-09-07 | 5 | G3 NOT ACCEPTED |
| S5 | `evidence/phases/P3_0/EVIDENCE.md` | G2 record | 5 | G2 PASS (cites GLM G3 entry adjudication) |
| S6 | `evidence/phases/P3_0_reinventory/CENSUS.md` | last touched `69004a231`, 2026-10-07 | 5 | **Newest census artifact** |
| S7 | `evidence/g3_remediation/F2_PERIMETER_RECORD.md` | last touched `e6a8c707e`, 2026-09-29 | 5 | Perimeter record 001R6 |
| S8 | `evidence/phases/P3_0_reinventory/WELD_SET.md` | modified (uncommitted, prior task) | 5 | Weld claims; U-3 |
| S9 | `evidence/p311_mvp/P311_EVIDENCE.md` | `19121d7da`, 2026-09-07 | 5 | §14.10–§14.12 evidence |
| S10 | `evaluations/campaign/FINAL_VERDICT_RECORD.md` | 2026-08-08, SENTINEL GLM-5.2 | 5 | **Project-frozen INCONCLUSIVE** |
| S11 | `evaluations/campaign/rbs_v4_reproducibility_manifest.json` | pinned anchor | 5 | Digest-pinned; drifted internally |
| S12 | `evidence/frozen_instrument_drift/UNVERIFIABLE_DRIFT_20261009.*` | prior task | 5 | `UNVERIFIABLE_DRIFT` |
| S13 | `evidence/GOVERNANCE_DECISIONS_20261009.jsonl` | prior task | 5 | 6 records, all PROPOSED |
| S14 | `evidence/governance/P4_RSI_FREEZE_NOTICE_20261009.md` | prior task | 5 | Freeze ACTIVE |

---

## 4. Q1 — AM-4-R3 provenance and status

### 4.1 Chronology

| Date | SHA | Event | Evidence |
|---|---|---|---|
| (pre) | `7272880f7e…` | P0 baseline; 17 SUB sites inventoried | `P0_DIFF.md:3-6` |
| 2026-09-07 17:11 | `ee9497289` | G3 remediation: F1 fix + **F2 perimeter record** + Scope evidence | `git log -- evidence/g3_remediation` |
| 2026-09-07 17:14 | `768285b33`→`cf0da0e6e`→`07fad8c1d`→`5630cd215` | K.0 provenance block; STATUS at `07fad8c1` — **G3 NOT ACCEPTED** | `evidence/g3_remediation/STATUS.md:17,54` |
| 2026-09-07 17:47 | `19121d7da` | **P3.11 §14.10 MVP evidence package** (385 floor, §14.11 8/8, §14.12 13/13) | `evidence/p311_mvp/P311_EVIDENCE.md` |
| 2026-09-16 16:08 | `3b2e22db3` | **P3.0 re-inventory (AM-1)** — 150-file census, W-01…W-15 welds, AM-4-R2 deletions | `WELD_SET.md`, `CENSUS.md` |
| 2026-09-19 | (content date) | Roadmap v4.2 authored; state block: `AM-4-R3: NOT EXECUTED`, `G3: BLOCKED` | roadmap:25, 4657 |
| 2026-09-29 19:19 | `e6a8c707e` | P0 snapshot before offensive restoration | `git log` |
| **2026-10-07 13:48** | **`69004a231`** | **Roadmap file ADDED** (321 files, +89,523/−135) | `git log --diff-filter=A` |
| 2026-10-09 11:15 | `fc3e2c132` | RSI-1 adjudication package — current HEAD | `git log -1` |

**Material observation:** the canonical roadmap entered the repository in `69004a231`, a
321-file bulk import whose subject line ("harden measurement authority and holdout gating")
describes only a fraction of what it did. Commit subjects are therefore **not** a reliable
index for this repository, and the roadmap's own 2026-09-19 state block post-dates the weld
work it declares outstanding.

### 4.2 Required vs discovered

| Required deliverable | Discovered evidence | Strength | Missing proof |
|---|---|---|---|
| AM-4-R3 **task packet** (scope, acceptance criteria) | None in repository. Roadmap asserts `AM-4-R3 prompt: EXISTS` (line 3627) but no artifact carries it | `NO_EXECUTION_EVIDENCE_FOUND` for the packet | The packet itself — operator-held or lost |
| AM-4-R3 execution record | **Zero.** No commit in any ref mentions `AM-4-R3` in subject or body (`git log --all --grep`); the only pickaxe hit is the roadmap file itself | `PROVEN` absence | Any artifact naming AM-4-R3 as executed |
| AM-4-R3 independent audit | None | `PROVEN` absence | — |
| **AM-4-R2** welds (W-01…W-15) + branch deletions | **Code-verified.** e.g. `chains/tool_registry.py:57-93` gates then unconditionally `raise WeldNotAuthorized`, primitive gone; `agent/agent.py:97-102,115-120` exec/uninstall branches deleted; `sandbox/__init__.py:34-46` | `PROVEN` (code read) | Independent verification of the *whole* set |
| AM-4-R2 evidence trail | 30+ tracked references across `CENSUS.md`, `WELD_SET.md`, `probe_reinventory.py`, `raw/probe_reinventory.txt` (`PASS` lines), source comments | `PROVEN` | — |

### 4.3 Two numbering systems — and the mapping nobody recorded

| System | Range | Source | Meaning |
|---|---|---|---|
| AM-4 clauses | AM-4.1 … AM-4.5 | `ADR-005:22-45` | Positive interface / weld semantics / G3 exit / rollback / deletion |
| AM-4 remediation revisions | AM-4-R2, AM-4-R3 | roadmap:3501, 3622 | Execution packets governed by the v4.1 arbitration |
| Executor task IDs | Task 001, 001R2…001R6, 002 | `EFFECT_SCOPE_RULING_REQUEST.md:3`, `WELD_SET.md:181`, `P0_DIFF.md:61` | P3.0 re-inventory work series, executor "Muse Spark 1.3" |

`AM-4-R3` is **not** `AM-4.3`. Nothing in the repository maps Task 001R* onto AM-4-R3.
Establishing such a mapping would be an authority act, not an inference.

### 4.4 A substantive nuance GLM should see

The deletion-class welds are **gate-then-unconditional-raise**, not gate-then-route:
14 `raise WeldNotAuthorized` sites across 11 files (`agent/agent.py`,
`cloak-service/main.py`, `kali-tools/server.py`, `mhddos-service/main.py`,
`orchestrator/auth.py`, `c2/beacon.py`, `c2/implant_builder.py`, `c2/sliver_backend.py`,
`chains/tool_registry.py`, `kali_tools_client.py`, `sandbox/__init__.py`).

So on those paths the Broker decision does not determine the outcome — the outcome is always
deny. That **satisfies** ADR-005 AM-4.2 ("the legacy branch at that call site is deleted"),
but `WELD_SET.md:41-45`'s phrasing "the gate is not blanket-deny" could be read as implying
the Broker's verdict matters. It does not, on these 14 sites. `[PROVEN]` for the pattern,
`INFERRED` for the wording-collision risk.

### 4.5 Q1 conclusion

> ## `NO_EXECUTION_EVIDENCE_FOUND`
>
> For **AM-4-R3 specifically**. Absence is proven, not inferred: no commit message in any
> ref, no evidence file, no ADR, no test, no branch name.

> **AM-4-R2** is a separate matter and is **strongly evidenced** — the work exists in code
> and in a trail of census rows, probe transcripts and source comments.

The two must not be conflated, and this packet does not conflate them. The prior task's
ADR-013 correctly retained `NOT EXECUTED`; nothing found here changes that.

**Minimum missing artifact:** the AM-4-R3 packet. **Minimum ruling:** whether AM-4-R2's
verified weld/deletion work discharges the AM-4-R3 obligation — answerable only once the
packet's scope is known.

---

## 5. Q2 — The 78-file census inconsistency

### 5.1 The conflicting claims, verbatim

**`F2_PERIMETER_RECORD.md:82`** (record 001R2, 140-file census):
> "Census (001R2): 140 files — 68 not-yet-mediated files · 6 mediated · 5 reachable notes · 61 dead."

**`F2_PERIMETER_RECORD.md:49`** (record 001R6):
> "(001R6 supersedes: census 149 → 150, WELD_SET §U-3 → 150 · 78/6/4/62.)"

**`WELD_SET.md:193-196`** (U-3):
> "U-3 RESOLVED (CENSUS.md): full 150-file effect census reconciled (78 welded files · 6 mediated · 4 reachable notes · 62 dead). … (AM-4 note: the 78 formerly not-yet files now read `Pxx welded`.)"

### 5.2 Reconciliation — this resolves the blocker

> **Q2 conclusion: `NO_CONFLICT_EXISTS`** (JSON: `Q2_census_reconciliation.conclusion`)

Two counts were being compared that describe **different censuses at different revisions**:

| Record | Census size | Arithmetic | Total |
|---|---|---|---|
| 001R2 | **140** files | 68 + 6 + 5 + 61 | 140 ✅ |
| 001R6 | **150** files | 78 + 6 + 4 + 62 | 150 ✅ |
| U-3 | **150** files | 78 + 6 + 4 + 62 | 150 ✅ |

**001R6 and U-3 agree exactly.** The apparent conflict came from reading the *001R2*
paragraph ("68 not-yet-mediated") as if it described the 150-file census. It does not.

**Empirical confirmation against `CENSUS.md` at HEAD** — 150 numbered rows, final-column
tally:

| Final classification | Rows |
|---|---|
| `… welded` | **78** (P23×31, P07×12, P06×6, P20×5, P19×4, P16×4, P11×4, P27×3, P18×3, P12, P10, P09, P05, P04, P04-shared) |
| `… mediated` | **6** (P13×4, P01×2) |
| `… note` | **4** (P17×3, P18×1) |
| `… dead` | **62** (P24×60, P25×1, P14×1) |
| **Total** | **150** ✅ |

`git grep` finds **zero** live `not-yet` labels in `CENSUS.md`; the only two occurrences
(lines 18, 203) are historical narrative ("former not-yet rows now read `Pxx welded`").

### 5.3 Timing explains why it looked contradictory

`CENSUS.md` was last touched by `69004a231` (**2026-10-07**); `F2_PERIMETER_RECORD.md` by
`e6a8c707e` (**2026-09-29**). The census is the **newer** artifact and post-dates the weld
relabelling, so the "welded" reading is the current one. `[PROVEN]`

> ### ⚠️ Correction to the previous two reports
> The prior remediation report recorded this as an open "78-file relabelling inconsistency"
> and deliberately did not resolve it. On the evidence above, **there is no inconsistency to
> resolve**: the numbers were never in conflict, and the census itself settles the
> classification. That prior caution was defensible from the two records alone, but the
> blocker as stated was a **revision/scope misreading** and should not be carried into a G3
> submission.

### 5.4 What remains genuinely open (and is not a bookkeeping problem)

`welded` in `CENSUS.md` is a **recorded label**, not an independently verified security
property. Nothing in the repository demonstrates that all 78 files are genuinely
Broker-mediated at runtime. That is precisely what roadmap §14.12 exists to test, and it has
not been attempted by the authority (§7).

**Security implications of each interpretation:**

| Reading | Implication |
|---|---|
| 78 welded (current, evidenced) | Largest legacy surface is Broker-gated. Residual risk concentrates in the **62 "dead"** rows — deadness partly established by *import failure* (`DEFECT_REGISTER.md` DR-001: `sword.phase_2_exploit` fails to import, "1 of the 19 remaining fresh-process import failures"). Repairing an import could resurrect an unmediated primitive. |
| 78 not-yet-mediated | 78 files with live primitives outside the Broker — materially worse, and would block G3 outright. |

**Question for GLM:** *"Do you accept `CENSUS.md` (150 rows: 78 welded / 6 mediated / 4 notes
/ 62 dead) as the authoritative current classification, and do you accept 'dead-by-import-
failure' as equivalent to deleted for perimeter purposes?"* The first is now evidenced; the
second is a judgement only GLM can make.

---

## 6. Q3 — Published evaluation-effect-size decision brief

### 6.1 Trace of published claims

| Published claim | Location | Declared dataset | Declared instrument | Verifiable now? |
|---|---|---|---|---|
| "1,200-run holdout evaluation across 5 scenario families × 4 arms × 60 seeds" | `README.md:118-119` | `rbs_v4_holdout.jsonl` | frozen v2.1.1 | **No** — file absent from tree and git; `.gitignore:87` |
| `FULL vs NO_WORLD_MODEL Δ=+0.149, d=+0.773, p=3.16e-30` | `README.md` Key Results | same | same | **No** — depends on the same missing dataset |
| `FULL vs NO_PLANNER Δ=+0.090, d=+0.547` | same | same | same | **No** |
| `FULL vs NO_STUDENT Δ=+0.021 (boost confound)` | same | same | same | **No** |
| `FULL vs NO_FALSIFICATION — Single-template (T10)` | same | same | same | **No** |
| `FULL vs PROMPTED_AGENT 0/300 pass (structural)` | same | same | same | **No** |
| `FULL vs SCRIPTED_BASELINE Δ=+0.347 (defect disclosure)` | same | same | same | **No** |
| `Δ=0.3287, McNemar p=4.48e-44` | `FINAL_VERDICT_RECORD.md:51` | same | same | **No** |
| Manifest declares `total_rows_expected: 3240`, `seeds 1072-1101` | `rbs_v4_reproducibility_manifest.json:47-53` | Campaign A | — | Internally inconsistent with its own `dataset` block (Campaign B, 1200 rows) |
| Manifest integrity gate PASS `3240/3240` | `rbs_v4_holdout_integrity_gate.json:5-7` | Campaign A | commit `74e52edd` (absent) | **No** — certifies a dataset the manifest does not declare |

**Instrument status:** `UNVERIFIABLE_DRIFT` — declared commit and tag absent, 5 of 9 pinned
digests mismatch including the canonical PDP (prior task, reproduced; see S12).

**Pinned anchor status:** **intact** — manifest still hashes to
`c26ed773ba57…`, matching `AUTHORITATIVE_ANCHORS` (`evaluation_gate.py:174-178`).

### 6.2 A second, independent problem the drift analysis did not surface

`FINAL_VERDICT_RECORD.md` (2026-08-08, Authority: **SENTINEL GLM-5.2**) is the project's own
terminal verdict:

- **Status: "PROJECT FROZEN — INCONCLUSIVE"**
- **Not Supported:** "Raphael is superior to strong prompting"; "Architecture is necessary."
- **"No terminal superiority claim may be published or acted upon."**
- Disposition: "Frozen as inconclusive … an honest, frozen research artifact."
- It states it tagged the repository `raphael-terminal-freeze-inconclusive`.

**That tag does not exist locally.** `git tag -l` returns only `raphael-orphan-phase12-preserved`,
`raphael-p0-baseline-7272880f`, `raphael-p1-post-migration-7272880f`,
`raphael-p1-pre-migration-7272880f`, `raphael-p14.5-baseline`. `[PROVEN]` absent locally;
whether it exists on a remote is `UNKNOWN` (no fetch performed).

So the effect-size question has **two independent axes** that are routinely conflated:

| Axis | Question | Current state |
|---|---|---|
| **Provenance** | Can the numbers be verified? | **No** — dataset UNVERIFIABLE, instrument UNVERIFIABLE_DRIFT |
| **Interpretation** | May the numbers be published/acted on? | **Restricted by the project's own verdict** for the central thesis; internal ablations fall under "Supported" *as recorded* |

The README already carries the interpretation caveat — *"Central thesis … remains
**UNRESOLVED** due to instrument defects"* (`README.md:204`) — and the prior task added the
provenance banner. What is missing is **an authority decision**, not documentation.

### 6.3 The five questions, answered separately

1. **What is historically recorded?** Effect sizes above, as published 2026-10-04, plus a
   SENTINEL verdict of frozen-inconclusive with publication restricted.
2. **What source data and instrument can presently be verified?** Neither. Dataset absent
   from tree and history; instrument drifted and its commit unrecoverable.
3. **Which claims remain reproducible?** None of the listed effect sizes. Reproducing them
   would require re-running the campaign, which would produce **new** results, not a
   reproduction.
4. **Which are currently unverifiable?** All seven rows.
5. **Consequences of each option** — see below.

### 6.4 Decision options (presented, not selected)

| # | Option | Advantages | Risks | Evidence required | Impact | Reversible? | Authority |
|---|---|---|---|---|---|---|---|
| **A** | Retain figures, caveats strengthened | Preserves research record; no deletion of history; matches current README state | Unverifiable numbers remain quotable; may be read as validated | None beyond current | Low | Yes | operator + GLM |
| **B** | Retain figures **and** formally downgrade to "historical, unverifiable" with a standing machine-readable marker | Keeps record while making status machine-checkable; prevents silent re-quotation | Requires a new marker artifact; marker itself becomes governance surface | A classification record analogous to `HOLDOUT_CLASSIFICATION_20261009.json` | Medium | Yes | operator |
| **C** | Withdraw the effect sizes from all user-facing surfaces; retain internally with provenance header | Cleanest separation of claim from evidence; cannot be misread | Loses visible research record; may be read as admitting falsity, which the evidence does **not** establish | Same as B | High (README, `RESEARCH_ASSIGNMENT_001_REPORT.md`) | Yes, but visible | operator + GLM |
| **D** | Authorize provenance recovery from outside the repository, then re-decide | Only path that could restore verifiability | Recovery may fail; costs time; partial recovery is a new evidence problem | Operator authorization + external access | Medium | n/a | operator |
| **E** | Re-establish later via a fresh, fully-bound campaign under a new measurement contract | Clean provenance going forward | Does not repair historical claims; large cost; requires G8 preconditions that are themselves blocked | Full P8/G8 chain | High | n/a | operator + GLM, after G8 |

**Not an option:** recalculating effects, rerunning the campaign to regenerate the missing
file, manufacturing substitute values, or editing the pinned anchor. All are prohibited.

### 6.5 The decision record that applies — **there is none**

The six existing PROPOSED records are: `GD-2026-10-09-01` holdout-provenance-recovery,
`-02` policy-identity-mode, `-03` denominator-and-exclusion-semantics, `-04`
configuration-adoption-authority, `-05` statistical-policy, `-06`
snapshot-and-replay-semantics.

**None covers "do the published effect-size claims stand, be caveated, or be withdrawn?"**

> **Gap reported, not filled.** `GD-01` is adjacent (whether the *dataset* may be recovered
> or is permanently unverifiable) but is a different question: it does not address
> publication of already-published figures. A new decision record would be required. Creating
> a PROPOSED record is an engineering act; **adopting** it is not, and this task does
> neither.

---

## 7. Q4 — Authoritative test floor and safe validation plan

### 7.1 There are **seven** reported figures, not six

| # | Figure | Source:line | Revision claimed | Distance to HEAD | Interpreter | In declared range? | Transcript |
|---|---|---|---|---|---|---|---|
| 1 | **357** | `RAPHAEL_STATE.md:10` | none | — | none recorded | — | **No** `[REPORTED]` |
| 2 | **369** | `evidence/g3_remediation/STATUS.md:23` | `07fad8c1` | **39 commits** | 3.14.4 (`environment.txt`) | **No** | **Yes** — `floor_transcript_final.txt`: `369 passed, 32 warnings in 21.09s` |
| 3 | **385** | `evidence/p311_mvp/P311_EVIDENCE.md:88` | `fc83a6179` | **37 commits** | 3.14.4 (`p311_environment.txt`) | **No** | **Yes** + clean-checkout corroboration: `385 passed, 33 warnings in 11.99s` / `14.03s` |
| 4 | **552** | `F2_PERIMETER_RECORD.md:31` | 001R6 era | ~35 | none recorded | — | **No** `[REPORTED]` |
| 5 | **621** | `REVIEWER_GUIDE.md:28` | none | — | 3.14.4 (stated) | **No** — the file itself says the pin "is NOT satisfiable" | **No** `[REPORTED]` |
| 6 | **1218** | `reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md:22,110,122,374` | `c1eab3dd2` era | — | 3.12.15 (§0 line 9) | **Yes** | **No** `[REPORTED]` |
| 7 | **1318** | `evidence/phase3_readiness/REMEDIATION_MANIFEST.json:13` | `1fd7cda76`, tree `49237b06` — **`git rev-parse` matches** `[PROVEN]` | **8 commits** | 3.12.15, pytest 9.1.1 | **Yes** | **Yes** — `full_suite_output.txt`: `1318 passed, 44 warnings in 103.38s` |

**Findings:**

- **No figure describes HEAD (`fc3e2c132`).** The nearest transcript-backed figure on a
  declared-supported interpreter is 1318, **8 commits behind**. `[PROVEN]`
- The two figures with the strongest evidence (369, 1318) disagree on interpreter, revision
  and duration. They are not alternatives for the same thing.
- Three of four transcript-backed runs used **Python 3.14.4, outside the declared
  `>=3.11,<3.13`**. `REVIEWER_GUIDE.md:28-31` states this openly.
- The 1318 transcript contains a **CUDA driver mismatch** warning ("driver … too old (found
  version 12080)") — torch fell back during that run. Environment fidelity is therefore
  imperfect even in the best-evidenced figure. `[PROVEN]` from the transcript text.
- A prior task collected **1509 tests** at HEAD-with-uncommitted-changes. That is a
  **collection** count, not a pass count, includes 57 tests from two then-untracked files,
  and is not comparable to any figure above. `[REPORTED]` (not reproduced this task — no
  tests were run).

**Per the instruction, no averaging, no choosing the largest, no privileging the newest.**

### 7.2 Validation protocol — requires separate operator authorization

**Nothing below was executed. This is an execution-ready protocol.**

**Baseline to validate**
- Commit `fc3e2c132591eab7edaa12e97e13fe2d01619411`, tree `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061`.
- Decide explicitly whether the run includes the prior task's uncommitted files (ADR-013,
  registry, tests, README/WELD_SET/DEFECT_REGISTER edits). **Recommendation:** first commit
  or shelve them so the floor is unambiguous — otherwise the count silently includes 57
  tests that are not in the baseline tree. This is an operator decision.

**Interpreter**
- Must satisfy `pyproject.toml` `requires-python = ">=3.11,<3.13"`. Use **3.12.x** (the
  version already shown to run the suite: `.venv` = 3.12.15).
- Record the incompatible-interpreter problem explicitly in the report — it is the reason no
  existing figure is authoritative.

**Environment fingerprint (all recorded, none assumed)**
- `python -VV`; interpreter executable SHA-256
- `python -m pip freeze` **plus lockfile state** — there is currently **no lockfile**
  (`poetry.lock`/`uv.lock`/`constraints.txt` all absent), so `pip freeze` is the only
  inventory available and is itself a reproducibility gap
- `uname -a`, CPU model/count, RAM, GPU + driver version (the CUDA warning must be captured,
  not ignored)
- `git rev-parse HEAD HEAD^{tree}`, `git status --porcelain` (must be clean or fully enumerated)
- `.env` **variable names only** — never values

**Commands and inclusion policy**
```bash
# Phase 0 — isolation proof BEFORE anything runs
git ls-files > /tmp/tracked.txt
xargs -a /tmp/tracked.txt -d '\n' sha256sum > BEFORE.sha256

# Phase 1 — collection only (distinct from execution)
PYTHONPATH=src python -m pytest tests/ --collect-only -q

# Phase 2 — the configured suite
PYTHONPATH=src python -m pytest tests/ -q --no-header

# Phase 3 — guardrails
PYTHONPATH=src python -m pytest tests/test_p2_guardrail_*.py -q --no-header

# Phase 4 — post-run integrity
xargs -a /tmp/tracked.txt -d '\n' sha256sum > AFTER.sha256
diff <(sort BEFORE.sha256) <(sort AFTER.sha256)
```
- **Inclusion policy:** `tests/` only. `testpaths = ["tests"]` in `pyproject.toml` already
  excludes `src/arena/tests` — state this explicitly so the exclusion is a decision, not an
  accident. `src/arena/tests` is **out of scope** for this floor (see §7.4).
- Record five **separate** fields: collected / passed / failed / skipped / errors, plus
  warnings and duration. Never a single blended number.

**Capture requirements** — every invocation records: exact command line, working directory,
exit code, UTC start/end timestamps, full stdout and stderr to file, host and interpreter
fingerprint. Exit code is mandatory; a transcript without it is not a result.

**Independent verification**
- A second party re-runs the fingerprint commands and confirms `BEFORE.sha256` /
  `AFTER.sha256` match the submitted manifest byte-for-byte.
- A second party re-derives `git rev-parse HEAD^{tree}` and confirms the declared tree.
- **AM-6 discipline:** if any retained test must be weakened, skipped or xfailed, that is
  evidence tampering and an automatic gate failure — not a fix.

**Protected evidence**
Must be hash-verified before and after, covering **all four** trees named in the brief
plus the rest of the tracked tree:
`arena/results/`, `src/arena/results/`, `src/arena/arena/results/`, `evidence/`.
Recommendation: extend to **all 67,641 tracked files**, as the prior task did — that produced
a before/after delta of exactly 3 intentionally-changed files and is the strongest available
form.

**Nested Arena suite isolation**
- Must run in a **disposable worktree** (`git worktree add --detach`), never the primary
  worktree.
- Copy the safeguard in, hash before/after, then `git worktree remove` and verify
  `git worktree list` is restored.
- The prior task's four legacy failures are `REPORTED`, not fixed. A nested-suite run is a
  **separate authorization** and must not be folded into the floor run.

**Rollback / stop conditions**
Stop and report, do not continue, if: any tracked file changes unexpectedly; the working
tree is not clean or fully enumerated; the interpreter is outside `>=3.11,<3.13`; the
exit code is non-zero **and** the failure is environmental (import error, GPU, network) —
record it as environment, not as a test result; or elapsed time exceeds a pre-declared
budget. Never "fix" a failure by editing a test.

**Recording failures honestly**
Warnings are recorded verbatim, including the pre-existing `SyntaxWarning: "\-"` at
`src/orchestrator/capabilities/interactive_shell/capability.py:141` that appears in three
transcripts. Environmental problems are labelled separately from assertion failures. No
output file is edited after capture; corrections are new files with new names.

**Criteria for designating one authoritative floor**
A figure may be declared authoritative only if **all** hold:
1. transcript exists with exit code and timestamps;
2. bound to a specific commit **and** tree SHA, verified with `git rev-parse`;
3. interpreter satisfies the declared range;
4. full environment fingerprint captured;
5. collected/passed/failed/skipped/errors reported as distinct fields;
6. `BEFORE.sha256` ≡ `AFTER.sha256` across all protected trees;
7. describes the **current** baseline tree, or names its delta explicitly;
8. independently re-verified per §7.2 "Independent verification".

On today's evidence **no figure meets 1-8**; the closest is 1318 (fails 7, and its transcript
carries the CUDA warning).

### 7.3 Review of the nested-suite fingerprint safeguard — and its limits

`src/arena/tests/conftest.py` (added by the prior task, **not modified here**) uses two
layers: an autouse fixture redirecting `arena.ablation_runner.RESULTS_BASE` to `tmp_path`,
and a session-scoped guard fingerprinting four protected trees with `(size, mtime_ns)` per
file and failing the session on any difference. That guard was demonstrated to *detect* a
planted write in a disposable worktree (test passed, session errored, exact path named).

> ### Can `(size, mtime_ns)` substitute for content hashes as the required integrity proof?
>
> **No.** It is an adequate fast in-suite tripwire. It is **not** an integrity proof.
>
> **Evasion (false negatives):**
> - Any write that restores the original `mtime_ns` (via `os.utime`, `shutil.copy2`,
>   `rsync -t`, `cp -p`, a VCS checkout, or a backup tool) is **invisible**. Content is
>   fully attacker- or accident-controllable in this case.
> - A same-size rewrite that the filesystem happens to leave with an unchanged coarse
>   timestamp can evade detection on filesystems with coarse `mtime` granularity.
> - A file replaced with different content of identical size within the same nanosecond
>   tick would evade.
> - The guard compares **before/after within one session**. A modification made before the
>   session starts (or between sessions) is by definition not detected.
>
> **False positives:** an unrelated backup, sync, or `git` operation touching `mtime`
> fails the session even when content is byte-identical — noise that trains reviewers to
> ignore the guard.
>
> **Coverage gap:** it guards only `arena/results`, `src/arena/results`,
> `src/arena/arena/results`, `evidence`. It does **not** guard `evaluations/`, `failures/`,
> `baseline/`, `Report_Raphael/`, `policies/`, `configs/`, or the rest of the tracked tree.
>
> **Therefore:** the authoritative integrity artifact must remain an **external SHA-256
> manifest** taken before and after, as §7.2 specifies. The conftest guard is a
> defence-in-depth tripwire and must be labelled as such, never cited as the integrity proof.
> `[PROVEN]` for the implementation's stated behaviour; `[INFERRED]` for the evasion
> properties, which follow from filesystem semantics and were not exploited here.

---

## 8. Additional G3 submission blockers

| # | Item | Newer evidence resolves it? | Blocks G3 submission? | Roadmap basis | Label |
|---|---|---|---|---|---|
| 1 | §14.12 ten attack classes — no recorded GLM adversarial review | **Partially.** Automated probes exist: `tests/test_p311_adversarial_probes.py`, 13 tests mapped to the 10 categories (`P311_EVIDENCE.md:63-81`), transcript `p311_targeted_transcript.txt` "13/13 probes green". **The authority review has not occurred** | **Yes** | §14.12: "G3 passes only when these attempts fail according to policy and leave traceable evidence" — GLM "must actively attempt" | probes `IMPLEMENTED`; review `PROVEN` absent |
| 2 | §14.11 eight MVP failure criteria | **More than previously reported.** `P311_EVIDENCE.md:55-61` maps all 8 to named tests, "8/8 PROVEN", criterion 5 via clean worktree | **Yes**, but only the acceptance step | §14.11 | `REPORTED` (transcript-backed) |
| 3 | Pinned instrument unavailable / drifted | No — unchanged. `UNVERIFIABLE_DRIFT` stands; anchor intact | **Yes** for provenance criterion | G4 provenance; §14 evidence chain | `PROVEN` |
| 4 | Holdout dataset missing / unverifiable | No — unchanged. `HOLDOUT_CLASSIFICATION_20261009.json`: `UNVERIFIABLE`, `MISSING` | **Yes** | §14.11/§14.12 evidence; G8 | `PROVEN` |
| 5 | Six governance decisions PROPOSED | No — all six still `PROPOSED`, 0 authoritative | **No** for G3 submission; **Yes** for G4/G8 | G4 ledger criterion | `PROVEN` |
| 6 | ADR-011 duplicated | No — still two files numbered ADR-011; ADR-013 taken next | **No** — deferrable, but GLM should resolve before relying on ADR-011 citations | Precedence level 1 integrity | `PROVEN` |
| 7 | License / authorized-use posture | No — no LICENSE, no `license` field | **No** for G3 (architecture gate); **Yes** before any distribution | Outside roadmap G3 scope | `PROVEN` |
| 8 | P4/RSI freeze notice ACTIVE | Yes — present and correct | **Yes** while active; lifts only on a G3 ruling | Roadmap §36, §37, Appendix D | `IMPLEMENTED` |

> ### ⚠️ Second correction to the previous report
> The prior remediation report recorded §14.11 as "not established / requires executing the
> MVP path" and §14.12 as "NOT PERFORMED". Both understated the evidence.
> `evidence/p311_mvp/P311_EVIDENCE.md` provides named-test mappings, transcript-backed results
> for all eight §14.11 criteria and thirteen §14.12 probes, and clean-checkout reproduction.
> What is missing is the **GLM ruling that converts PROVEN into ACCEPTED** — which is a
> different gap from "no evidence exists", and a materially smaller one.

**G0/G1/G2 status.** `G0 PASS (historical)` and `G1 PASS (historical)` are asserted only at
`evidence/g3_remediation/STATUS.md:51-52` with no cited ruling artifact. `G2 PASS` is
recorded at `evidence/phases/P3_0/EVIDENCE.md:16` citing "the GLM G3 entry adjudication" —
a named authority, no artifact. A repository-wide search for a G3 acceptance artifact
returns only `F2_PERIMETER_RECORD.md`, where the phrase occurs in a **negation**
("Nothing in this record claims AM-4 weld completion, G3 PASS, or production readiness").
**No acceptance artifact for G3 exists.** `[PROVEN]`

---

## 9. Decision table

| ID | Exact question | Available options (from source records) | Evidence | Authority | Next required action |
|---|---|---|---|---|---|
| **D-1** | What did AM-4-R3 require, and does the verified AM-4-R2 work discharge it? | (a) supply the packet; (b) rule that R2 discharges R3; (c) rule it does not and issue R3 | Zero R3 artifacts; R2 code-verified (§4.2) | **operator** (packet) + **GLM** (ruling) | Operator produces the packet; GLM rules |
| **D-2** | Is `CENSUS.md` (78/6/4/62) the authoritative current classification? | (a) accept; (b) order re-derivation | Empirically verified this task (§5.2) | **GLM** | GLM accepts or orders re-derivation |
| **D-3** | Is "dead-by-import-failure" equivalent to deleted for perimeter purposes? | (a) yes; (b) no — require zero-import proof for P9 | DR-001 documents 19 import failures | **GLM** | GLM rules |
| **D-4** | Do the published effect-size claims stand, get caveated, or get withdrawn? | A–E in §6.4 | Provenance + SENTINEL verdict both unfavourable (§6.1, §6.2) | **operator** + **GLM** | Create a decision record; ratify through the registry |
| **D-5** | Does the missing `raphael-terminal-freeze-inconclusive` tag need recreating? | (a) recreate locally; (b) leave absent and annotate | Tag absent locally `[PROVEN]`; remote unknown | **operator** | Operator decides (history rewrite risk) |
| **D-6** | Which single figure is the authoritative floor? | None currently qualify; protocol §7.2 must be run first | Seven figures; none describes HEAD (§7.1) | **operator** (authorize run) | Authorize the §7.2 run |
| **D-7** | Should the floor run include the prior task's uncommitted files? | (a) commit/shelve first; (b) run as-is and document | 57 tests untracked | **operator** | Decide before any run |
| **D-8** | Ratify or reject the six PROPOSED decisions | Each has 0–2 recorded options | `GOVERNANCE_DECISIONS_20261009.jsonl` | **operator** | Ratify through the registry |
| **D-9** | Resolve the ADR-011 numbering collision | (a) renumber + update 68 refs; (b) accept ambiguity and document | 68 textual references | **GLM** | GLM decides |
| **D-10** | Is a G3 ruling issued? | n/a until D-1, D-2, D-3, D-6 close | No acceptance artifact exists | **GLM** | After the above |

---

## 10. Proposed action order and dependency graph

```text
D-7 (commit-or-shelve prior work) ──┐
                                   ├──> D-6 (floor run, §7.2) ──> FLOOR
operator: produce AM-4-R3 packet ──┤
                     GLM: D-2 census ──┤
                     GLM: D-3 deadness ─┼──> D-1 (AM-4-R3 ruling) ──> G3 PACKAGE
operator+GLM: D-4 effect sizes ─────┤                                    │
operator+GLM: D-5 tag ─────────────┤                                    v
GLM: D-9 ADR-011 ──────────────────┘                          §14.12 GLM ADVERSARIAL REVIEW
                                                                            │
                                                                            v
                                                                     D-10 G3 RULING
```

**Critical path:** D-7 → D-6 → FLOOR, and operator packet → D-1. These are independent and
can run in parallel. D-2 and D-3 are cheap GLM rulings that can be issued immediately and
should not wait for anything.

---

## 11. Missing inputs and authority requests

**Artifacts that must be supplied (cannot be produced by investigation):**

| Missing | Who holds it | Consequence if unavailable |
|---|---|---|
| AM-4-R3 task packet | operator / v4.1 arbitration | D-1 unanswerable; G3 package cannot be assessed on its central claim |
| GLM G3 acceptance ruling | GLM | G3 stays NOT ACCEPTED |
| `raphael-terminal-freeze-inconclusive` tag (if it exists) | operator | D-5 unanswerable; verdict-record integrity gap remains |
| Lockfile / dependency pin | engineering + operator | Floor cannot be reproduced across machines; §7.2 fingerprint is weaker than it should be |

**Requests:**

1. **Operator** — produce the AM-4-R3 packet; decide D-4, D-5, D-6 authorization, D-7, and
   ratify or reject the six PROPOSED decisions.
2. **GLM** — rule on D-1 (given the packet), D-2, D-3, D-9; then perform the §14.12
   adversarial review and issue D-10.

---

## 12. Readiness conclusion

> ### The packet is **NOT** a G3 gate submission, and no gate is accepted.

**What this investigation established:**

- **AM-4-R3:** `NO_EXECUTION_EVIDENCE_FOUND`. Zero commits, zero artifacts. AM-4-R2 is
  separately and **strongly evidenced** in code. The two must not be conflated. The packet
  that defines R3 does not exist in this repository.
- **78-file census:** the reported inconsistency **does not exist**. `F2 001R2` (140 files,
  68/6/5/61) and `F2 001R6` / `U-3` (150 files, 78/6/4/62) describe different censuses;
  `CENSUS.md` at HEAD empirically tallies **78 welded / 6 mediated / 4 notes / 62 dead =
  150**. This blocker should be struck. The *substantive* question — whether "welded" is
  verified rather than labelled, and whether "dead by import failure" counts as deleted —
  remains open and is GLM's to rule.
- **Effect sizes:** unfavourable on **two independent axes** — provenance (dataset
  UNVERIFIABLE, instrument UNVERIFIABLE_DRIFT) and interpretation (the project's own
  SENTINEL verdict froze the project as inconclusive and barred terminal superiority
  publication). No existing decision record covers it; options are set out without selection.
- **Test floor:** **seven** figures, not six. None describes HEAD. The two
  transcript-backed figures disagree on interpreter, revision and duration. None satisfies
  the eight criteria in §7.2. A protocol is supplied, unexecuted.
- **Two prior-report errors corrected:** the 78-file blocker (Q2) and the §14.11/§14.12
  evidence characterisation (§8). Both corrections reduce the apparent blocker set.

**Remaining true blockers to a G3 submission:** D-1 (AM-4-R3 packet + ruling), D-6 (floor),
and the §14.12 GLM adversarial review. D-2, D-3, D-4, D-5, D-8, D-9 are decisions, not
unknowns — they can be closed by the named authority without further investigation.

**Confidence.** High on Q1, Q2 and Q4 (directly reproducible from committed objects and
files). High on Q3's provenance findings; medium on Q3's interpretation consequences, which
turn on the absent tag and the unreviewed remote. No conclusion here depends on executing any
test.

---

*Ends here. Nothing was committed, signed, ratified, or accepted. G3 remains NOT ACCEPTED.*
