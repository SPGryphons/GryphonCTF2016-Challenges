import california
import hashlib

def main():
    print "Goodbye to my Santa Monica dream"

    # Check PIN
    pin = "73313"
    if not pin.isdigit():
        print "PINs don't have non-digits!"
        exit()

    pin = int(pin)

    if california.dreams(pin):
        print "PIN Accepted!"
    else:
        print "PIN Invalid!"
        exit()

    # Check pass phrase
    pass_phrase = "Be Sure To Wear Flowers In Your Hair"
    if california.mama(pass_phrase):
        print "Passphrase acccepted!"
    else:
        print "Passphrase invalid!"
        exit()

    # Print flag
    print california.papa(hashlib.md5(pass_phrase).digest())


if __name__ == "__main__":
    main()
