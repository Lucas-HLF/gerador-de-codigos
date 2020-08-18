import string
import random

def generateRandomPassword(lenght):
    passwordCharacters = string.ascii_letters + string.digits

    password = ''.join(random.choice(passwordCharacters) for i in range(lenght))

    return password

def passwordsVerification(passwords, length):
    if length < 5 or length > 25:
        print("ERRO")
    elif len(passwords) == 1:
        print(f"{len(passwords)} senha gerada")
        print(passwords)
        return passwords
    else:
        print(f"{len(passwords)} senhas geradas")
        return passwords
