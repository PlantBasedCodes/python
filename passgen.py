#//==  VERSION 1.2
#imports 
import time
from time import sleep
import sys
import random


#stings
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()+_-='
charactername = 'abc123'
VisaDeposit = '1234567890'

Password = 'Password'
Username = 'Username'
Backup = 'Backup'


#stuff here
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.049)


password = ''
for x in range(16):
    password += random.choice(chars)
    
username1 = ''
for x in range(12):
    username1 += random.choice(charactername)

backupcode = ''
for x in range(6):
    backupcode += random.choice(VisaDeposit)
        
#code
print_slow("PassShield V1\n")
sleep(.75)
print_slow("Password Generator \n")
sleep(.75)

while True:
    sleep(1)
    Option = input('\n Would you like to generate a\n Password\n Username\n or Backup Code: ')
    if Option == Password:
        print(password)
    elif Option == Username:
        print(username1)
    elif Option == Backup:
        print(backupcode)
    else:
        print('Case Senitive!')


#other



