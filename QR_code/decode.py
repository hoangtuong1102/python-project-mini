import cv2
from pyzbar.pyzbar import decode


def decode_qr_code(filename):
    img = cv2.imread(filename)
    detect_barcodes = decode(img)

    if not detect_barcodes:
        print('No QR code detected.')
    else:
        for barcode in detect_barcodes:
            if barcode.data:
                print(barcode.data.decode('utf-8'))

if __name__ == '__main__':
    filename = 'qr_code.png'
    decode_qr_code(filename)

