'''The program creates a key for encryption and encrypts a file'''

import os  # a module for work with OS
import pyAesCrypt  # a module for encryption
# a module for encryption with a key generation function
from cryptography.fernet import Fernet


# key generation
def write_key():
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)


bufferSize = 512*1024
password = input('Enter the key: ')  # type the key used for encryption


# encryption
def crypt(dir):
    print('-----------------------------------')
    pyAesCrypt.encryptFile(str(dir), str(dir)+'.aes', password, bufferSize)
    print('[Crypted] '+str(dir)+'.aes')


# to generate a key:
# write_key()

# file name to be encrypted
# dir = input('Enter file name: ')

# to encrypt the file
# crypt(dir)


# to decrypt the file
# pyAesCrypt.decryptFile("/home/elizaveta/Desktop/ITMO/Python/cr.txt.aes",
#                        "/home/elizaveta/Desktop/ITMO/Python/cr.txt",
#                        password, bufferSize)
