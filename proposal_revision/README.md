# Dissertation Proposal Revision

This directory records the reproducible revision of the supplied dissertation
proposal. The source DOCX remains outside this directory and is never modified.

## Principal deliverables

- `Doctoral_Dissertation_Proposal_PEI_Rongkang_revised_tracked.docx`: review copy
  with WordprocessingML tracked insertions.
- `Doctoral_Dissertation_Proposal_PEI_Rongkang_revised_clean.docx`: clean reading
  copy.
- `proposal_revision_memo.md`: substantive change record and interpretation
  boundaries.
- `citation_audit.csv`, `references.bib`, and `literature_search_log.md`:
  literature provenance and claim-level citation checks.
- `terminology_control_table.csv` and `terminology_audit_findings.csv`: controlled
  vocabulary and contextual findings.
- `proposal_structure_map.md`: research-question and section mapping.
- `quality_control_report.md`: automated integrity, structure, citation, and
  terminology checks.
- `unresolved_issues.md`: limitations and decisions requiring later evidence or
  supervisory review.

## Rebuild and audit

Run from the repository root with a Python environment containing `python-docx`,
`lxml`, and `Pillow`:

```bash
python3 proposal_revision/generate_supporting_files.py
python3 proposal_revision/build_proposal.py \
  --source ../Doctoral_Dissertation_Proposal_PEI_Rongkang_BH_0704_Claude_tracked_revision2.docx \
  --out-dir proposal_revision \
  --work-dir proposal_revision/.build
python3 proposal_revision/run_quality_audits.py \
  --source ../Doctoral_Dissertation_Proposal_PEI_Rongkang_BH_0704_Claude_tracked_revision2.docx \
  --root proposal_revision \
  --accept-script /path/to/documents/scripts/accept_tracked_changes.py
```

Render both DOCX files with the Documents skill's `render_docx.py`, inspect every
page, and confirm that accepting revisions in the tracked copy reproduces the
clean copy before release. Rendered PNG/PDF files are QA intermediates and are not
versioned.

## Interpretation boundary

The revised proposal presents descriptive and associational analyses. Lagging,
event-history models, sequence analysis, and linked administrative records improve
temporal ordering and coverage; they do not identify causal effects or eliminate
selection and unobserved confounding.
