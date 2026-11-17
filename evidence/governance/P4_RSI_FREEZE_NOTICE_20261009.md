# P4 / RSI Work-Freeze Notice

**Date:** 2026-10-09
**Status:** **ACTIVE** — this is an operational constraint, not a roadmap amendment.
**Authority:** none claimed. This notice records a sequencing constraint that
already exists in the canonical roadmap; it does not create, relax, or interpret
any gate.

---

## 1. The constraint this restates

The canonical roadmap (`RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md`) already says, in five
places, that no further P4 or RSI implementation work is authorized:

| Location | Text |
|---|---|
| Line 28 | `do not begin RSI implementation before G3 passes.` |
| Line 698 | `No RSI implementation work begins before G3.` |
| Line 3508 | `AM-4-R3 has **not** been executed. G3 has **not** passed. No RSI implementation is authorized yet.` |
| Lines 3521–3528 | "Until G3 passes, do **not**: add ExperienceNode infrastructure to production; activate Student learning; implement a replay simulator; add policy promotion/deployment; modify the Runtime for RSI purposes; introduce a second loop." |
| Appendix D | `G3: BLOCKED` / `RSI IMPLEMENTATION: NOT STARTED` / `NEXT ENGINEERING STEP: AM-4-R3` |

**Observed state at revision `fc3e2c132`:** G3 is NOT ACCEPTED (no GLM ruling artifact
exists), while P4.1–P4.5 and 20+ `RSI-1:` commits are already present. The freeze
exists to stop that gap widening.

## 2. What is frozen

No **new** work in:

- `src/orchestrator/rsi/` beyond defect closure on already-landed RSI-1 modules
- P4.1–P4.5 scope (MissionSpec/Scope/AuthContext/ReceiptStore/ArtifactStore and successors)
- Student learning activation; replay simulator; policy promotion or deployment
- P5, P6, P7, P8, P9, P10 in any form
- any second Runtime, execution path, authorization authority, or cognitive loop

## 3. What remains authorized

Only the items the operator explicitly authorized on 2026-10-09 for the G3
submission: **A1–A5 and C1–C3**. Defect closure on already-landed RSI-1 modules
(for example `DR-002`, `DR-003`) is permitted. Records, evidence, tests and
documentation that support a G3 submission are permitted.

## 4. Review procedure (no new subsystem)

A freeze is only as good as the review that catches violations, so the check is
made explicit and human rather than automated. **No enforcement subsystem was
added** — that would be a new governed surface and is out of scope.

**Before any commit whose subject matches** `RSI`, `P4`, `P5`…`P10`, `replay`,
`promotion`, `student learning`, or which touches `src/orchestrator/rsi/`:

1. **Confirm the gate.** Is there a recorded G3 acceptance ruling? At the time of
   writing there is not. If there is not, the change is out of order.
2. **Confirm the requester.** The change must reference a task packet that an
   authority issued. A change justified only by "the roadmap design is complete"
   is not authorized — roadmap §36: *"Do not skip gates … because supporting code
   already exists."*
3. **Confirm scope.** The change must not touch the canonical control plane
   (`src/orchestrator/runtime/`, `src/orchestrator/brain/capability_broker.py`,
   `src/orchestrator/exec/`) for RSI purposes.
4. **Record the decision, don't assume it.** If a gate ruling is claimed, cite the
   artifact path. An unverifiable claim is a stop condition.

**Who performs it:** the implementing session, before committing, and the reviewer
during G3 adjudication.

**Deliberately not implemented:** a CI gate, a pre-commit hook, or a registry of
"allowed" RSI commits. Those change the repository's enforcement surface and need
their own approval. This section is the human procedure that stands in their
place until then.

## 5. How the freeze lifts

Only by an **explicit authority act**:

1. a recorded GLM ruling that **G3 is accepted**, and
2. for anything beyond G3, the corresponding later gate acceptance.

Engineering cannot lift this notice, and neither can a test result, a green suite,
or the existence of implementation code. A superseding ADR or roadmap amendment,
adopted by the designated authority, would replace this notice.

## 6. Related

- `docs/adr/ADR-013-am4-r3-status-and-precedence-conflict.md` — the AM-4-R3 status
  and the roadmap/evidence precedence conflict
- `reports/product-readiness/g3-remediation/G3_REMEDIATION_REPORT_20261009.md` —
  this task's report and handoff
- `RAPHAEL_MASTER_ROADMAP_v4.2_RSI.md` §36, §37, Appendix D

---

*Operational notice. Changes nothing about gate status. G3 remains NOT ACCEPTED.*
