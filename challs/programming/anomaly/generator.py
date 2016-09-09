#!/usr/bin/python
import hashlib
import random

flag = "GCTF{5h4-rry_5h4-rry_n16h7}"
i = 1
chance = 1000000 // (len(flag) * 1.3)

def hexit(text):
	for i in range(512):
		text = hashlib.sha512(bytes(text, "UTF-8")).hexdigest()
	return text

with open('864e3e64c86dacf441bd5196f5c999f5', 'w+') as f:
	while len(flag) > 0 or i <= 1000000:
		text = hexit(str(i))
		if random.randint(0, chance) == 0 and len(flag) > 0:
			if i % 2 == 1:
				text = '{:0128x}'.format((int(text, 16) - ord(flag[0])))
			else:
				text = '{:0128x}'.format((int(text, 16) + ord(flag[0])))
			flag = flag[1:]
			print(flag)
		f.write(text + "\n")
		if i % 10000 == 0:
			print("Wrote: " + str(i) + " lines")
		i += 1
	f.close()
	