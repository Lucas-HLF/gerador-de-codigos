import string
import random
from datetime import datetime


def generateRandomPassword(lenght):
    passwordCharacters = string.ascii_letters + string.digits
    password = ''.join(random.choice(passwordCharacters) for i in range(lenght))

    return password

def savePasswords(passwords):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    z = 1
    archive = open('Senhas.txt', 'a+')
    archive.write(f'\n \n{dt_string} \n')
    for i in range(len(passwords)):
        archive.write(f'Senhas {z}:' + passwords[i] + '\n')
        z += 1
    print("Novas senhas adicionandas no arquivo")
