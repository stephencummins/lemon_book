#!/bin/bash
# Add page breaks after page number markers and at end of chapters

PAGE_BREAK='<div style="page-break-after: always;"></div>'

for file in *.md; do
    # Skip generated files
    if [[ "$file" == "Complete_Lemon_Book.md" ]] || [[ "$file" == "clean_book.md" ]]; then
        continue
    fi
    
    echo "Processing $file..."
    
    # Create backup
    cp "$file" "$file.bak"
    
    # Add page break after each page number marker
    # Pattern: <div align="right"><sub>NUMBER</sub></div>
    # Replace with: <div align="right"><sub>NUMBER</sub></div>\n<div style="page-break-after: always;"></div>
    sed -i '' 's|<div align="right"><sub>\([0-9]*\)</sub></div>|<div align="right"><sub>\1</sub></div>\n'"$PAGE_BREAK"'|g' "$file"
    
    # Add page break at the end of the file if not already there
    if ! tail -1 "$file" | grep -q "page-break-after"; then
        echo "" >> "$file"
        echo "$PAGE_BREAK" >> "$file"
    fi
    
    echo "✓ Added page breaks to $file"
done

echo ""
echo "Done! Backup files saved as *.md.bak"
