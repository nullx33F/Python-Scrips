
#!/usr/bin/python

# Coded by Hossam Hamdy @Nullx33F
# Coded in : 20/02/2021
# VERSION = "v0.3"

# to-do
	# add brute force options
	# add option parser


# importing area
import hashlib
import os

# all supported hashing algorithms
HASHING_TYPES = ["MD5","SHA1","SHA224","SHA256","SHA384"]
# author name -_-
AUTHOR = "\033[93mNullx33F\033[97m"
# version number
VERSION = "\033[91mv0.3\033[97m"


def get_hash_of(plain_text, hash_type):
	"""[function to get calculate the hash value for input data (text/binary file)]

	Args:
		plain_text [binary data]		: [the data which we want to calculate the hash value for it.]
		hash_type  [String]				: [the hashing algorithm]

	Returns:
		hashing_result [string]			: [the hash value of input with the givin hashing algorithm.]
	"""

	# get the hash type
	hashed_text = hashlib.new(hash_type)
	# encoding plain text
	hashed_text.update(plain_text)
	# hashing the text then store result in hashing_result var
	hashing_result = hashed_text.hexdigest()
	# return the result
	return hashing_result


def banner(AUTHOR, VERSION):
	"""[print the script information and options]

	Args:
		AUTHOR ([string])			: [author name]
		VERSION ([string])			: [script version]
	"""

	os.system("cls") # clear consol screen for windows

	# display banner on screen
	print(f"""\033[92m
		 __  __     ______     ______     __  __     ______   __  __    
		/\ \_\ \   /\  __ \   /\  ___\   /\ \_\ \   /\  == \ /\ \_\ \   
		\ \  __ \  \ \  __ \  \ \___  \  \ \  __ \  \ \  _-/ \ \____ \  
 	 	 \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\ \_\  \ \_\    \/\_____\ 
		  \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_/     \/_____/ By: @{AUTHOR}

		Supported Hashing in this version ({VERSION}):
			MD5 - SHA1 - SHA224 - SHA256 - SHA384

		Hashpy-options:
			[1] Calculate text hash.
			[2] Calculate file hash.
			[3] Check file integrity \n\n""")


def main():
    
	# display banner on screen
	banner(AUTHOR, VERSION)

	# get user choice
	user_choice = int(input("[+] Enter choice~$ "))

	# get valid inputs
	while user_choice > 4 or user_choice < 1:
		print("[-] Please enter valid choice number")
		user_choice = input("[+] Enter choice~$ ")


	if user_choice == 1:  # Calculate text hash
		# call calculate_text_hash() function when user_choice = 1
		calculate_text_hash()


	elif user_choice == 2:
		result = calculate_file_hash()
		print(f"Hashing file result : \033[93m{result}\033[97m \n")


	elif user_choice == 3:
    		
		result = calculate_file_hash()
		print(result)
		hash_value = input("[+] Enter hash value~$ ")
		# check Matching test of the two hashs
		if result == hash_value:
			print("\033[92m[+] Integrity: True\033[97m \n")
		else:
			print("\033[91m[-] Integrity: False\033[97m \n")


def calculate_text_hash():
	""" this function generate/ calculate the hashing value for plain text with a specific hashing type

	Returns:
		result [String]: [the hash value of the file content]
	"""
	

	# get plain text from the user.
	plain_text = input("[+] Enter plain text~$ ").encode()

	# display hashing algorithm
	print("Supported hashing algorithms: MD5 - SHA1 - SHA224 - SHA256 - SHA384")

	# get hashing type from user
	hashing_algo = input("[+] Enter hashing type~$ ").upper()

	while hashing_algo not in HASHING_TYPES: # get a supported hashing type.
		print("[-] Please enter supported algorithm -_-")
		hashing_algo = input("[+] Enter hashing type~$ ").upper()
	
	# store result in result variable.
	result = get_hash_of(plain_text, hashing_algo)

	# displaing the result of hashing process.
	print(f"""
		[+] Plain text   : {plain_text}
		[+] Hashing type : {hashing_algo}
		[+] Hashed text  : \033[93m{result}\033[97m \n""")
    			

def calculate_file_hash():
	""" this function generate/calculate the hashing value for binary files with a specific hashing type

	Returns:
		result [string]: [the hashed file content value]
	"""
	file_content = ""
	file_name = input("[+] enter file name~$ ")
	with open(f"{file_name}", "rb") as binary_file:
		file_content = binary_file.read()

	# display hashing algorithm
	print("Supported hashing algorithms: MD5 - SHA1 - SHA224 - SHA256 - SHA384")

	# get hashing type from user
	hashing_algo = input("[+] Enter hashing type~$ ").upper()

	while hashing_algo not in HASHING_TYPES:  # get a supported hashing type.
		print("[-] Please enter supported algorithm -_-")
		hashing_algo = input("[+] Enter hashing type~$ ").upper()

	# store result in result variable.
	result = get_hash_of(file_content, hashing_algo)
	return result
	

if __name__ == "__main__":
    # calling main function
	main()
