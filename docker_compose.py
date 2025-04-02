version: '3.8'

services:
  qr-generator:
    build: .
    environment:
      - QR_DATA_URL=https://github.com/kaw393939
      - QR_CODE_DIR=/app/qr_codes
      - QR_CODE_FILENAME=github_qr.png
      - FILL_COLOR=black
      - BACK_COLOR=white
    volumes:
      - ./qr_codes:/app/qr_codes
