# ADR-013 — AM-4-R3 Execution Status and the Weld-Claim Precedence Conflict

| Field | Value |
|---|---|
| ADR | 013 |
| Phase | P3 (G3 submission support) |
| Status | **Proposed — recorded, NOT adopted.** See "Status semantics" below. |
| Deciders | *Unassigned.* This ADR is authored by an engineering remediation task and has **no** decider. Ratification is an operator/GLM act that has not occurred. |
| Source | `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` §40.0.1, §36, Appendix D, Appendix E; `docs/adr/ADR-005` (AM-4.1–AM-4.5); `evidence/phases/P3_0_reinventory/WELD_SET.md` |
| Authority | *None claimed.* This record does not amend the roadmap. |
| Date | 2026-10-09 |

## Status semantics (read first)

This ADR is a **governance record of an unresolved conflict**, not a decision.

- It does **not** declare AM-4-R3 executed, partially executed, or waived.
- It does **not** accept, amend, or reinterpret any roadmap gate.
- It does **not** change G3's status, which remains **NOT ACCEPTED**.
- Its `Status: Proposed` means exactly *"this text awaits authority review"* — nothing more.
  Per roadmap Appendix E it does not yet sit at precedence level 1, because no authority has
  adopted it.

---

## 1. Context

### 1.1 What the roadmap says

The canonical roadmap states, in four separate places:

| Location | Text |
|---|---|
| Line 25 | `**AM-4-R3: NOT EXECUTED.**` |
| Line 28 | `**Next engineering action: execute AM-4-R3; do not begin RSI implementation before G3 passes.**` |
| Lines 3508 | `AM-4-R3 has **not** been executed. G3 has **not** passed. No RSI implementation is authorized yet.` |
| Lines 3627–3631 | `AM-4-R3 prompt: EXISTS / NOT YET EXECUTED` / `AM-4-R3 implementation: NOT EXECUTED` / `G3: BLOCKED` / `RSI implementation: NOT STARTED` |
| Appendix D (4657–4660) | `AM-4-R3: NOT EXECUTED` / `G3: BLOCKED` / `RSI IMPLEMENTATION: NOT STARTED` / `NEXT ENGINEERING STEP: AM-4-R3` |

Roadmap §36 additionally fixes the required sequence:

```text
AM-4-R3 → independent audit of AM-4-R3 → re-derive/reconcile CENSUS + WELD_SET
        → pass G3 → start P4
```

and §37 forbids, "until G3 passes": adding ExperienceNode infrastructure to production,
activating Student learning, implementing a replay simulator, adding policy
promotion/deployment, modifying the Runtime for RSI purposes, and introducing a second loop.

### 1.2 What the weld record says

`evidence/phases/P3_0_reinventory/WELD_SET.md` records all 15 weld items (W-01…W-15) as
carrying a `WELDED (gate …)` claim, with deletion evidence at the named call sites.

### 1.3 The conflict

`WELD_SET.md` (precedence level **5** — repository evidence) asserts a complete weld outcome.
The roadmap (precedence level **2**) asserts that the named execution packet `AM-4-R3` has not
been executed.

Under **Appendix E**, level 2 outranks level 5. The roadmap's `NOT EXECUTED` status therefore
**stands**, and the weld claim does not override it.

---

## 2. Findings — what the evidence does and does not establish

These were established by read-only inspection at revision
`fc3e2c132591eab7edaa12e97e13fe2d01619411` / tree `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061`.

### 2.1 Established

| # | Finding | Label |
|---|---|---|
| F-1 | A repository-wide search for the string `AM-4-R3` (Markdown, JSON, Python) returns **matches only inside the canonical roadmap itself**. | `PROVEN` |
| F-2 | **No artifact identifying the AM-4-R3 packet exists in the repository** — no prompt, no task definition, no scope statement, no execution record, no independent-audit record. | `PROVEN` |
| F-3 | `WELD_SET.md` repeatedly attributes its deletion work to **`AM-4-R2`** (e.g. "route gate (403) added AM-4-R2", "legacy execution branches DELETED … (AM-4-R2)"), never to R3. | `REPORTED` (read from the record) |
| F-4 | `evidence/g3_remediation/STATUS.md:17` states `G3 NOT ACCEPTED (no GLM ruling yet)`. | `REPORTED` |
| F-5 | No commit, file, or ADR in the repository records a G3 acceptance ruling. | `PROVEN` |
| F-6 | `tests/test_am4_weld_gates.py` contains **47 test functions** at this revision. Presence only. | `PROVEN` (static count) |

### 2.2 Not established — and therefore **not** claimed

- That AM-4-R3 was executed, in whole or in part. The weld work cites **R2**, not R3.
- That the weld work and the AM-4-R3 packet are the same work. **They are not equated here.**
- That the AM-4-R3 prompt does not exist. The roadmap says it `EXISTS`; it simply is **not in
  this repository** (it may be operator-held). Its absence here is not its absence everywhere.
- That any weld claim is false. The weld claims are engineering records that were **not
  re-verified** by this task.

### 2.3 On the meaning of "AM-4-R3"

`AM-4-R3` is **not** `AM-4.3`. Per `docs/adr/ADR-005`, AM-4 has five numbered clauses —
AM-4.1 positive interface, AM-4.2 weld semantics, AM-4.3 G3 exit condition, AM-4.4 rollback
discipline, AM-4.5 deletion. `AM-4-R3` is instead the roadmap's name for a **third
revision/step of the AM-4 remediation task packet**, described at line 3622 as "the already-issued
**AM-4-R3** implementation packet governed by the v4.1 arbitration". Its exact contents are
**not recoverable from this repository** (F-2). Any reconciliation attempt that guesses them
would be fabrication.

---

## 3. Decision recorded

**The roadmap's `AM-4-R3: NOT EXECUTED` status is retained unchanged.**

Concretely, this ADR records that:

1. The `NOT EXECUTED` status at roadmap lines 25, 3508, 3628 and Appendix D stands. It is
   **not** withdrawn, softened, or reinterpreted by the existence of weld records.
2. **No existing work is relabelled as AM-4-R3.** The weld records cite AM-4-R2; they remain
   attributed to AM-4-R2.
3. The `WELDED (gate …)` claims in `WELD_SET.md` stand as **engineering claims** that have not
   been independently re-verified and are **not** a gate acceptance.
4. G3 remains **NOT ACCEPTED**. Nothing in this ADR changes that.
5. Only the designated authority — GLM for architecture/gate adjudication, the operator for
   task packets and ratification — may (a) supply the missing AM-4-R3 packet and execution
   record, (b) rule that the existing weld work discharges the AM-4-R3 obligation under a
   different task ID, or (c) accept G3. **Engineering cannot and does not do this.**

---

## 4. Consequences

### Positive
- The precedence conflict is now explicit, recorded, and referred, instead of being silently
  reconciled by whichever document a reader happens to open first.
- A future adjudicator can see, in one place, exactly what evidence exists and what is missing.
- No historical artifact was altered to make documents agree.

### Negative / accepted cost
- The conflict remains **open** after this ADR. That is deliberate: resolving it requires
  authority this task does not have.
- G3 remains blocked. The G3 package is **not** ready to submit until this is ruled.

### Neutral
- No code, test, policy, evaluation anchor, or historical evidence file was changed.
- `ADR-005` is unchanged and remains the authority on AM-4 clause semantics.

---

## 5. Open items for the authority

1. **Supply the AM-4-R3 task packet** (or confirm it is operator-held and out of repository), so
   its scope can be compared against the weld records.
2. **Rule on whether the AM-4-R2 weld work discharges the AM-4-R3 obligation.** If yes, that
   requires an explicit roadmap/ADR amendment with the reasoning recorded — not a silent
   reinterpretation.
3. **Rule on the 78-file relabelling inconsistency** recorded in `WELD_SET.md` (U-3 says the 78
   formerly not-yet-mediated files "now read `Pxx welded`"; `F2_PERIMETER_RECORD.md` 001R6 still
   presents them as not-yet-mediated). This changes a substantive security claim about 78 files
   and **was deliberately not resolved** by this task.
4. **Rule on the P9 deletion ruling** for gated library code (recorded as D-1 in `WELD_SET.md`).

---

## 6. Numbering note — ADR-011 collision NOT resolved here

`docs/adr/` contains **two different files numbered ADR-011**:

- `ADR-011-arena-clause-addendum.md` — "Arena-Clause Addendum", self-labelled `ADR | 011 (arena-clause addendum)`, Status: Accepted
- `ADR-011-sandbox-layer-mechanisms-not-authorization.md` — "`orchestrator/sandbox/` is Mechanisms-Only"

A repository-wide count finds **68 textual references to `ADR-011`**, so the ambiguity is
load-bearing, not cosmetic.

**This ADR therefore takes the next free number, `ADR-013`, and does not renumber ADR-011.**
Correct disambiguation requires touching the 68 references and is a **wider change than this
task's scope permits**. Resolving it by renaming either ADR-011 here would silently alter which
document existing references point at. The collision is **referred, not fixed**.

## 7. References

- `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` §36 (line 3496+), §37 (line 3519+), §40.0.1 (line 3620+), Appendix D (line 4650+), Appendix E (line 4665+)
- `docs/adr/ADR-005-legacy-migration-seam.md` (AM-4.1–AM-4.5 clause semantics)
- `evidence/phases/P3_0_reinventory/WELD_SET.md` (weld claims; U-3; D-1)
- `evidence/g3_remediation/STATUS.md` (G3 NOT ACCEPTED)
- `evidence/g3_remediation/F2_PERIMETER_RECORD.md` (150-file census, 001R6)
- `reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md` (AM-4-R3 sequencing)
