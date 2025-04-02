import os
import qrcode
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_qr_code(data, output_dir='qr_codes', filename='github_qr.png', 
                    fill_color='black', back_color='white', box_size=10, border=4):
    """Generate QR code and save as PNG"""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    output_path = os.path.join(output_dir, filename)
    img.save(output_path)
    
    logger.info(f"QR code generated successfully at {output_path}")
    return output_path

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate QR Code')
    parser.add_argument('--url', type=str, help='URL for QR code')
    args = parser.parse_args()
    
    # Get values from environment variables with fallbacks
    qr_data = args.url or os.getenv('QR_DATA_URL', 'https://github.com/yeomigie')
    output_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
    filename = os.getenv('QR_CODE_FILENAME', 'github_qr.png')
    fill_color = os.getenv('FILL_COLOR', 'black')
    back_color = os.getenv('BACK_COLOR', 'white')
    
    # Generate the QR code
    generate_qr_code(
        data=qr_data,
        output_dir=output_dir,
        filename=filename,
        fill_color=fill_color,
        back_color=back_color
    )
