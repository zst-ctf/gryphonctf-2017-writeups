#! /usr/bin/env python3
import os  
from base64 import *
from Crypto.Cipher import AES

for filename in os.listdir('./distrib/'):
	with open('./distrib/' + filename) as file:
		contents = file.read()

	ciphertext = b64decode(contents)
	key = filename
	plaintext = AES.new(key, AES.MODE_ECB).decrypt(ciphertext).decode()
	
	if 'GCTF' in plaintext:
		print(plaintext)
		quit()