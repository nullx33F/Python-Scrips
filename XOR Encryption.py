
# XOR encryption in python 3 by Nullx33F
# Coded in    : 15/11/2020
# last update : 20/02/2021

# importing area
import string
import random
from os import system

# the result file.txt path
# edit it if you want to save results in txt file to avoide unsupported chars!
# un comment writting function after encryption/decryption process.
RESULT_FILE_PATH = r""


def writing(RESULT_FILE_PATH, result):
    """[this function used to write/store the result of all encryption or decryption processes]

    Args:
        RESULT_FILE_PATH ([String]): [Result file directory/path]
        result ([String]): [the encrypted or decrypted text.]
    """
    with open(f"{RESULT_FILE_PATH}\RESULT-FILE.txt", "a") as result_file:
        result_file.write(result)

# generate randome key with a Custom length
# The key consists of upper and lower case letters, numbers, and symbols
def generate_key(length):
    """[summary]

    Args:
        size ([int]): [The encryption key length >= text length]

    Returns:
        [String]: [generated key with the given length]
    """
    key = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + 
                                string.digits + "~!@#$%^&*()_+=*{}[]<>-,;:؛") for _ in range(0, length))
    return key


# XOR function
def XOR(text, key):
    """[ A function that receives text and an encryption key and does Encrypt/Decrypt XOR Process ]

    Args:
        text ([String])     : [ the plain text or the encrypted text ]
        key ([String])      : [ encrypting key ]

    Returns:
        [String]: [if the text is encrypted it returns decrypted text, if the text is a plain text it returns the encrypted text]
    """
    # return the encrypted text / decrypted text
    return "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(text, str(key))])


def main():
    
    # print banner
    print("""
         /$$   /$$  /$$$$$$  /$$$$$$$ 
        | $$  / $$ /$$__  $$| $$__  $$
        |  $$/ $$/| $$  \ $$| $$  \ $$
        \  $$$$/  | $$  | $$| $$$$$$$/
         >$$  $$  | $$  | $$| $$__  $$
        /$$/\  $$ | $$  | $$| $$  \ $$
        | $$  \ $$|  $$$$$$/| $$  | $$
        |__/  |__/ \______/ |__/  |__/ By: @Nullx33F

        [1] Encrypt plain text with random encryption key.
        [2] Decrypt with Specific encryption key.
        [3] Encrypt with Specific encryption key.

    """)
    
    # get user choice number
    choice = int(input("Enter your choice~# "))
    while choice < 1 or choice > 3:
        print("[-] Enter valid input number -_- ")
        choice = int(input("Enter your choice~# "))

    if choice == 1:  # Encrypt plain text with random encryption key.

        # get plain text from user then calculate it's length to generate a key with the same length.
        plain_text = input("[+] Enter plain-text~# ")

        # get the key length from the user.
        # generate the encryption key (key_length) length.
        # store the key in key variable
        key = generate_key(len(plain_text))

        # result = plain text + key
        result = f"""
        [+] Result:
         |   Encrypted Text: {XOR(plain_text, key)}
         |   Encryption key: {key}
        [-]-------------------------------------\n"""
        # print the result on screen
        print(result)

        # un comment the following line to write results in txt file.
        # writing(RESULT_FILE_PATH, result)


    elif choice == 2:  # Decrypt with Specific encryption key

        # get encrypted text from user then calculate it's length to generate a key with the same length.
        encrypted_text = input("[+] Enter encrypted text~# ")

        # store the key in key variable
        key = input("[+] Enter decryption key~# ")

        # result = encrypted text + key
        result = f"""
        [+] Result:
         |   Decrypted Text: \033[92m{XOR(encrypted_text, key)}\033[97m
         |   Encryption key: \033[92m{key}\033[97m
        [-]-------------------------------------\n"""
        # print the result on screen
        print(result)

        # un comment the following line to write results in txt file.
        # writing(RESULT_FILE_PATH, result)


    elif choice == 3:  # Encrypt with Specific encryption key.
        # get plain text from user then calculate it's length to generate a key with the same length.
        plain_text = input("[+] Enter plain-text~# ")
        text_length = len(plain_text)

        # get the key length from the user.
        key = input("[+] Enter decryption key~# ")

        while len(key) < len(plain_text):
            print("[-] Key length must be >= Plain-text length :(")
            text_length = len(plain_text)
            # get the key length from the user.
            key = input("[+] Enter decryption key~# ")

        # result = plain text + key
        result = f"""
        [+] Result:
         |   Encrypted Text: \033[92m{XOR(plain_text, key)}\033[97m
         |   Encryption key: \033[92m{key}\033[97m
        [-]-------------------------------------\n"""
        # print the result on screen
        print(result)

        # un comment the following line to write results in txt file.
        # writing(RESULT_FILE_PATH, result)


if __name__ == '__main__':
    system("cls") # for windows
                  # if you want to run it on linux change it to clear :)

    # calling main function.
    main()