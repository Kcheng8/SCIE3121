#!/usr/bin/env python3
"""
QR Code Generator for Alphavirus Research Website
This script generates QR codes for the detail pages.

Usage:
    python3 generate_qr_codes.py
"""

import os
try:
    import qrcode
except ImportError:
    print("Installing required package: qrcode")
    os.system("pip install qrcode[pil]")
    import qrcode

def generate_qr_codes(base_url="http://localhost:8000"):
    """
    Generate QR codes for all detail pages.
    
    Args:
        base_url: The base URL where the website will be hosted
                 Default is localhost for local testing
    """
    
    # Create qr_codes directory if it doesn't exist
    qr_dir = "qr_codes"
    if not os.path.exists(qr_dir):
        os.makedirs(qr_dir)
        print(f"Created directory: {qr_dir}")
    
    # Define pages and their URLs
    pages = {
        'background': f'{base_url}/background.html',
        'methods': f'{base_url}/methods.html',
        'results': f'{base_url}/results.html',
        'future': f'{base_url}/future.html'
    }
    
    # Generate QR code for each page
    for page_name, url in pages.items():
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code
        filename = f'{qr_dir}/{page_name}_qr.png'
        img.save(filename)
        print(f'✓ Created: {filename} -> {url}')
    
    print("\nQR codes generated successfully!")
    print(f"\nTo use these QR codes:")
    print("1. Update the base_url if deploying to a different host")
    print("2. Re-run this script with your final URL")
    print("3. The QR codes will automatically work with the HTML page")

if __name__ == "__main__":
    import sys
    
    base_url = "http://localhost:8000"
    
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    
    print(f"Generating QR codes for: {base_url}")
    print("=" * 50)
    
    generate_qr_codes(base_url)
