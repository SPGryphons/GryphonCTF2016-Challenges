# Dirty Bird
This challenge requires searching on social media.

## Question Text
You found a dirty ol' square piece of black paper with a QR code on it, naturally, you become curious... Should you scan it? Image file located in distrib folder.

## Solution
The QR code produces a large number after scanning it, "234469727479426972647341726531333337". It is actually a hex representation of an ASCII string "#DirtyBirdsAre1337". This string is a hashtag for a Twitter post, and after a quick search, leads to a Twitter post with an encoded string "JFWI{7k3\_gxps573u\_g1y3u}". This encoded string is encoded with ROT\_3 Caesar cipher, and decoding it with ROT\_23 instead, will produce the flag.
