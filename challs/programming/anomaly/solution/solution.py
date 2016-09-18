#!/usr/bin/python
import hashlib
import random

i = 1
flag = ""

def hexit(text):
	for i in range(512):
		text = hashlib.sha512(bytes(text, "UTF-8")).hexdigest()
	return text

print("Starting scan...")
	
with open('864e3e64c86dacf441bd5196f5c999f5', 'r') as f:
	for line in f:
		correct = hexit(str(i))
		if correct != line.strip():
			print("Anomaly Found:")
			print("Expected:", correct)
			print("Got:", line.strip())
			diff = abs(int(correct, 16) - int(line.strip(), 16))
			print("Decoded:", chr(diff))
			print("---")
			flag += chr(diff)
		i += 1
	f.close()
	
print("Flag:", flag)
	