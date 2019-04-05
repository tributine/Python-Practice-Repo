#! python3
# The above code is for shebang...?

# Name: christopher wong
# date: 2019-04-03
# Project name: pw.py
# Description: This python code saves passwords and copies them to clipboard
# NOTE THIS IS A VERY INSECURE PROGRAM


PASSWORDS = {'email': 'F12312e9dasFdaskall212',
            'blog': '123123123123',
            'toilet': 'IneedtoPOOP'}

import sys, pyperclip #import sys python library
if len(sys.argv) < 2:
    print('Usage: Python pw.py [account] - copy account password')
    sys.exit() #exits the PROGRAM

account = sys.argv[1] # first command line arg is account Name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
