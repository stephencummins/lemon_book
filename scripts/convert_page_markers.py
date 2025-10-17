#!/usr/bin/env python3
"""
Script to convert HTML page markers to arrow format
From: <div align="center"><sub>X</sub></div>
To: → X ←
"""

import re
import os

# List of all chapter files
CHAPTERS = [
    "00_front_matter.md",
    "00_introduction.md",
    "01_enlightenment_roots_full.md",
    "02_classical_liberalism.md",
    "03_build_houses_full.md",
    "04_Pt1_mental_health_full.md",
    "04_Pt2_Reclaiming_Healthcare.md",
    "05_capitalism_conscience.md",
    "06_every_vote_counts.md",
    "07_europe_complicated.md",
    "08_immigration_conversations.md",
    "09_green_growth.md",
    "10_technology_good.md",
    "11_right_education.md",
    "12_your_rights_choices.md",
    "13_rights_modern_age.md",
    "14_tomorrows_tyranny.md",
    "15_guest_voices.md",
    "16_cooption_language.md",
    "17_reclaiming_liberalism.md",
    "18_liberal_lemonade.md",
]

def convert_page_markers(content):
    """Convert HTML page markers to arrow format"""
    # Pattern to match: <div align="center"><sub>X</sub></div>
    # Where X can be roman numerals (i, ii, iii, iv, v) or numbers
    pattern = r'<div align="center"><sub>([^<]+)</sub></div>'

    def replacement(match):
        page_num = match.group(1)
        return f'→ {page_num} ←'

    new_content = re.sub(pattern, replacement, content)
    return new_content

def process_file(filename):
    """Process a single file"""
    if not os.path.exists(filename):
        print(f"  ⚠️  File not found: {filename}")
        return False

    print(f"Processing {filename}...")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

    # Count how many markers we're converting
    original_count = len(re.findall(r'<div align="center"><sub>([^<]+)</sub></div>', content))

    if original_count == 0:
        print(f"  ℹ️  No HTML markers found")
        return True

    # Convert markers
    new_content = convert_page_markers(content)

    # Count new markers
    new_count = len(re.findall(r'→ ([^←]+) ←', new_content))

    # Write back
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Converted {original_count} markers to arrow format")
        return True
    except Exception as e:
        print(f"  ❌ Error writing file: {e}")
        return False

def main():
    print("=" * 70)
    print("CONVERTING PAGE MARKERS FROM HTML TO ARROW FORMAT")
    print("=" * 70)
    print()

    success_count = 0
    total_markers = 0

    for filename in CHAPTERS:
        if process_file(filename):
            success_count += 1

    print()
    print("=" * 70)
    print(f"✅ Successfully processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
