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
  "18_Conclusion.md"
  "bibliography.md"
  "book_index_with_pages.md"
  "colophon.md"
)

echo "📚 Assembling markdown files..."

# --- Generate PDF (using MacTeX/XeLaTeX) ---
echo "📄 Generating PDF..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_PDF" \
  --metadata-file "$SCRIPT_DIR/metadata.yaml" \
  --from markdown+smart+raw_tex \
  --resource-path=.:images \
  --pdf-engine=/Library/TeX/texbin/xelatex

echo "✅ Created $OUTPUT_PDF ($(du -h "$OUTPUT_PDF" | cut -f1))"

# --- Generate EPUB ---
echo "📱 Generating EPUB..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_EPUB" \
  --metadata-file "$SCRIPT_DIR/metadata.yaml" \
  --from markdown+smart \
  --resource-path=.:images \
  --toc --toc-depth=2

echo "✅ Created $OUTPUT_EPUB ($(du -h "$OUTPUT_EPUB" | cut -f1))"

# --- Generate DOCX ---
echo "📝 Generating DOCX..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_DOCX" \
  --metadata-file "$SCRIPT_DIR/metadata.yaml" \
  --from markdown+smart \
  --resource-path=.:images \
  --toc --toc-depth=2

echo "✅ Created $OUTPUT_DOCX ($(du -h "$OUTPUT_DOCX" | cut -f1))"

# --- Generate HTML ---
echo "🌐 Generating HTML..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_HTML" \
  --metadata-file "$SCRIPT_DIR/metadata.yaml" \
  --from markdown+smart \
  --resource-path=.:images \
  --standalone --toc --toc-depth=2 \
  --css=style.css

echo "✅ Created $OUTPUT_HTML ($(du -h "$OUTPUT_HTML" | cut -f1))"

# --- Generate RTF ---
echo "📋 Generating RTF..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_RTF" \
  --metadata-file "$SCRIPT_DIR/metadata.yaml" \
  --from markdown+smart \
  --resource-path=.:images

echo "✅ Created $OUTPUT_RTF ($(du -h "$OUTPUT_RTF" | cut -f1))"

# --- Generate ODT ---
echo "📄 Generating ODT..."
pandoc "${CHAPTERS[@]}" \
  -o "$OUTPUT_ODT" \
  --metadata-file "$SCRIPT_DIR/metadata.yaml" \
  --from markdown+smart \
  --resource-path=.:images \
  --toc --toc-depth=2

echo "✅ Created $OUTPUT_ODT ($(du -h "$OUTPUT_ODT" | cut -f1))"

echo ""
echo "🎉 Build complete! Generated files:"
ls -lh "$OUTPUT_PDF" "$OUTPUT_EPUB" "$OUTPUT_DOCX" "$OUTPUT_HTML" "$OUTPUT_RTF" "$OUTPUT_ODT"

# --- Upload to Cloudflare R2 ---
UPLOAD_TO_R2="${UPLOAD_TO_R2:-false}"

if [[ "$UPLOAD_TO_R2" == "true" ]]; then
  if command -v wrangler &> /dev/null; then
    echo ""
    echo "📤 Uploading to Cloudflare R2..."

    wrangler r2 object put "lemon-book/book/$OUTPUT_PDF" --file="$OUTPUT_PDF" --content-type="application/pdf" --remote
    wrangler r2 object put "lemon-book/book/$OUTPUT_EPUB" --file="$OUTPUT_EPUB" --content-type="application/epub+zip" --remote
    wrangler r2 object put "lemon-book/book/$OUTPUT_DOCX" --file="$OUTPUT_DOCX" --content-type="application/vnd.openxmlformats-officedocument.wordprocessingml.document" --remote
    wrangler r2 object put "lemon-book/book/$OUTPUT_HTML" --file="$OUTPUT_HTML" --content-type="text/html" --remote
    wrangler r2 object put "lemon-book/book/$OUTPUT_RTF" --file="$OUTPUT_RTF" --content-type="application/rtf" --remote
    wrangler r2 object put "lemon-book/book/$OUTPUT_ODT" --file="$OUTPUT_ODT" --content-type="application/vnd.oasis.opendocument.text" --remote

    echo "✅ All files uploaded to Cloudflare R2!"
    echo "📍 Location: lemon-book/book/"
  else
    echo ""
    echo "⚠️  Wrangler not found. Cannot upload to Cloudflare R2."
    echo "   Install with: npm install -g wrangler"
    exit 1
  fi
fi

echo ""
echo "🍋 The Lemon Book build complete!"