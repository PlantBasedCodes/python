#imports
import time
from time import sleep
import random

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

print('Username Password & Security Code Generator')
sleep(.75)
print('Very basic ')
sleep(2)
print('\n Your password: ' + password +  '\n Your username: ' + username + '\n You backup codes: ' + backupcode + '\n')
