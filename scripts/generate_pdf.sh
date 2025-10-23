#!/bin/bash
# This script is a wrapper for the main build script.
# It ensures that the correct, modern build process is used.

echo "======================================================================"
echo "DEPRECATION WARNING: generate_pdf.sh is outdated."
echo "Redirecting to the primary build script: build_book.sh"
echo "======================================================================"
echo ""

./scripts/build_book.sh
