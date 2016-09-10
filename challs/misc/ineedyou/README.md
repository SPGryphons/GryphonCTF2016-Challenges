# I Need You
Distribution file is located in the distrib folder.

## Details
A QR code with missing information, hint given: "The information you require **begins** with **'00010'**".

## Solution
To solve this, the user will have to have knowledge about the structure of QR codes. One way to solve this challenge is to use an image editor such as GIMP or Photoshop.

The solution in step by step order (solution .psd file is located in solution folder):
1. Determine the version of the QR code
  - Based on the given image, the QR code seems to be 33x33 pixels in size. With this we can calulate the version of this QR with the formula `(n - 21) / 4 + 1`
  - The result tells us that the QR code is version 4. Version 4 QR codes do not have version information bits in the QR code, and will only contain a single 5x5 alignment module.
2. Reconstruct the 3 position modules and single alignment alignment module (the big black squares with a border around them).
  - These modules are standard, place the 3 position modules flushed to the top-left, top-right and bottom-left.
  - Align the alignment module with the borders of the bottom-left and top-right position modules. It should be near the top-left of the bottom-right empty area.
3. Reconstruct the missing timing bits (an ant-trail) between the position modules.
4. Now the last bit of missing information seems to be the QR code's format information (on the edges of the position modules). We'll have to reconstruct this.
  - Based on the hint, "the information we require begins with '00010'". This is actually the first 5 bits of the missing format information.
  - We can lookup these partial bits online, "[Format and Version String Tables](http://www.thonky.com/qr-code-tutorial/format-version-tables "Format and Version String Tables")" seems to be a good reference for this purpose.
  - With the information given, there is only one format that begins with '00010', ECC level 'H', mask pattern 7. Full format string: 000100000111011
  - Now, we can reconstruct the format information.
5. Scan the QR code.
  - Since the error correction encoding level is set to 'H' for 'High', the QR code can handle up to 30% damage, therefore the missing data bits at the bottom-right of the QR code does not matter.
