#imports
import time
import sys

#funtion
def Name_Age_Guesser():
    name = input('What is your name: ')
    time.sleep(.5)
    print('ok!')
    time.sleep(.5)
    print('Hello ' + name + '!')
    time.sleep(.75)
    age = input('Enter your age: ')
    time.sleep(.75)
    print('Hello ' + name + '! ' + 'You are ' + age + ' years old' + '!')
    time.sleep(90000)
    return

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("age guesser & name guesser \n")

time.sleep(2)
time.sleep(2)
Name_Age_Guesser()
