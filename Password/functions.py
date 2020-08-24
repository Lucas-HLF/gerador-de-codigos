import string
import random
from datetime import datetime


def generateRandomPassword(lenght):
    passwordCharacters = string.ascii_letters + string.digits
    password = ''.join(random.choice(passwordCharacters) for i in range(lenght))

    return password


def passwordsVerification(passwords, length):
    if length < 5 or length > 25:
        print("ERRO")
        return False
    if len(passwords) == 1:
        return passwords
    else:
        return passwords


def savePasswords(passwords):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    archive = open('Senhas.txt', 'w')
    z = 1
    archive.write(f'\n \n{dt_string} \n')
    for i in range(len(passwords)):
        archive.write(f'Senhas {z}:' + passwords[i] + '\n')
        z += 1