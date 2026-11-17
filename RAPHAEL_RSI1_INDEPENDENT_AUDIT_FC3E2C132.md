# RAPHAEL RSI-1 — Independent Audit Report

**Frozen target:** commit `fc3e2c132591eab7edaa12e97e13fe2d01619411`,
tree `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061`,
parent `9936223dc0363cc4b3f210c1c3015f20b7c379c6`,
branch `governance/rsi-1-provenance-correction`,
repository `https://github.com/The-Despicable/raphael-audit-target.git` (private).

**Report date:** 2026-10-09
**Status of verdict:** completes this commission.

---

## 1. Auditor identity, role, and independence declaration

- **Role:** independent software-assurance auditor engaged to audit the frozen
  commit, reproduce evidence, run adversarial checks, and issue a verdict.
- **Independence:** I did **not** author, materially implement, review, or
  co-develop any commit under audit. The commit authors are recorded in Git as
  `OMP Agent <agent@local>` for every commit `1fd7cda76..fc3e2c132`; the
  operator of record is `The-Despicable`. I am a separate, freshly instantiated
  audit agent. I therefore **claim independence** and issue a verdict.
- **Disclosures / limitations:**
  - I executed the audit inside the operator's machine/WSL environment. My Git
    identity inherited the global config `user.name=The-Despicable`, but I made
    no commits, and the frozen target was never modified by me. The only writes
    I performed were to a disposable clone (`~/audit-rsi1/target`) and to an
    audit workspace (`~/audit-rsi1`), both outside the audited tree.
  - I did **not** treat the author's own reproduction report as evidence; every
    result below was independently re-run or re-derived.
  - I did not authenticate the *human* behind `OMP Agent`; independence is
    asserted at the agent/implementation level, not as a personnel attestation.

## 2. Repository, commit, tree, parent, and clean-checkout verification

| Check | Expected | Observed | Result |
|---|---|---|---|
| Remote branch tip | `fc3e2c132…` | `git ls-remote https://…/raphael-audit-target.git governance/rsi-1-provenance-correction` → `fc3e2c132591eab7edaa12e97e13fe2d01619411` | **VERIFIED** |
| HEAD (audited clone) | `fc3e2c132…` | `fc3e2c132591eab7edaa12e97e13fe2d01619411` | **VERIFIED** |
| Tree | `e24d42bf…` | `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061` | **VERIFIED** |
| Parent | `9936223dc…` | `9936223dc0363cc4b3f210c1c3015f20b7c379c6` | **VERIFIED** |
| Clean checkout | 0 modified | `git status --porcelain` → 0 tracked changes | **VERIFIED** |

- The private repository **is accessible** (stored credentials); the remote
  serves exactly the frozen commit. No `NOT VERIFIABLE — PRIVATE REPOSITORY
  ACCESS REQUIRED` condition applies.
- Ancillary tree bindings also verified: `9936223dc → d68d8e4d…`,
  `1fd7cda76 → 49237b06…`, `2d049e2f → 191ae07e…`.
- Method: audited a **disposable clone** of the branch (not the operator's
  working checkout) detached at the frozen commit; primary checkout re-checked
  pristine before and after. No amend/rebase/cherry-pick/push occurred.

## 3. Commands, environment, test ledger

Environment (matches the committed remediation manifest):
Python `3.12.15`, pytest `9.1.1`, torch `2.14.1+cu130`, numpy `2.5.3`,
pydantic `2.13.5`, sqlalchemy `2.1.3`, transformers `5.18.0`, venv
`~/external-audits/raphael-2/.venv` (no editable install; imports via
`pythonpath=["src"]`). Configured scope from `pyproject.toml`:
`testpaths = ["tests"]`, `pythonpath = ["src"]`, `asyncio_mode = "auto"`.

Commands (run from the disposable clone):
- Full configured suite: `python -m pytest -q`
- Focused: `python -m pytest -q tests/test_historical_split_adjudication_package.py`
  (and the two sibling files below)

| Suite | Command | Exit | Result | Reported | Match |
|---|---|---:|---|---|---|
| Full configured suite | `pytest -q` | 0 | **1452 passed, 44 warnings** | 1452 / 44 | **VERIFIED** |
| Historical split-adjudication package | `pytest -q tests/test_historical_split_adjudication_package.py` | 0 | **35 passed** | 35 | **VERIFIED** |
| Historical call-site rulings | `pytest -q tests/test_rsi1_historical_call_site_rulings.py` | 0 | **19 passed** | 19 | **VERIFIED** |
| F-SPLIT-1 split vocabulary | `pytest -q tests/test_f_split_1_split_vocabulary.py` | 0 | **74 passed** | 74 | **VERIFIED** |

Warnings (44): 26 × `PytestReturnNotNoneWarning` (test functions returning a
non-`None` value), 4 × `DeprecationWarning`, 1 × `UserWarning` (CUDA driver too
old for the bundled torch), 1 × `SyntaxWarning` (invalid escape sequence).
**Significance:** non-blocking test hygiene; none indicates a behavioral defect.
An initial run under `-W default` surfaced 50 warnings; under default filters the
count is exactly 44 — the difference is filter-induced, not a real drift.

Additional suites independently run (all exit 0): `test_rsi1_policy_identity`
69, `test_rsi1_config_adoption` 59, `test_rsi1_production_adoption_registry` 26,
`test_rsi1_holdout_classification` 17, `test_rsi1_governance_remediation` 69,
`test_phase3_evidence_binding` 21, `test_rsi1_measurement_integrity` 93,
guardrail subset (single-runtime / no-bypass / no-seam / belief-port /
deny-by-default / evaluator-isolation / reproducibility / auth-context /
re-inventory) 50.

### 3.1 `src/arena/tests` isolation assessment

- It is **not** in `testpaths`, and it was disclosed as not run
  (`reports/PROVENANCE_CORRECTION_REPORT_20261009.md:192,234`;
  `reports/RAPHAEL_BLOCKER_RESOLUTION_REPORT_2026-10-09.md:333-334`).
- It is **not safe to run in place**: `src/arena/tests/test_runconclusion.py`
  constructs `AblationRunner(...).run()` with no `output_dir`, and there is no
  `conftest.py` under `src/arena` to redirect `RESULTS_BASE`.
- Executed in the disposable clone with before/after integrity checks:
  **4 failed, 69 passed**, and it **mutated 6 tracked historical evidence
  files** (`arena/results/raw/abl_*_known-observable_s0042_dev/episodes.jsonl`).
  All mutations were restored (`git checkout -- .`; final tracked status 0).
- The 4 failures are pre-existing and out of RSI-1 scope: one test explicitly
  raises `NotImplementedError`; the others (`NO_PLANNER`/`NO_FALSIFICATION`
  discrepancy checks) fail in the legacy harness. `src/arena/tests` is
  unchanged across the entire branch (`git diff` vs the Phase-3 starting commit
  is empty; last touched by the v2.0 migration `50ba7cbfe`).
- **Conclusion:** exclusion is operationally justified and disclosed. The claim
  "full configured suite = 1452" is accurate **for the configured scope
  (`tests/`)**, which excludes a nested, pre-existing, evidence-mutating suite.
  See finding **F-3**.

## 4. Evidence-bundle checksums and missing-manifest treatment

- `CHECKSUM_STEP=NOT_APPLICABLE_NO_CHECKSUM_FILE_AT_AUDITED_COMMIT` — the file
  `evidence/historical_split_adjudication/SHA256SUMS` is **absent** at the
  frozen commit: **VERIFIED**.
- `evidence/phase3_readiness/SHA256SUMS`: all 6 entries **OK** (`sha256sum -c`
  exit 0).
- `evidence/provenance_correction/SHA256SUMS`: all 6 entries **OK** (exit 0).
- Independently recomputed SHA-256 of the adjudication package files:
  - `ADJUDICATION_METHOD.md` = `3170e161a3801982188c5542216db21f5e6852d0354d6250e39bf6f19356513b`
  - `call_site_census.json`  = `76c3a18f421aea6222509116981649db03484980f507a7c0f487978c2ef46ffe`
- **Integrity gap recorded:** the adjudication package has **no checksum
  manifest**. This is **not** claimed to have passed verification.
- **Non-blocking determination (justified, not assumed):** the package files are
  Git-committed and therefore content-addressed and tamper-evident through the
  verified tree `e24d42bf…`; their internal consistency is enforced by 35
  behavioral tests including an independent source rescan. The manifest's
  absence does not weaken the digest binding of the other two bundles (both
  verified) and does not enable any authority. It is a **bounded,
  separately-tracked follow-up**, non-blocking for this verdict.

## 5. Independently re-derived historical census and split behavior

- Independent regex rescan of source for `split="validation"`, the typed
  default-argument form `split: str = "validation"`, and `{"split":
  "validation"}` dict keys reproduces **exactly 22 sites** in the artifact:
  **19 live call sites + 3 non-live references** (a negative test, a comment, a
  docstring). Recorded set == rescan set (zero missing, zero stale).
- The 19 live sites are 18 direct `split="validation"` constructions plus
  `scripts/run_experiment0.py:50` (`def run_single(..., split: str =
  "validation")`), which a naive `split=` grep misses — the artifact is more
  complete than a naive scan. **VERIFIED.**
- **Baseline defect VERIFIED:** at `b6ef24bd…:src/arena/ablation_runner.py` the
  resolver read `sp = split_map.get(self.split, ScenarioSplit.DEV)` with keys
  `{"dev","val","holdout"}`, so the legacy label `"validation"` resolved to
  `ScenarioSplit.DEV`. The identical fallback is present at the F-SPLIT-1
  parent `bd1fcc109^`. The frozen commit replaces it with fail-closed
  `_resolve_scenario_split` (`ablation_runner.py:58`, `:73`).
- **Separation of evidence classes VERIFIED:** every site carries
  `evidence_class="ACTUAL_BEHAVIOR_ESTABLISHED_INTENT_UNKNOWN`,
  `actual_historical_behavior="DEV"`, `proposed_ruling="UNKNOWN"`,
  `current_authority_granted=false`, `operator_ruling_status=
  "PENDING_OPERATOR_RATIFICATION"`. Disposition is 22 `UNKNOWN`, zero DEV/VAL/
  HOLDOUT rulings, no authority granted. The package does **not** infer intent
  from the defective implementation, filenames, docstrings, or run IDs; those
  are separately labelled `author_stated_intent_unratified`.
- **Caveat (documentation, not artifact):** the commission text states "22 live
  literal call sites"; the artifact correctly reports **19 live, 22 total**. The
  artifact is right; the brief's phrasing overcounts. See finding **F-4**.
- **Minor self-reference:** `call_site_census.json` declares
  `commit=9936223dc…`/`tree=d68d8e4d…` (its generating commit / parent) rather
  than the containing commit `fc3e2c132`/`e24d42bf`. Defensible (the package was
  generated before it was committed), but note it is not self-binding to the
  commit that contains it.

## 6. Seed-band contradiction (2,394 runs)

- Empirically, over `arena/results/raw/*/manifest.json` (7,337 manifests):
  split distribution `{validation: 2394, holdout: 4543, dev: 200, val: 200}`.
  **All 2,394 `validation` manifests carry a seed in 1000–1999** (none out of
  band). None of the 2,394 dirs carries a `_dev/_val/_holdout` suffix (legacy
  naming). **VERIFIED.**
- `SPLIT_OFFSETS = {DEV: 0, VALIDATION: 1000, HOLDOUT: 2000}`
  (`src/arena/templates/base.py`). Because the baseline mapped the legacy label
  to **DEV (offset 0)**, the absolute seed actually used equals the band value in
  the manifest; re-deriving the same run as **VAL** would add `+1000` and would
  **not** reproduce the historical runs. The conclusion "runs must not be
  represented as authentic VAL/HOLDOUT evidence without independent provenance"
  is arithmetically and evidentially supported. **VERIFIED.**
- Corpus-consumption check: no authoritative evaluation path consumes
  `arena/results/raw`; the only readers are ad-hoc `evaluations/campaign/_audit*.py`
  scripts and `AblationRunner` (a writer). The holdout gate sources its truth
  from the pinned anchor manifest, not this corpus. No accidental authoritative
  consumer found.

## 7. Holdout provenance and policy-identity / adoption

**Holdout:** the canonical `evaluations/campaign/rbs_v4_holdout.jsonl` is
**absent**; `HOLDOUT_CLASSIFICATION_20261009.json` correctly records
`UNVERIFIABLE`, `canonical_status=MISSING`,
`predecessor_dataset_status=ABSENT_AND_UNVERIFIABLE`,
`reconstruction_permitted=false`, and that the earlier "QUARANTINED" claim was
**withdrawn**. Live `verify_authoritative_holdout()` returns **MISSING** with no
substitution. `.gitignore` still blocks `evaluations/campaign/*.jsonl`. No
holdout was reconstructed or backfilled. **VERIFIED.**

**Policy identity / adoption (independently probed against the real API):**
- `resolve_config_adoption(GateConfig(...))` → `UNADOPTED_CONFIG` (no registry is
  pinned: `AnchorSet.adopted_config_registry_file/_sha256 = None`). **VERIFIED.**
- `resolve_policy_identities(config)` without adoption → `POLICY_MANIFEST_UNPINNED`
  and an **empty** identities tuple. **VERIFIED.**
- Caller cannot inject adoption: `resolve_config_adoption(cfg, adoption=True)`
  raises `TypeError` (no such parameter); `adoption_id` is derived, and the
  classifier/build-authority take no adoption input. **VERIFIED.**
- `derive_policy_identity` takes **bytes, not a digest**; passing a digest
  raises `EvaluationGateError`. **VERIFIED.**
- Derived-vs-declared mismatch → `POLICY_IDENTITY_MISMATCH` / `REFUSE`
  **unconditionally** (even when binding is not required). Asserted-only identity
  → `POLICY_IDENTITY_ASSERTED` / `BLOCKED` and can never verify. Supplying only a
  `baseline` identity leaves `candidate` `BLOCKED` (role swap fails closed).
  **VERIFIED.**
- Removed registry: no production adoption registry file exists or is tracked;
  tests `test_no_production_adoption_registry_file_exists`,
  `test_no_adoption_registry_was_created`, `test_a1/a2` pass. **VERIFIED.**
- Tamper / swap / restart are covered by passing tests `k3–k11`, `k17–k24`,
  `c12–c18`, `b12–b13`, `d24–d31` (69/69 policy-identity, 59/59 config-adoption,
  26/26 registry). The trust chain is registry-bytes → config digest → manifest
  digest → artifact bytes, all digest-verified; no ledger or caller identity is
  ever a source.

## 8. Measurement-contract integrity and non-vacuity

`src/orchestrator/rsi/measurement_contract.py` is fail-closed by construction:
- Evidence bytes are read from a **committed, digest-pinned index** and their
  SHA-256 is **recomputed** and compared to the pinned digest; caller asserts
  nothing. **VERIFIED.**
- Attribution: an evidence record's own `run_id` must equal the cell's expected
  run identity, else `UNACCOUNTED`. **VERIFIED.**
- Explicit categories `MISSING_RESULT` / `INVALID_RESULT` / `UNACCOUNTED` /
  `EXCLUDED`; only `EXPECTED_SUCCESS|FAILURE` count toward completeness;
  `assert_complete` raises `GridIncomplete`; `aggregate_result` calls it first;
  **no rate, denominator, or threshold** is produced, and none confers promotion
  authority. **VERIFIED.**
- Non-vacuity proven by mutation (see §9): disabling the digest check breaks 3
  tests; disabling completeness breaks 9, including empty-grid and
  exclusion-cannot-satisfy tests. **VERIFIED.**
- Grid identity mirrors the real runner (`abl_{config}_{family}_s{seed:04d}_{split}`)
  and is pinned against a real constructed `AblationRunner` by test.
- **Gap F-1 (LOW):** `AccountingReport.duplicate_run_ids` is unreachable
  (`EvidenceIndex.records` is a dict, so keys are unique) **and**
  `EvidenceIndex.load` uses plain `json.loads`, which silently collapses
  duplicate JSON keys ("last wins"). Thus duplicate-run-identity detection is
  vacuous and a duplicate-key index is accepted rather than refused. This cannot
  manufacture authority (each cell is still digest- and run_id-verified), so it
  is non-blocking; a proposed hardening patch is supplied in §13.

## 9. Adversarial / mutation results (with restoration)

All mutations applied to the disposable clone and restored; byte-identity and
clean checkout verified afterwards (`call_site_census.json` and
`measurement_contract.py` SHA-256 restored to originals; tracked status 0).

| # | Mutation | Reported failures | Reproduced | Fails for the correct reason |
|---|---|---:|---:|---|
| A | Census path changed | 2 | **2** | `test_every_recorded_path_exists`, `test_every_recorded_line_still_contains_a_match` |
| B | Ruling `UNKNOWN → VAL` | 2 | **2** | `test_ruling_histogram_matches_the_entries`, `test_no_site_claims_a_confirmed_ruling_without_ratification` |
| C | Authority granted | 1 | **1** | `test_no_entry_grants_current_authority` |
| D | Census site removed | 5 | **5** | rescan drift, package-vs-source census, both histograms, report count (5 fails when the header counts are adjusted to stay self-consistent; 4 if not) |
| E | Digest verification disabled | 3 | **3** | `test_tampered_evidence_digest_is_invalid_result`, `test_a_bogus_digest_cannot_buy_a_success`, `test_assert_complete_raises_when_evidence_is_invalid` |
| F | Completeness enforcement disabled | 9 | **9** | empty-grid, missing, invalid, one-missing-among-many, exclusion-cannot-satisfy, aggregate-refused, no-promotion-authority |

- Each failure detects the intended violation (verified by inspecting which
  assertions fired, not just counts).
- Tests were **not** weakened or rewritten to obtain the expected outcome.
- Restoration verified: original SHAs match; final checkout unchanged.

Policy/adoption adversarial probes (live API): caller-controlled adoption
rejected; asserted identity cannot verify; derived mismatch refuses even when
unbound; digest-as-content refused; role swap leaves the other role `BLOCKED`;
anchors pin no registry. `k`-suite additionally covers tampered artifact bytes,
changed manifest digest, wrong campaign, swapped roles, missing artifact/manifest,
path escape, restart regain, and re-read fail-closed after tampering/withdrawal.
**VERIFIED.**

## 10. Protected-boundary review and residual risks

| Concern | Label | Evidence |
|---|---|---|
| Single `RaphaelRuntime` / canonical loop | **CONFIRMED** | one definition, `src/orchestrator/runtime/loop.py:52`; `test_p2_guardrail_single_runtime` passes |
| PDP/Broker + PEP singular and enforced | **CONFIRMED** | single `CapabilityBroker` (`brain/capability_broker.py:277`), `BrokeredExecutionEngine` (`:1280`); `test_p2_guardrail_no_production_bypass`, `runtime_no_seam` pass |
| Planner cannot authorize own proposals | **CONFIRMED** | deny-by-default guardrail suite passes; broker-only receipt authority |
| World-model belief authority protected | **CONFIRMED** | `test_p2_guardrail_belief_transition_port` passes |
| Replay read-only, no real execution | **CONFIRMED** | `snapshot.py` docstring + `verify_snapshot` re-derives from persisted stores, executes no live actions |
| Evaluator/holdout/promotion/human-release boundaries | **CONFIRMED** | holdout MISSING; promotion requires ADOPTED config + verified identities; gate sources are pinned; `test_evaluator_isolation`, `test_p3_0_reinventory_consistency` pass |
| Snapshot-origin provenance | **NON-BLOCKING** | `EVALUATOR_VERSION` is an explicit non-authoritative label; authority = `EvaluatorIdentity.compute_current` content digest over real modules + anchors (`snapshot.py:26-45`, `evaluation_gate.py:212-278`) |
| Historical evidence provenance / digest binding | **NON-BLOCKING** | adjudication files are Git-committed/tree-bound; two bundles verify; missing manifest tracked (§4) |
| Measurement-contract scientific validity | **NON-BLOCKING** | counts-only; produces no rate/threshold and no authority; gap F-1 |
| Missing evidence fails closed | **CONFIRMED** | `MISSING_RESULT`/`INVALID_RESULT`; `GridIncomplete`; holdout `MISSING`; adoption `UNADOPTED_CONFIG` |
| `_check_lineage` reads stored ledger index, not independently derived lineage | **CONFIRMED (by design) / NON-BLOCKING** | `evaluation_gate.py:2571-2607`: lineage compares the new record against the append-only stored predecessor ledger. Lineage *is* the stored history; admission still requires freshly derived authority (`append` re-verifies before lineage). An empty/forged ledger removes lineage pressure but cannot grant authority. No remediation required; document as inherent |

## 11. Findings ranked by severity

| ID | Severity | Finding | Reference | Minimal remediation |
|---|---|---|---|---|
| **F-1** | **LOW** | Evidence-index duplicate run-identity detection is vacuous, and `EvidenceIndex.load` accepts duplicate JSON keys (silently collapsed). Cannot manufacture authority. | `src/orchestrator/rsi/measurement_contract.py:288-314`, `:493-499` | Apply §13 patch (`object_pairs_hook` rejecting duplicate keys) + regression test |
| **F-2** | **LOW** | Adjudication package lacks a `SHA256SUMS` manifest. Disclosed and tracked as follow-up. | `evidence/historical_split_adjudication/` | Add a manifest in a separate, non-audit commit |
| **F-3** | **LOW (out of scope)** | `src/arena/tests` is excluded from the configured suite; when run it fails 4 pre-existing tests and mutates 6 tracked evidence files. | `src/arena/tests/test_runconclusion.py`, `tests/conftest.py` | Add `src/arena/tests/conftest.py` mirroring the `RESULTS_BASE` isolation, then triage the 4 legacy failures |
| **F-4** | **INFO** | Commission brief says "22 live call sites"; the artifact and independent rescan both give **19 live / 22 total**. | `call_site_census.json`, `ADJUDICATION_METHOD.md` | Correct the brief's wording (artifact is correct) |
| **F-5** | **INFO** | `call_site_census.json` self-declares the generating (parent) commit/tree, not the containing commit. | `call_site_census.json` top-level `commit`/`tree` | Optionally re-stamp on next regeneration |

No CRITICAL/HIGH/BLOCKING finding. No unresolved material integrity,
correctness, provenance, or governance defect was found within scope.

## 12. Verdict

**VERDICT: `PASS`** — scoped to code integrity, reproducibility, and provenance
of the audited artifact.

- Commit `fc3e2c132591eab7edaa12e97e13fe2d01619411`
- Tree `e24d42bf7f7655293f3eb3a273c9ce4d94b1e061`
- Parent `9936223dc0363cc4b3f210c1c3015f20b7c379c6`
- Branch `governance/rsi-1-provenance-correction`
- Repository `https://github.com/The-Despicable/raphael-audit-target.git`

**Basis:** commit/tree/parent/cleanliness verified against the live private
remote; the full configured suite reproduces at **1452 passed / 44 warnings**
and all three focused suites reproduce exactly (35 / 19 / 74); both evidence
bundles verify; the census re-derives exactly (19 live / 22 total); the baseline
fail-open defect and the +1000 seed-band contradiction are confirmed; holdout
and adoption fail closed; the measurement contract is non-vacuous; all six
reported mutation outcomes reproduce and fail for the right reasons; and every
mutation was restored with byte-identity re-verified.

**Non-blocking residuals:** F-1 (LOW code hardening), F-2 (missing manifest,
tracked follow-up), F-3 (out-of-scope nested suite), F-4/F-5 (documentation).

**Limitations:** This PASS does **not** assert that historical intent has been
resolved (it remains `UNKNOWN`), that an authoritative campaign has been adopted
(it has not — `UNADOPTED_CONFIG`), that a holdout exists (it is `UNVERIFIABLE`),
that L2 has been demonstrated, or that Phase 3 is authorized. It also does not
attest the human identity behind `OMP Agent`, nor re-audit code outside the
enumerated RSI-1 scope.

**Outstanding operator decisions (outside this commission):** ratify or reject
the 22 historical call-site rulings; decide the canonical holdout's permanent
disposition and any alternative measurement contract; adopt (or continue to
withhold) a production evaluation configuration; authorize or withhold Phase 3.

## 13. Proposed code hardening (not applied to the frozen target)

Verified in the disposable clone: patch applied + regression test → **141
passed (140 baseline + 1 new)**, no regressions, then fully reverted (source
SHA-256 restored, tracked status 0). Proposed as a separate commit; **do not
apply to the frozen audit target**.

```diff
--- a/src/orchestrator/rsi/measurement_contract.py
+++ b/src/orchestrator/rsi/measurement_contract.py
@@ def _stable(obj: Any) -> str:
     return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)
 
+
+def _reject_duplicate_keys(pairs):
+    """object_pairs_hook that refuses duplicate JSON keys.
+
+    The evidence index is keyed by run_id; a duplicated run_id would otherwise
+    be silently collapsed by json.loads (last wins), defeating the run-identity
+    "claimed at most once" guarantee duplicate_run_ids relies on.
+    """
+    result = {}
+    for key, value in pairs:
+        if key in result:
+            raise MeasurementContractError(
+                f"duplicate JSON key in evidence index: {key!r}")
+        result[key] = value
+    return result
+
 
 def _sha256(data: bytes) -> str:
     return hashlib.sha256(data).hexdigest()
@@ class EvidenceIndex:
@@ def load(cls, relpath: str, expected_sha256: str,
              repo_root: Optional[Path] = None) -> "EvidenceIndex":
-        payload = json.loads(raw.decode("utf-8"))
+        payload = json.loads(raw.decode("utf-8"),
+                             object_pairs_hook=_reject_duplicate_keys)
         if not isinstance(payload, dict):
             raise MeasurementContractError("evidence index must be a JSON object")
```

Regression/adversarial test (proposed file `tests/test_rsi1_measurement_contract.py`
addition or standalone):

```python
import hashlib
import pytest
from orchestrator.rsi import measurement_contract as mc

def test_duplicate_run_id_keys_are_refused(tmp_path, monkeypatch):
    monkeypatch.setattr(mc, "_REPO_ROOT", tmp_path)
    raw = (b'{"schema_version":1,"campaign_id":"c","records":{'
           b'"abl_x_f_s0001_dev":{"path":"a.json","sha256":"' + b'0'*64 + b'"},'
           b'"abl_x_f_s0001_dev":{"path":"b.json","sha256":"' + b'1'*64 + b'"}}}')
    (tmp_path / "idx.json").write_bytes(raw)
    digest = hashlib.sha256(raw).hexdigest()
    with pytest.raises(mc.MeasurementContractError):
        mc.EvidenceIndex.load("idx.json", digest)
```

Exact verification command (run it yourself after applying, in an isolated
worktree): `python -m pytest -q tests/test_rsi1_measurement_contract.py
tests/test_rsi1_measurement_integrity.py`

---

### Evidence-class legend used above
`VERIFIED` = independently reproduced/re-derived in this audit;
`REPORTED` = asserted by author/commission, not independently confirmed;
`INFERRED` = reasoned from verified facts; `NOT VERIFIABLE` = not obtainable.

### Artifacts produced by this audit (outside the frozen target)
- Disposable audited clone: `~/audit-rsi1/target` (detached at `fc3e2c132`, pristine)
- Audit scripts/probes: `~/audit-rsi1/*.sh`, `~/audit-rsi1/*.py`
- Raw test outputs: `~/audit-rsi1/full_suite_audit.txt`, `~/audit-rsi1/full_suite_default.txt`
