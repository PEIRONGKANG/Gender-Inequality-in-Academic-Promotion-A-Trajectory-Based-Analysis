import os
import csv
import glob
import json
from json.decoder import JSONDecodeError

import pandas as pd

# ─── Constants ────────────────────────────────────
OUTPUT_DIR = os.path.join("static", "sampleresolver")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "jp_researchers_degrees.csv")
JSON_DIR = os.path.join("static", "sample")

def load_json_safe(fp):
    """Safely load JSON, skipping empty or malformed files."""
    if os.path.getsize(fp) == 0:
        return None
    try:
        with open(fp, "r", encoding="utf-8") as f:
            return json.load(f)
    except JSONDecodeError as e:
        print(f"JSON decode error in {fp}: {e}")
        return None

def process_file(fp):
    data = load_json_safe(fp)
    if not data:
        return None

    researcher_user_id = str(data.get("rm:user_id", "")).strip()
    if not researcher_user_id:
        return None

    degrees_data = data.get("degrees", [])
    if not degrees_data:
        return None

    degrees = []
    for degree_item in degrees_data:
        degree_info = degree_item.get("degree", {})
        degree_institution_info = degree_item.get("degree_institution", {})
        
        record = {
            "researcher_user_id": researcher_user_id,
            "degree_ja": str(degree_info.get("ja", "")),
            "degree_en": str(degree_info.get("en", "")),
            "degree_institution_ja": str(degree_institution_info.get("ja", "")),
            "degree_institution_en": str(degree_institution_info.get("en", "")),
            "degree_date": str(degree_item.get("degree_date", "")),
            "display_degree": str(degree_item.get("display_degree", "")),
            "rm_institution_code": str(degree_item.get("rm:institution_code", "")),
        }
        degrees.append(record)

    return degrees

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = glob.glob(os.path.join(JSON_DIR, "*.json"))
    print(f"Found {len(files)} JSON files.")

    headers = [
        "researcher_user_id", "degree_ja", "degree_en", "degree_institution_ja",
        "degree_institution_en", "degree_date", "display_degree", "rm_institution_code"
    ]

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

    count = 0
    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        for fp in files:
            records = process_file(fp)
            if records:
                writer.writerows(records)
                count += len(records)
            
            if (files.index(fp) + 1) % 1000 == 0:
                print(f"Processed {files.index(fp) + 1} files...")

    print(f"Processing complete. Extracted {count} records to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()