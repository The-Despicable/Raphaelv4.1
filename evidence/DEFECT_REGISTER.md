# DEFECT REGISTER — raphael-2 (branch offensive-restore)

Living register for confirmed defects formally deferred out of hardening
milestones. Entries are numbered `DR-NNN`, state the cause, the impact, the
deferral decision, and the owning milestone/ticket.

**Register maintenance note (2026-10-09):** DR-002 and DR-003 were added on branch
`governance/rsi-1-provenance-correction` by the G3 remediation task. The header's
branch attribution (`offensive-restore`) is the branch on which DR-001 was recorded
and is left unchanged rather than rewritten. Both defects are `DEFERRED`; neither is
closed, and closing either requires the conditions stated in its entry.

---

## DR-001 — `sword.phase_2_exploit` validator interface drift

- **Discovered**: 2026-10-04 import sweep (M0 reassessment §3; class "code drift").
- **Cause**: `src/sword/phase_2_exploit.py:4` imports
  `validate_exploit_results` from `orchestrator.validation.exploit_validator`
  and calls it (line ~55) as `await validate_exploit_results(raw, self.target)` —
  i.e. an **async validator of raw scan results**. The validator module exposes
  only `validate_exploit(exploit_config: dict, target: str) -> dict` — a **sync
  validator of an exploit config** whose payload expects a `safe_checks` key.
  Signatures, sync/async shape, and input semantics all differ; there is no
  evidence the results-validator ever existed under this name.
- **Impact**: `sword.phase_2_exploit` fails to import
  (`ImportError: cannot import name 'validate_exploit_results'`). No canonical
  Runtime path imports it (Runtime import closure is Arena-free and does not
  include sword); it counts as 1 of the 19 remaining fresh-process import
  failures. It does not affect M0–M3 acceptance paths.
- **Why not fixed in M2.1**: aliasing `validate_exploit = validate_exploit_results`
  would not be behavior-preserving (wrong input semantics; sync/async mismatch;
  the sword call site awaits a coroutine). Repairing it properly means designing
  the missing results-validation semantics for an offensive module — squarely
  out of the hardening milestone's boundary ("M2.1 should not expand into a
  general repair of the offensive codebase").
- **Disposition**: **formally deferred.** Fix belongs with the sword service
  bring-up work (gap-plan M4/M6 scope) alongside the other sword wiring.
- **Owner**: implementation engineer, sword workstream ticket.

---

## DR-002 — second pinned-anchor read (fail-closed, but not one-observation purity)

- **Discovered**: 2026-10-09, RSI-1 blocker resolution (`reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md` §5 item 7).
  The entry was specified there and remained unimplemented until this record.
- **Source description (verbatim from that report, lines 340–341)**:
  *"DR-002 (F1 — second pinned-anchor read; fail-closed but not literal one-observation purity)"*.
- **Cause (code-grounded, `src/orchestrator/rsi/evaluation_gate.py`)**:
  * `load_authoritative_anchor()` (:1285) re-reads the pinned anchor file from disk and re-verifies
    its digest against `AUTHORITATIVE_ANCHORS` on every invocation.
  * `_classify_with_authority()` (:2085–2093) documents the refactor intent explicitly: the ledger
    derives authority *"exactly ONCE per admission … instead of re-reading pinned anchors three
    times and risking a mid-admission change."*
  * `verify_authoritative_holdout()` (:1482) is **public** and calls `load_authoritative_anchor()`
    itself, so an anchor observation can be taken outside the admission flow and then a second
    one taken during admission.
- **Impact**: within a *single* admission the one-observation property is intended and the
  fail-closed behaviour is not in question. Across a *sequence* of operations the pinned anchor is
  read more than once, so a mid-sequence change of the anchor file's bytes would be observed by one
  operation and not another. The anchored manifest is digest-pinned, so such a change would be
  rejected as `HOLDOUT_ANCHOR_TAMPERED` rather than silently honoured — the failure mode is
  refusal, not mis-authorisation.
- **Why not fixed now**: the mitigations each constitute a behavioural change to
  `_classify_with_authority`/`verify_authoritative_holdout` or a new integrity subsystem. Neither
  is in the authorized scope of the 2026-10-09 G3 remediation task (items A1–A5, C1–C3).
- **Status**: **DEFERRED**.
- **Closure conditions (all required)**: (a) an authority ruling on whether one-observation purity
  is a G3 requirement or a later hardening item; (b) if required, a mechanism that binds one anchor
  observation across the whole operation rather than per call; (c) a test that **pins the property**
  — i.e. fails if a second read is introduced. See *Uncertainty retained* below.
- **Uncertainty retained**: this task did **not** execute any test. Whether any existing test in
  `tests/test_rsi1_policy_identity.py` already pins the one-observation property across operations
  is **`UNKNOWN`** and must be checked by the adjudicator before the item is closed. Do not read the
  presence of a similar test name as evidence that the property is covered.

---

## DR-003 — schema v2 spans old and new evaluator-identity digest semantics

- **Discovered**: 2026-10-09, RSI-1 blocker resolution
  (`reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md` §5 item 7).
- **Source description (verbatim from that report, lines 341–343)**:
  *"DR-003 (F4 — schema v2 spans old/new digest semantics; stale records refused via
  re-derivation + evaluator identity)"*.
- **Cause (code-grounded, `src/orchestrator/rsi/evaluation_gate.py`)**:
  * `SCHEMA_VERSION = 2` (:47).
  * `EvaluationDecisionRecord.evaluator_identity` (:1882) is a free string.
  * `EvaluatorIdentity.is_placeholder()` (:281–287) returns `True` for anything that is not a
    64-character lowercase hex string, or that matches a known placeholder label.
  * `_is_hex_sha256()` (:202–205) is the hex test.
  * The `evaluator_identity_current` gate (:2113–2122) refuses on three distinct paths and
    distinguishes them by reason: *placeholder / non-digest*, *stale or foreign* (a well-formed hex
    digest that differs from the currently derived identity), and *malformed*.
  So a single `schema_version: 2` field can legitimately carry a **free-text label written under
  the older semantics** or a **digest written under the newer semantics**, and the schema itself
  does not record which semantics a given record was written under. The gate resolves this safely
  by re-deriving the authoritative identity from the current evaluator modules and comparing —
  all such records are refused.
- **Impact**: **no authority-granting path is opened** — every variant is refused. The defect is
  schema hygiene: one version number spans two meanings, so a reader of a schema-v2 record cannot
  tell from the record alone which identity semantics produced it, and refusal *reason* is the only
  signal available downstream.
- **Why not fixed now**: separating the semantics requires a schema version bump and a
  compatibility/migration decision for stored records — a governed schema change, outside the
  authorized scope.
- **Status**: **DEFERRED**.
- **Closure conditions**: (a) an authority decision on whether to introduce an explicit
  `evaluator_identity_kind` discriminator or a `schema_version = 3`; (b) if a discriminator is
  added, a decision on how existing stored records are treated (refuse vs. grandfather); (c) a
  test pinning that no record can reach `PROMOTION_ELIGIBLE` under either semantics.
- **Uncertainty retained**: this task did **not** execute any test, and did **not** enumerate
  production consumers of the refusal *reason* string. Whether any consumer distinguishes
  `"stale or foreign"` from `"malformed"` is **`UNKNOWN`**.

---

### Related, already-classified (not separate tickets here)

The 18 structural import failures (arena `d6c_holdout_runner` cwd-based runners
×10, `mcp-hub.*` internal naming ×3, `config` vs `configs/` ×2,
`case_store` recon-pipeline ×3) are classified in
`evidence/M0_REVIEW_REASSESSMENT_20261004.md` §3 with per-module cause and
milestone assignment (service bring-up, M4/M6). They are unchanged by M2.1.
