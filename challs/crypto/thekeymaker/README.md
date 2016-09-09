# The Keymaker
Distribution files are located in the distrib folder.

## Details
The flag is encrypted with a 256-bit RSA key (both provided in the distrib folder).

## Solution
The user will have to devise a solution to reconstruct the private key from the public key file given. One solution is to factorize 256-bit modulus n found in the public key to become primes p and q, with those calculate totient, and private exponent d to reconstruct private key. With reconstructed private key, decrypt flag.

The solution program, `solution.py` uses a third-party program, msieve, to factorize very large prime numbers in a matter of minutes. Run `make all` in the msieve folder to install. Configure "pub_key\_file", "ciphertext\_file", and "msieve\_location" variables in `solution.py` to point to their various locations. Run with `./solution.py`.

