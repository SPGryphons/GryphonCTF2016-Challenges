#!/usr/bin/python3

# RSA Private Key Reconstructor
# Optixal

import subprocess, re, sys
from Crypto.PublicKey import RSA

msieve_location = "../msieve/msieve"
pub_key_file = "../distrib/pub_key.txt"
ciphertext_file = "../distrib/flag_ciphertext"

template = "{0:20}: {1:}"

# Public Key - Public Exponent (e), Modulus (n)
def readpub(pub_key_file):
    pub = RSA.importKey(open(pub_key_file, "r").read())
    e = pub.e
    n = pub.n
    print("[+] Found public exponent e -", e)
    print("[+] Found modulus n -", n)
    return e, n

# Factorization of n using msieve (requires msieve location)
def factor(n, msieve):
    if len(str(n)) > 310:
        print("[-] n is too large! n should be < 1024 bits.")
        sys.exit(1)

    print("[*] Factoring n... This might take a while...")
    cmd = msieve + " -v " + str(n)
    output = subprocess.check_output(cmd, shell=True).decode("UTF-8").strip()

    res = re.findall(r"p\d+ factor: (\d+)", output)
    if not res:
        print("[-] Could not find prime factors p and q!")
        sys.exit(1)
    print("[+] Found prime factors p and q!")
    p = int(res[0])
    q = int(res[1])
    return p, q

# Totient (p - 1) * (q - 1)
def totient(p, q):
    totient = (p - 1) * (q - 1)
    return totient

# Greates Common Denominator
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Mod Inverse e and φ(n)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Mod inverse not found!")
    else:
        return x % m

    return modinv(a, m)

# Print Findings
def compilation(e, n, p, q, t, d):
    print()
    print(template.format("Public Exponent e", e))
    print(template.format("Modulus n", n))
    print(template.format("Prime Factor p", p))
    print(template.format("Prime Factor q", q))
    print(template.format("Totient φ(n)", t))
    print(template.format("Private Exponent d", d))
    print()

# Decrypt Ciphertext
def decrypt(ciphertext_file, priv_key):
    with open(ciphertext_file, "rb") as f:
        ciphertext = f.read()

    plaintext = priv_key.decrypt(ciphertext)
    try:
        plaintext = plaintext.decode("UTF-8")
    except UnicodeDecodeError:
        pass

    return plaintext

def main():
    print("[*] Starting Reconstruction...\n")
    
    e, n = readpub(pub_key_file)
    p, q = factor(n, msieve_location)
    t = totient(p, q)
    d = modinv(e, t)
    compilation(e, n, p, q, t, d)
    
    prv = RSA.construct((n, e, d))
    plaintext = decrypt(ciphertext_file, prv)

    print("[+] Plaintext Obtained:", plaintext)

if __name__ == "__main__":
    main()

