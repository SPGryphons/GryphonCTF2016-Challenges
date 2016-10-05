import california

def main():
    print "Goodbye to my Santa Monica dream"

    # Check PIN
    pin = raw_input("Please enter your PIN: ").strip()
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
    pass_phrase = raw_input("Please enter the passphrase: ").strip()
    if california.mama(pass_phrase):
        print "Passphrase acccepted!"
    else:
        print "Passphrase invalid!"
        exit()

    # Print flag
    # I'm not sure how to do this yet...


if __name__ == "__main__":
    main()
