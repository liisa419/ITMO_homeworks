'''The program looks for passwords to different accounts
in a txt file. For usage type the account name you
want to get password to and the program will copy it'''

import pyperclip  # a module for copy and paste clipboard functions
import crypt  # the written module for work with encryption

# specify the name of the file to be decrypted
crypted = input('Enter the name of encrypted file: ')

# file decryption with a specific key and saving in decr.txt
crypt.pyAesCrypt.decryptFile(crypted,
                             '/home/elizaveta/Desktop/ITMO/Python/decr.txt',
                             crypt.password, crypt.bufferSize)

decrypted = '/home/elizaveta/Desktop/ITMO/Python/decr.txt'

# to split decrypted file to username and password and save into a list
with open(decrypted) as my_pass:
    credentials = [x.strip().split(':') for x in my_pass]

# to specify the account you want to get the password to
account = input('Enter account name: ')

# to save input into a list
words = account.split()
usrnames = []

# to check if there are more than one account names
if len(words) > 1:
    print('Please choose the only one account name.')
# to check if there are no account names
elif len(words) == 0:
    print('Please enter the account name.')

# to add account names from file into the list
# to find equal to the input and copy the corresponding password
for username, password in credentials:
    usrnames.append(username)
    if len(words) == 1 and username == words[0]:
        pyperclip.copy(password)
        print('Password for ' + account + ' copied to clipboard.')
    else:
        continue

# to check if input not in the source file
if len(words) != 0 and words[0] not in usrnames:
    print('There is no account with this name.')

# to remove decrypted file
crypt.os.remove('/home/elizaveta/Desktop/ITMO/Python/decr.txt')
