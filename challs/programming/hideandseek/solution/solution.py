#!/usr/bin/python3

from PIL import Image
import zbarlight

challenge_location = "../distrib/f1d9cfca11cd971e2e41fce28d49b226.png"
qr_size = 33

def readqr(img):
    # Resize due to zbarlight requirement for 66x66 minimum QR code size
    img = img.resize((66, 66))
    codes = zbarlight.scan_codes('qrcode', img)
    try:
        print(codes[0].decode("UTF-8"))
    except TypeError:
        pass
    img.close()

def splitqr(img):
    for h in range(int(img.height / qr_size)):
        for w in range(int(img.width / qr_size)):
            qr_img = img.crop((w * qr_size, h * qr_size, w * qr_size + qr_size, h * qr_size + qr_size))
            readqr(qr_img)
            qr_img.close()

def main():
    with open(challenge_location, 'rb') as image_file:
        challenge = Image.open(image_file)
        challenge.load()
    
    splitqr(challenge)
    challenge.close()

if __name__ == "__main__":
    main()
