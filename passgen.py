import time
import sys
import random
import os
from time import sleep
from os import system
import webbrowser
import pyperclip
import string
import colorama
from colorama import Fore, Back, Style

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PassSheild V2 - Tools for nerds")

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()+_-='
charactername = 'abcdefghijklmnopqrstuvwzyz'
VisaDeposit = '1234567890'
Robuxchars = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'

Owner = 'Owner - Chris\n'
Developer = 'Developer - Chris\n'
Staff = 'Staff - Empty\n'
Website = 'Website Designer - Chris\n'
Support = 'Support - Empty\n'

def generate_password(length):
    """Generate a random password of a given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password


def credits():
    print(Owner)
    print(Developer)
    print(Staff)
    print(Website)
    print(Support)

Robux5 = ''
for x in range(16):
    Robux5 += random.choice(Robuxchars)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.049)
        
def freerobux():
    Robux1 = ''
    for x in range(4):
        Robux1 += random.choice(Robuxchars)
    Robux2 = ''
    for x in range(4):
        Robux2 += random.choice(Robuxchars)
    Robux3 = ''
    for x in range(4):
        Robux3 += random.choice(Robuxchars)
    Robux4 = ''
    for x in range(4):
        Robux4 += random.choice(Robuxchars)
    print('RI'+'-'+Robux1+'-'+Robux2+'-'+Robux3+'-'+Robux4)
    return freerobux


def generate_username():
    username = ''.join(random.choice(charactername) for _ in range(12))
    return username

def generate_backup_code():
    backupcode = ''.join(random.choice(VisaDeposit) for _ in range(6))
    return backupcode

open = input('Would you like to open Passsheild V2? [Y/N]\nInput: ')

if open == 'yes' or open == 'Y' or open == 'y' or open == 'Yes':
    os.system('cls')
else:
    print('\nClosing')
    print('.75')
    sleep(.25)
    print('.50')
    sleep(.25)
    print('.25')
    sleep(.25)
    print('0')
    print('bye :3')
    sleep(.25)
    quit()

def main():
    print('loading.')
    sleep(.37)
    print('loading..')
    sleep(.12)
    print('loading...')
    sleep(.84)
    print('Loaded!')
    sleep(.93)
    os.system('cls')
    print_slow("PassShield V2\n")
    time.sleep(.75)
    print_slow("Tools for stuff - PassSheild owner\n")
    sleep(1.75)

    while True:
        os.system('cls')
        print(f"{Fore.RED} ___                      ___  _          _  _     _")
        print(f"{Fore.RED}| _ \ __ _  ___ ___      / __|| |_   ___ (_)| | __| |")
        print(f"{Fore.RED}|  _// _` |(_-/(_-/      \__ \|   \ / -_)| || |/ _` |")
        print(f"{Fore.RED}|_|  \__/_|/__//__/      |___/|_||_|\___||_||_|\__/_|\n")
        sleep(.75)
        option = input(f'Main{Fore.RED}\n[1]. Password       [2]. Username\n[3]. Backup Code    [4]. Robux Generator\n------------\nOther\n[5]. Copy Discord   [6]. Help\n[7]. Github         [8]. Exit\n[9]. Credits        [10]. Updates\n\Input: ')
        if option == '1':
            length = int(input("Enter the length of the password: "))
            password = generate_password(length)
            print("Your password is:", password)
            input("Press Enter to continue...")
        elif option == '2':
            username = generate_username()
            print("Generated Username:", username)
            input("Press Enter to continue...")
        elif option == '3':
            backupcode = generate_backup_code()
            print("Generated Backup Code:", backupcode)
            print('Automatically Copied')
            input("Press Enter to continue...")
        elif option == '4':
            Robux = freerobux()
            input("Press Enter to continue...")
        elif option == '5':
            pyperclip.copy('https://discord.gg/BJ4yfusK')
            webbrowser.open_new_tab("https://discord.gg/BJ4yfusK")
            input("Press Enter to continue...")
        elif option == '6':
            print('Password - Generates a random password')
            print('Username - Generates a random username')
            print('Backup Code - Generates a random backup code \n\n\n')
        elif option == '7':
            input('Are you sure? ENTER TO CONTINUE: ')
            webbrowser.open_new_tab("https://github.com/PlantBasedCodes/python")
        elif option == '8':
            print('Closing!')
            sleep(.75)
            break
        elif option == '9':
            credits()
            input("Press Enter to continue...")
        elif option == '9':
            print('Pass Sheild Updates\n\n[Update 1.0] - Added Username, Password and backup code generator\n[Update 1.1] - Added loading & real robux generator\n[Update 1.2] - Added github & other links\n[Update 1.3] - Added inputs')
        else:
            print('Invalid option. Please select a valid option.')

if __name__ == "__main__":
    main()
