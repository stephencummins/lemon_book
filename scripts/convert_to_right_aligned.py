#!/usr/bin/env python3
"""
Convert page markers from arrow format to right-aligned format.
From: → X ←
To: <div align="right"><sub>X</sub></div>
"""

import re
import os

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

def convert_markers(content):
    """Convert arrow markers to right-aligned format"""
    # Pattern: → X ←
    pattern = r'→\s*([^←]+)\s*←'

    def replacement(match):
        page_num = match.group(1).strip()
        return f'<div align="right"><sub>{page_num}</sub></div>'

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

    # Count markers before
    before_count = len(re.findall(r'→\s*[^←]+\s*←', content))

    if before_count == 0:
        print(f"  ℹ️  No arrow markers found")
        return True

    # Convert markers
    new_content = convert_markers(content)

    # Count markers after
    after_count = len(re.findall(r'<div align="right"><sub>[^<]+</sub></div>', new_content))

    # Write back
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Converted {before_count} markers to right-aligned format")
        return True
    except Exception as e:
        print(f"  ❌ Error writing file: {e}")
        return False

def main():
    print("=" * 70)
    print("CONVERTING PAGE MARKERS TO RIGHT-ALIGNED FORMAT")
    print("=" * 70)
    print()

    success_count = 0
    for filename in CHAPTERS:
        if process_file(filename):
            success_count += 1

    print()
    print("=" * 70)
    print(f"✅ Successfully processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
