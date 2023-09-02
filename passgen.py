#imports
import time
from time import sleep
import random
import sys

#code

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()+_-='
username = 'qwertyuiopasdfghjklzxcvbnm1234567890'
backup = '1234567890abcgiop'

password = ''
for x in range(16):
    password += random.choice(chars)

username1 = ''
for x in range(12):
    username1 += random.choice(username)

backupcode = ''
for x in range(6):
    backupcode += random.choice(backup)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("Username Password & Security Code Generator \n")
sleep(.75)
print_slow("Very basic \n")
sleep(.75)
print_slow("Source @ https://github.com/PlantBasedCodes/python/blob/main/passgen.py \n")
sleep(3)
print('\n Your password: ' + password +  '\n Your username: ' + username + '\n You backup codes: ' + backupcode + '\n')
sleep(.95)
print('thank you for using this \n')
sleep(.75)
print('- Chris \n')
