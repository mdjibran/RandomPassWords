import string
import random
import os

alphas = list(string.ascii_letters)
nums = list(range(0,10))
reDo = True

while reDo:
    passwrd = ''
    os.system('cls')
    for a in range(4):
        passwrd += random.choice(alphas)
    for a in range(4):
        passwrd += str(random.choice(nums))
    print('=======================================')
    print("New Temporary Password :      " + passwrd)
    print('=======================================')
    print('Select the password and press CTRL+C to copy\n\n\n\n')
    print('Select an option : ')
    print('1 - Press 1 to Regenerate password')
    print('2 - Press any Key to Exit')
    c = input('Enter option : ')
    if c == '1':
        reDo = True
    else:
        os.system('cls')
        exit(0)
        
