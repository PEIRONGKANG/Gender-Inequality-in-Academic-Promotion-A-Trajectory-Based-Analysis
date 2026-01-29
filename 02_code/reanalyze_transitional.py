import json
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parents[1]
INPUT_XLSX = BASE.parent / "Full Process Analysis_01" / "回归分析过程" / "data_input" / "学者任职全路径_transitional.xlsx"
OUTPUT_DIR = BASE / "03_results" / "tables"
LOG_DIR = BASE / "04_logs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


def _standardize_gender(series: pd.Series) -> pd.Series:
    mapping = {
        "M": "Male",
        "Male": "Male",
        "F": "Female",
        "Female": "Female",
    }
    return series.map(mapping)


def main() -> None:
    df = pd.read_excel(INPUT_XLSX, sheet_name="dr-ap-fp")

    df["gender_std"] = _standardize_gender(df["gender"])

    # Overall counts
    overall_counts = df["gender_std"].value_counts(dropna=False).rename_axis("gender").reset_index(name="count")
    overall_counts.to_csv(OUTPUT_DIR / "overall_gender_counts.csv", index=False)

    # Stage definitions
    stages = {
        "stage1": "doctor_to_ap",
        "stage2": "ap_to_fp",
    }

    summary_rows = []
    for stage_name, col in stages.items():
        observed = df[col].notna()
        non_negative = observed & (df[col] >= 0)

        # Observability counts
        obs_counts = df.loc[observed, "gender_std"].value_counts(dropna=False)
        nn_counts = df.loc[non_negative, "gender_std"].value_counts(dropna=False)

        for gender, count in obs_counts.items():
            summary_rows.append(
                {
                    "stage": stage_name,
                    "subset": "observed",
                    "gender": gender,
                    "n": int(count),
                }
            )
        for gender, count in nn_counts.items():
            summary_rows.append(
                {
                    "stage": stage_name,
                    "subset": "non_negative",
                    "gender": gender,
                    "n": int(count),
                }
            )

        # Duration summaries (non-negative)
        for gender in ["Female", "Male"]:
            gmask = non_negative & (df["gender_std"] == gender)
            series = df.loc[gmask, col]
            if series.empty:
                continue
            summary_rows.append(
                {
                    "stage": stage_name,
                    "subset": "non_negative",
                    "gender": gender,
                    "metric": "mean",
                    "value": float(series.mean()),
                }
            )
            summary_rows.append(
                {
                    "stage": stage_name,
                    "subset": "non_negative",
                    "gender": gender,
                    "metric": "median",
                    "value": float(series.median()),
                }
            )

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(OUTPUT_DIR / "stage_summary_counts_and_stats.csv", index=False)

    # High-level JSON summary for quick reference
    summary_json = {
        "total_records": int(len(df)),
        "gender_counts": overall_counts.to_dict(orient="records"),
        "stage_counts": summary_df[summary_df["metric"].isna()].to_dict(orient="records"),
        "stage_stats": summary_df[summary_df["metric"].notna()].to_dict(orient="records"),
    }
    (OUTPUT_DIR / "summary.json").write_text(json.dumps(summary_json, indent=2), encoding="utf-8")

    # Log basic run info
    LOG_DIR.joinpath("run_info.txt").write_text(
        "Input: {}\nRows: {}\n".format(INPUT_XLSX, len(df)),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
