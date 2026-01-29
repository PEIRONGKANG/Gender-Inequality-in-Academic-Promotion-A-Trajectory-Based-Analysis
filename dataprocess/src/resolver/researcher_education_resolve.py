import os
import csv
import glob
import json
from json.decoder import JSONDecodeError

import pandas as pd

# ─── Constants ────────────────────────────────────
OUTPUT_DIR = os.path.join("static", "sampleresolver")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "jp_researchers_education.csv")
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

    education_graph = next((g for g in data.get("@graph", []) if g.get("@type") == "education"), None)
    if education_graph is None:
        return None

    education_records = []
    for item in education_graph.get("items", []):
        rm_id = str(item.get("rm:id", "")).strip()
        
        affiliation_info = item.get("affiliation", {})
        department_info = item.get("department", {})
        course_info = item.get("course", {})

        record = {
            "researcher_user_id": str(item.get("rm:user_id", "")),
            "rm_id": rm_id,
            "display": str(item.get("display", "")),
            "major_achievement": 1 if item.get("major_achievement") else 0,
            "creator_id": str(item.get("rm:creator_id", "")),
            "creator_type": str(item.get("rm:creator_type", "")),
            "created": str(item.get("rm:created", "")),
            "modifier_id": str(item.get("rm:modifier_id", "")),
            "modifier_type": str(item.get("rm:modifier_type", "")),
            "modified": str(item.get("rm:modified", "")),
            "from_date": str(item.get("from_date", "")),
            "to_date": str(item.get("to_date", "")),
            "rm_institution_code": str(item.get("rm:institution_code", "")),
            "affiliation_ja": str(affiliation_info.get("ja", "")),
            "affiliation_en": str(affiliation_info.get("en", "")),
            "department_ja": str(department_info.get("ja", "")),
            "department_en": str(department_info.get("en", "")),
            "course_ja": str(course_info.get("ja", "")),
            "course_en": str(course_info.get("en", "")),
            "address_country": str(item.get("address_country", "")),
        }
        education_records.append(record)

    return education_records

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = glob.glob(os.path.join(JSON_DIR, "*.json"))
    print(f"Found {len(files)} JSON files.")

    # Headers for CSV
    headers = [
        "researcher_user_id", "rm_id", "display", "major_achievement", "creator_id",
        "creator_type", "created", "modifier_id", "modifier_type", "modified",
        "from_date", "to_date", "rm_institution_code", "affiliation_ja",
        "affiliation_en", "department_ja", "department_en", "course_ja",
        "course_en", "address_country"
    ]

    # Initialize CSV with headers
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

    print(f"Processing complete. extracted {count} records to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()