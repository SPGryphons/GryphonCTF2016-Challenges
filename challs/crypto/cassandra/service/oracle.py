#!/usr/bin/python

from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib
import sys
import os

BLOCK_SIZE = 16  # AES-128 is super effective

def write(data, sep="\n"):
    sys.stdout.write(data + sep)
    sys.stdout.flush()

def str_to_bin(data):
    return "".join([bin(ord(i))[2:].rjust(8, "0") for i in data])

def bin_to_str_padded(data):
    padding_len = (8 - (len(data) % 8))
    if padding_len != 8:
        data = data + padding_len * "0"
    return "".join([chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8)])

def permute_iv(iv):
    return hashlib.sha256(iv).digest()[:BLOCK_SIZE]

def pad_message(message):
    padding_len = (BLOCK_SIZE - (len(message) % BLOCK_SIZE))
    if padding_len != BLOCK_SIZE:
        message = message + padding_len * "\x00"
    return message

FLAG = file("/home/oracleuser/flag").read().strip()
assert len(FLAG) <= BLOCK_SIZE
FLAG = str_to_bin(FLAG)

KEY = os.urandom(BLOCK_SIZE)

def validate(data):
    for i in data:
        if i != "0" and i != "1":
            return False
    return True

def foresee(iv, desire):
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    data = bin_to_str_padded(desire + FLAG)
    message = pad_message(data)
    return aes.encrypt(message)

def main():
    iv = os.urandom(BLOCK_SIZE)
    write("Welcome to the Seer's Stone.")
    write("I have planted the seed: %s" % iv.encode("hex"))
    while True:
        write("What is your heart's desire: ", sep="")
        desire = sys.stdin.readline().strip()
        if validate(desire):
            blocks = foresee(iv, desire)
            write("I see... %s" % blocks.encode("hex"))
        else:
            write("Danger lies in your future.")
            exit()
        iv = permute_iv(iv)

if __name__ == "__main__":
    main()
