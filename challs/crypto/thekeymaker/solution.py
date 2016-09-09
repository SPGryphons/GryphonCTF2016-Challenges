#!/usr/bin/python3

# RSA Cracker
# Optixal

import subprocess, re, sys
from Crypto.PublicKey import RSA

pub_key_file = "pub_key_ctf.txt"
ciphertext_file = "ciphertext_ctf"
msieve_location = "~/Documents/repos/msieve-1.52/msieve"

print("[*] Starting RSA cracking...")
template = "{0:20}: {1:}"

# Public Key - Public Exponent (e), Modulus (n)

pub = RSA.importKey(open(pub_key_file, "r").read())
e = pub.e
n = pub.n
print("[+] Found public exponent e -", e)
print("[+] Found modulus n -", n)

# Factorization of n

print("[*] Factoring n... This might take a while...")
cmd = msieve_location + " -v " + str(pub.n)
output = subprocess.check_output(cmd, shell=True).decode("UTF-8").strip()

res = re.findall(r"p\d+ factor: (\d+)", output)
if not res:
    print("[-] Could not find prime factors p and q!")
    sys.exit(1)
print("[+] Found prime factors p and q!")
p = int(res[0])
q = int(res[1])
print()
print(template.format("Public Exponent e", e))
print(template.format("Modulus n", n))
print(template.format("Prime Factor p", p))
print(template.format("Prime Factor q", q))

# Totient (p - 1) * (q - 1)

totient = (p - 1) * (q - 1)
print(template.format("Totient φ(n)", totient))

# Mod Inverse e and φ(n)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Mod inverse not found!")
    else:
        return x % m

d = modinv(e, totient)
print(template.format("Private Exponent d", d))

# Reconstruct Private Key (n, e, d)

prv = RSA.construct((n, e, d))

# Decrypt Ciphertext

with open(ciphertext_file, "rb") as f:
    ciphertext = f.read()

plaintext = prv.decrypt(ciphertext)
try:
    plaintext = plaintext.decode("UTF-8")
except UnicodeDecodeError:
    print("[*] Could not decode plaintext to UTF-8, printing bytes instead")

print(template.format("Plaintext Obtained", plaintext))

print("\n[+] RSA Cracking Complete")
