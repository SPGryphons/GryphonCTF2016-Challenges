# The Keymaker
Distribution files are located in the distrib folder.

## Details
The flag is encrypted with a 256-bit RSA key (both encrypted flag and public key provided in the distrib folder).

## Solution
To solve this, the user will have to reconstruct the private key from the public key file given. One solution is to factorize the 256-bit modulus "n" found in the public key to produce primes "p" and "q". With those the user will have to calculate the totient and private exponent d to reconstruct the private key. With the reconstructed private key, the user will then be able to decrypt the encrypted flag.

The solution program, `reconstructor_decode.py` uses a third-party program, msieve, to factorize very large prime numbers in a matter of minutes. Run `make all` in the msieve folder to build it. Configure "pub\_key\_file", "ciphertext\_file", and "msieve\_location" variables in `reconstructor_decode.py` to point to their various locations. Run with `./reconstructor_decode.py`.

