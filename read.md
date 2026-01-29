# GitHub Package (Nature-style layout)

This folder contains a minimal re-analysis based on `Full Process Analysis_01/回归分析过程/data_input/学者任职全路径_transitional.xlsx`.
The outputs are organized in a journal-style layout (data input, code, results tables/figures, logs).

## Structure
- `github/01_data_input/`: Reserved for input metadata or links (no data copied).
- `github/02_code/`: Re-analysis code.
- `github/03_results/tables/`: Derived tables and summaries.
- `github/03_results/figures/`: Placeholder for figures (not generated in this pass).
- `github/04_logs/`: Run logs.

## Re-analysis outputs
Generated from sheet `dr-ap-fp` of the transitional dataset.

Tables:
- `github/03_results/tables/overall_gender_counts.csv`
- `github/03_results/tables/stage_summary_counts_and_stats.csv`
- `github/03_results/tables/summary.json`

Code:
- `github/02_code/reanalyze_transitional.py`

Logs:
- `github/04_logs/run_info.txt`

## How to run
```bash
python3 github/02_code/reanalyze_transitional.py
```

## Notes
- Gender is standardized to `Male`/`Female` from `M/F/Male/Female`.
- Stage 1 uses `doctor_to_ap`; Stage 2 uses `ap_to_fp`.
- Counts are reported for observed durations and for non-negative durations.

## Data Availability
Only aggregated summary tables and analysis code are公开. Individual-level data are not shared.
