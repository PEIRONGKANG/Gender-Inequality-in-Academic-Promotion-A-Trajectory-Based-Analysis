# Dissertation Framework Build

The framework is generated from the retained proposal DOCX and the supplied
Tohoku University LaTeX thesis-template archive. Neither source is overwritten.

```bash
python3 framework_revision/build_framework.py \
  --source proposal_revision/Doctoral_Dissertation_Proposal_PEI_Rongkang_revised_tracked.docx \
  --school-template /Users/darin/Downloads/Tohoku_University_Thesis_Template__M_Sc____Ph_D__.zip \
  --out-dir framework_revision \
  --work-dir framework_revision/.build

python3 framework_revision/generate_supporting_files.py
```

The school-template path is intentionally external to Git. Its expected SHA-256
and the translated formatting rules are recorded in `tohoku_template_artifact.md`.
Render and inspect both generated DOCX files after every substantive or formatting
change.
