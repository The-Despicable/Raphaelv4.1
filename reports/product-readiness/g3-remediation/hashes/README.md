# Hash manifests — G3 remediation evidence

Every file here is a `sha256sum` manifest generated during the 2026-10-09 G3
remediation task. Generated read-only; regenerating them requires re-running the
commands in `../G3_REMEDIATION_REPORT_20261009.md` §4–5.

| File | Scope | Files | What it proves |
|---|---|---|---|
| `BEFORE_protected.sha256` | **all git-tracked files** at task start | 67,641 | Pre-change state of the entire tracked tree |
| `AFTER_all_tracked.sha256` | all git-tracked files, post-change | 67,641 | Same scope as BEFORE — valid comparison |
| `AFTER_final.sha256` | all git-tracked files, final re-verification | 67,641 | Independent third confirmation |
| `DELTA_tracked.txt` | diff BEFORE vs AFTER | 12 lines | Exactly 3 tracked files changed, 0 added, 0 deleted |
| `C2_BEFORE_wt.sha256` | protected trees in the **disposable worktree**, pre-run | 58,929 | C2 nested-suite baseline |
| `C2_AFTER_wt.sha256` | same trees, post-run | 58,929 | **Byte-identical to BEFORE** (`cmp` exit 0) |
| `C2_DIFF.txt` | diff of the two above | **0 bytes** | Nested suite modified nothing |
| `_all_tracked.txt` | the `git ls-files` input used for the manifests | 67,645 | Reproducibility of the manifest scope |

## Naming caveat

`BEFORE_protected.sha256` was intended to cover only the *protected evidence*
subtrees. A shell variable was consumed by the calling shell on the first
invocation, so it actually covered **all** tracked files. The AFTER manifests
were regenerated at that same all-tracked scope so the comparison is valid — and
the wider scope is the stronger claim. The file name is retained rather than
rewritten so the historical artefact stays auditable.

An intermediate `AFTER_protected.sha256` (protected-subset scope, **not**
comparable to BEFORE) was deleted rather than left in place with a misleading
name.

## Excluded from all manifests

`cai_service`, `cloak_service`, `mcp_hub`, `mhddos_service` — broken tracked
symlinks pointing at an absent `/home/yaser/raphael-2.0` tree. Unreadable by
`sha256sum`, therefore excluded **identically** from before and after.
Pre-existing and outside this task's scope.

## The three intentionally changed files

`README.md` (A5), `evidence/DEFECT_REGISTER.md` (C3),
`evidence/phases/P3_0_reinventory/WELD_SET.md` (A2).
All other 67,638 tracked files are byte-identical.
