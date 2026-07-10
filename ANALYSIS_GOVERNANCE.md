# DPR Analysis Governance

This document defines the mandatory operating rules for the dissertation
analysis developed on `agent/DPR-analysis-records`.

## Reproducibility Principle

Every material data or analysis operation must be committed to this branch.
The history must remain traceable, reversible, and reviewable.

Material operations include:

- source extraction and schema changes;
- identifier linkage and harmonization rules;
- cleaning, exclusion, allocation, and imputation rules;
- panel, network, sequence, and model construction;
- diagnostic, table, figure, and report generation;
- reruns caused by source-data or code changes.

Do not combine unrelated operations in one commit. Do not squash analysis
history. Correct an earlier decision with a new commit that documents the
reason and its effect instead of rewriting published history.

## Required Commit Record

Each analysis commit must identify, in code, configuration, a run manifest,
or the commit message:

1. input tables or files and their relevant versions or extraction time;
2. the processing rule or analytical decision applied;
3. outputs created or changed;
4. validation performed, including row counts and key quality checks;
5. known limitations or unresolved linkage and missingness issues.

Use focused commit subjects such as:

- `source: inventory ClickHouse tables for Study 2`
- `data: harmonize KAKEN member identifiers`
- `panel: build lagged promotion-risk predictors`
- `diagnostics: report AP-year validation results`
- `analysis: estimate baseline cloglog model`

Generated outputs must be reproducible from committed code and configuration.
For outputs too large for Git, commit a manifest containing the command,
timestamp, source snapshot information, row counts, schema, checksums, and
storage location. Never commit passwords, tokens, private keys, local secrets,
or temporary database extracts.

## Current Source-of-Truth Rules

- KAKEN project category is
  `v_jp_researchers_kaken_project.research_category`.
- Distinguish the KAKEN website user identifier from the JPR researcher
  `userId`. The dissertation researcher linkage uses the JPR `userId`.
- Do not remove unmatched KAKEN project members before computing team size or
  fractional-budget denominators. Include every identifiable project member
  in the denominator, then attach allocations to linked JPR researchers.
- Record true non-participation, unresolved linkage, and limited source
  coverage as distinct states.
- Study 2 predictors for promotion in fiscal year `t` must use only information
  observed before `t`. Promotion-year and post-promotion KAKEN or network
  information must not enter the risk model.
- Associate Professor events must come from harmonized research-experience
  titles, including `准教授` and `associate professor` patterns, rather than
  assistant-professor views.

## Branch Protection Practice

Before each push:

1. inspect the staged diff and confirm that it contains one coherent change;
2. run the relevant tests and data-quality checks;
3. record failures or skipped checks explicitly;
4. confirm that no credential or confidential raw data is staged;
5. push without force and retain all prior commits.

Any methodological rule change must be accompanied by updated documentation,
tests where applicable, and a comparison of affected sample or output counts.
