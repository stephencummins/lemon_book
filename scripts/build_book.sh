#!/bin/bash

# The Lemon Book - Complete Build Script
# This script generates The Lemon Book in multiple formats and optionally uploads to Cloudflare R2

set -e # Exit immediately if a command exits with a non-zero status.

echo "🍋 Starting build for The Lemon Book..."

# --- Configuration ---
BASE_NAME="lemon_book"
OUTPUT_PDF="${BASE_NAME}.pdf"
OUTPUT_EPUB="${BASE_NAME}.epub"
OUTPUT_DOCX="${BASE_NAME}.docx"
OUTPUT_HTML="${BASE_NAME}.html"
OUTPUT_RTF="${BASE_NAME}.rtf"
OUTPUT_ODT="${BASE_NAME}.odt"

# Get the directory where the script is located
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Change to the parent directory (where the markdown files are)
cd "$SCRIPT_DIR/.."

# --- File Assembly Order ---
# This order is based on PDF_BUILD_ORDER.md
CHAPTERS=(
  "00_front_matter.md"
  "00_introduction.md"
  "01_enlightenment_roots.md"
  "02_classical_liberalism.md"
  "03_build_houses_full.md"
  "04_Pt1_mental_health_full.md"
  "04_Pt2_Reclaiming_Healthcare.md"
  "05_capitalism_conscience.md"
  "06_every_vote_counts.md"
  "07_europe_complicated.md"
  "08_immigration_conversations.md"
  "09_green_growth.md"
  "10_technology_good.md"
  "11_right_education.md"
  "12_your_rights_choices.md"
  "13_rights_modern_age.md"
  "14_tomorrows_tyranny.md"
  "15_guest_voices.md"
  "16_cooption_language.md"
  "17_reclaiming_liberalism.md"
  "18_liberal_lemonade.md"
  "book_index_with_pages.md"
  "colophon.md"
)

echo "📚 Assembling markdown files..."

# --- Generate PDF (using MacTeX/XeLaTeX) ---
echo "📄 Generating PDF..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_PDF" \
  --metadata-file metadata.yaml \
  --from markdown+smart+raw_tex \
  --resource-path=.:images \
  --template custom-template.latex \
  --pdf-engine=xelatex

echo "✅ Successfully created $OUTPUT_PDF"
echo "Build complete."