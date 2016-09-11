#!/usr/bin/python3

import pyqrcode, sys, string, random, os, shutil, numpy as np
from PIL import Image

design_location = "../lib/design.txt"
blank_img_location = "../lib/blank.png"
qr_dump_folder = "../qr_dump/"
final_chall_file = "../distrib/hideandseek.png"

qr_filename_template = "{0}_{1}"
fake_flag_template = "GG{0:2}{{{1:19}}}"
actual_flag = "GCTF{w3_h4v3_f0und_y0u_!}"

idv_size = 33

img_locations = []

design = list(list(config.strip().split(",")) for config in open(design_location, "r") if config.strip())
design = list(list(int(i) for i in line) for line in design)

def genqr(s, filename):
    qr = pyqrcode.create(s)
    qr.png(filename, scale=1, quiet_zone=0)

def genfakeflag():
    return fake_flag_template.format(''.join(random.choice(string.ascii_uppercase) for i in range(2)), ''.join(random.choice("_" + string.ascii_lowercase + string.ascii_uppercase +  string.digits) for i in range(19)))

def genblock(digit, r, c):
    if digit == 0:
    # Returns a Blank Block
        shutil.copyfile(blank_img_location, qr_dump_folder + qr_filename_template.format(r, c))
    elif digit == 1:
    # Generate a Random QR Block with Fake Flag
        genqr(genfakeflag(), qr_dump_folder + qr_filename_template.format(r, c))
    elif digit == 2:
    # Generate the QR Block with the Real Flag
        genqr(actual_flag, qr_dump_folder + qr_filename_template.format(r, c))
    else:
        print("[-] Invalid digit found in design file")
        sys.exit(1)

def genrow(row, r):
    row_locations = []
    for i in range(len(row)):
        genblock(row[i], r, i)
        row_locations.append(qr_dump_folder + qr_filename_template.format(r, i))
    img_locations.append(row_locations)

def genfinalimg():
    # Read those QR Codes and Join Them
    print("[*] Generating final image by combining QR codes... ", end='')
    img = list(list(Image.open(n) for n in row) for row in img_locations)
    canvas = Image.new("RGB", (idv_size * len(img[0]), idv_size * len(img)))
    
    for r in range(len(img)):
        for i in range(len(img[r])):
            canvas.paste(img[r][i], (i * idv_size, r * idv_size))
    
    canvas.save(final_chall_file)
    print("Done!")

def genqrcodes():
    # Generate QR Codes and Save to Disk
    print("[*] Generating QR codes and saving them... ", end='')
    for i in range(len(design)):
        genrow(design[i], i)
    print("Done!")

def main():
    print("[*] Generating challenge...\n")
    genqrcodes()
    genfinalimg()
    print("\n[+] Successfully generated challenge!")

if __name__ == "__main__":
    main()
