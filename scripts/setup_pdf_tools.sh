#!/bin/bash
# Setup script for PDF generation tools
# This installs MacTeX (no GUI) and other necessary tools for generating print-quality PDFs

set -e

echo "========================================================================"
echo "🍋 LEMON BOOK - PDF TOOLS SETUP"
echo "========================================================================"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Please install it first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

echo "✅ Homebrew found"
echo ""

# Install MacTeX (no GUI version - smaller download)
echo "📦 Installing MacTeX (no GUI)..."
echo "   This is ~100MB vs 4GB for full MacTeX"
echo ""

if command -v xelatex &> /dev/null; then
    echo "✅ XeLaTeX already installed"
else
    echo "Installing mactex-no-gui..."
    brew install --cask mactex-no-gui

    # Add TeX to PATH for current session
    export PATH="/Library/TeX/texbin:$PATH"

    echo ""
    echo "⚠️  IMPORTANT: Add this to your ~/.zshrc or ~/.bash_profile:"
    echo "   export PATH=\"/Library/TeX/texbin:\$PATH\""
    echo ""
fi

# Install Pandoc
echo "📦 Installing Pandoc..."
if command -v pandoc &> /dev/null; then
    echo "✅ Pandoc already installed ($(pandoc --version | head -1))"
else
    brew install pandoc
fi

# Install Python PDF tools (optional but recommended)
echo ""
echo "📦 Installing Python PDF tools (WeasyPrint)..."
echo "   This provides better print quality than Chrome"
echo ""

if python3 -c "import weasyprint" 2>/dev/null; then
    echo "✅ WeasyPrint already installed"
else
    pip3 install weasyprint markdown
fi

# Verify installations
echo ""
echo "========================================================================"
echo "🔍 VERIFICATION"
echo "========================================================================"
echo ""

if command -v xelatex &> /dev/null; then
    echo "✅ XeLaTeX: $(xelatex --version | head -1)"
else
    echo "❌ XeLaTeX not found"
fi

if command -v pandoc &> /dev/null; then
    echo "✅ Pandoc: $(pandoc --version | head -1)"
else
    echo "❌ Pandoc not found"
fi

if python3 -c "import weasyprint" 2>/dev/null; then
    echo "✅ WeasyPrint: installed"
else
    echo "⚠️  WeasyPrint not installed (optional)"
fi

echo ""
echo "========================================================================"
echo "✨ SETUP COMPLETE"
echo "========================================================================"
echo ""
echo "You can now generate PDFs using:"
echo "  1. bash scripts/generate_pdf.sh (uses pandoc + XeLaTeX)"
echo "  2. python3 scripts/generate_print_pdf.py (uses WeasyPrint)"
echo ""
echo "⚠️  Remember to restart your terminal or run:"
echo "   export PATH=\"/Library/TeX/texbin:\$PATH\""
echo ""
