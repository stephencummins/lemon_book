#!/usr/bin/env python3
"""
Upscale book images to 300 DPI for Lulu print requirements.

This script uses Real-ESRGAN for AI-powered upscaling to achieve
print-quality resolution (300 DPI) from 72 DPI source images.

Target: 6"x9" book pages at 300 DPI = 1800x2700 pixels
"""

import os
import sys
from pathlib import Path
from PIL import Image

# Check if basicsr and realesrgan are available
try:
    from basicsr.archs.rrdbnet_arch import RRDBNet
    from realesrgan import RealESRGANer
    import torch
    REALESRGAN_AVAILABLE = True
except ImportError:
    REALESRGAN_AVAILABLE = False
    print("⚠️  Real-ESRGAN not installed. Install with:")
    print("   pip install realesrgan basicsr")
    print("\nFalling back to high-quality bicubic upscaling...")

# Configuration
INPUT_DIR = Path(__file__).parent.parent / "images"
OUTPUT_DIR = Path(__file__).parent.parent / "images_print"
SCALE_FACTOR = 4  # 4x upscaling (72 DPI → 288 DPI, close to 300)
TARGET_DPI = 300

def setup_realesrgan():
    """Initialize Real-ESRGAN upscaler."""
    if not REALESRGAN_AVAILABLE:
        return None

    print("🔧 Initializing Real-ESRGAN...")

    # Use RealESRGAN_x4plus model (best for general images)
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)

    # Determine device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    if device == 'cpu':
        print("⚠️  Running on CPU (slower). For faster processing, install CUDA-enabled PyTorch.")
    else:
        print(f"✅ Using GPU: {torch.cuda.get_device_name(0)}")

    # Initialize upscaler
    upscaler = RealESRGANer(
        scale=4,
        model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth',
        model=model,
        tile=400,  # Adjust if running out of memory
        tile_pad=10,
        pre_pad=0,
        half=False if device == 'cpu' else True,  # FP16 for GPU
        device=device
    )

    return upscaler

def upscale_with_realesrgan(upscaler, input_path, output_path):
    """Upscale image using Real-ESRGAN."""
    import cv2
    import numpy as np

    # Read image
    img = cv2.imread(str(input_path), cv2.IMREAD_UNCHANGED)

    # Upscale
    output, _ = upscaler.enhance(img, outscale=4)

    # Save with PIL to add DPI metadata
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(output_rgb)
    pil_img.save(output_path, dpi=(TARGET_DPI, TARGET_DPI), optimize=False)

    return pil_img.size

def upscale_with_pillow(input_path, output_path):
    """Fallback: High-quality bicubic upscaling with Pillow."""
    img = Image.open(input_path)

    # Calculate new size
    new_width = img.width * SCALE_FACTOR
    new_height = img.height * SCALE_FACTOR

    # Upscale using Lanczos (highest quality)
    upscaled = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Save with 300 DPI metadata
    upscaled.save(output_path, dpi=(TARGET_DPI, TARGET_DPI), optimize=False)

    return upscaled.size

def process_images():
    """Process all PNG images in the input directory."""

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Get all PNG images
    images = sorted(INPUT_DIR.glob("*.png"))

    if not images:
        print(f"❌ No PNG images found in {INPUT_DIR}")
        return

    print(f"\n📁 Input:  {INPUT_DIR}")
    print(f"📁 Output: {OUTPUT_DIR}")
    print(f"🎯 Target: {TARGET_DPI} DPI (Lulu print standard)")
    print(f"\n🖼️  Found {len(images)} images to upscale\n")

    # Initialize upscaler
    upscaler = setup_realesrgan() if REALESRGAN_AVAILABLE else None

    # Process each image
    for i, img_path in enumerate(images, 1):
        print(f"[{i}/{len(images)}] Processing: {img_path.name}")

        # Load original to get info
        original = Image.open(img_path)
        original_size = original.size
        original_dpi = original.info.get('dpi', (72, 72))

        output_path = OUTPUT_DIR / img_path.name

        try:
            if upscaler:
                # Use Real-ESRGAN
                new_size = upscale_with_realesrgan(upscaler, img_path, output_path)
            else:
                # Use Pillow fallback
                new_size = upscale_with_pillow(img_path, output_path)

            # Get file sizes
            original_size_mb = img_path.stat().st_size / (1024 * 1024)
            new_size_mb = output_path.stat().st_size / (1024 * 1024)

            print(f"  ✅ {original_size[0]}x{original_size[1]} @ {original_dpi[0]:.0f} DPI → {new_size[0]}x{new_size[1]} @ {TARGET_DPI} DPI")
            print(f"     Size: {original_size_mb:.1f} MB → {new_size_mb:.1f} MB")

        except Exception as e:
            print(f"  ❌ Error: {e}")
            continue

        print()

    print("=" * 80)
    print("✨ Upscaling complete!")
    print(f"\n📊 Results:")
    print(f"   - Upscaled images saved to: {OUTPUT_DIR}")
    print(f"   - Resolution: {TARGET_DPI} DPI (Lulu print-ready)")
    print(f"   - Scale factor: {SCALE_FACTOR}x")
    print(f"\n💡 Next steps:")
    print(f"   1. Review upscaled images in {OUTPUT_DIR}")
    print(f"   2. Replace images in your book source")
    print(f"   3. Regenerate PDF for Lulu print")

if __name__ == "__main__":
    print("=" * 80)
    print("🍋 LEMON BOOK - IMAGE UPSCALER FOR PRINT")
    print("=" * 80)

    process_images()
