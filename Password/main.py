from Password.functions import *

passwords = []
loop = int(input('Quantas senhas você quer gerar? \n'))
length = int(input('Quantos caracteres a senha deve ter? \n'))
z = 1

for i in range(loop):
    passwords.append(generateRandomPassword(length))
    print(f'Senha {z}: {passwords[i]},')
    z += 1
print(f'{len(passwords)} senhas geradas')

savePasswords(passwords)
