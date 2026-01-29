import csv
import glob
import json
import os
from json.decoder import JSONDecodeError

# ─── Constants ────────────────────────────────────
OUTPUT_DIR = os.path.join("static", "sampleresolver")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "jp_researchers.csv")
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

def process_file(file_path):
    """
    Process a single JSON file and extract researcher basic information.
    Returns a dictionary with researcher data.
    """
    data = load_json_safe(file_path)
    if not data:
        return None

    # Parse researcher basic information
    researcher = {
        "user_id": str(data.get("rm:user_id", "")),
        "creator_id": str(data.get("rm:creator_id", "")),
        "creator_type": str(data.get("rm:creator_type", "")),
        "created": str(data.get("rm:created", "")),
        "modifier_id": str(data.get("rm:modifier_id", "")),
        "modifier_type": str(data.get("rm:modifier_type", "")),
        "modified": str(data.get("rm:modified", "")),
        "context": str(data.get("@context", "")),
        "id": str(data.get("@id", "")),
        "type": str(data.get("@type", "")),
        "permalink": str(data.get("permalink", "")),
        "family_name_ja": str(data.get("family_name", {}).get("ja", "")),
        "family_name_ja_kana": str(data.get("family_name", {}).get("ja-Kana", "")),
        "family_name_en": str(data.get("family_name", {}).get("en", "")),
        "given_name_ja": str(data.get("given_name", {}).get("ja", "")),
        "given_name_ja_kana": str(data.get("given_name", {}).get("ja-Kana", "")),
        "given_name_en": str(data.get("given_name", {}).get("en", "")),
        "display_name_kana": str(data.get("display_name_kana", "")),
        "display_nickname": str(data.get("display_nickname", "")),
        "display_image": str(data.get("display_image", "")),
        "display_contact_pt": str(data.get("display_contact_point", "")),
        "display_profile": str(data.get("display_profile", "")),
        "display_url": str(data.get("display_url", ""))
    }

    return researcher

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = glob.glob(os.path.join(JSON_DIR, "*.json"))
    print(f"Found {len(files)} JSON files to process.")

    # CSV headers
    headers = [
        "user_id", "creator_id", "creator_type", "created", "modifier_id", "modifier_type",
        "modified", "context", "id", "type", "permalink", "family_name_ja", "family_name_ja_kana",
        "family_name_en", "given_name_ja", "given_name_ja_kana", "given_name_en", "display_name_kana",
        "display_nickname", "display_image", "display_contact_pt", "display_profile", "display_url"
    ]

    # Initialize CSV with headers
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

    count = 0
    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        
        for idx, file_path in enumerate(files):
            researcher = process_file(file_path)
            if researcher:
                writer.writerow(researcher)
                count += 1

            if (idx + 1) % 1000 == 0:
                print(f"Processed {idx + 1} files...")

    print(f"\n=== Processing Complete ===")
    print(f"Extracted {count} researcher records to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
