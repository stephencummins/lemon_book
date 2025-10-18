#!/bin/bash
# Direct Markdown to PDF converter using Pandoc + Chrome

if [ "$#" -lt 1 ]; then
    echo "Usage: ./md2pdf.sh <input.md> [output.pdf]"
    echo "Example: ./md2pdf.sh chapter1.md chapter1.pdf"
    exit 1
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.pdf}"
TEMP_HTML="${INPUT%.md}_temp.html"

echo "Converting $INPUT to $OUTPUT..."

# Step 1: Convert MD to HTML
pandoc "$INPUT" -o "$TEMP_HTML" --standalone --toc --toc-depth=2 --metadata title="$(basename ${INPUT%.md})" --resource-path=.:images --dpi=300

# Step 2: Convert HTML to PDF using Chrome (with print-quality settings)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless \
    --disable-gpu \
    --print-to-pdf="$OUTPUT" \
    --print-to-pdf-no-header \
    --no-margins \
    "file://$(pwd)/$TEMP_HTML"

# Clean up temp HTML
rm "$TEMP_HTML"

echo "✓ Created: $OUTPUT"
ls -lh "$OUTPUT"
