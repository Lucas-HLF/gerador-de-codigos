from functions import generateRandomPassword, passwordsVerification

passwords = []
loop = int(input('Quantas senhas você quer gerar? \n'))
length = int(input('Quantos caracteres a senha deve ter? (mínimo 5, máximo 25) \n'))
z = 1

for i in range(loop):
    passwords.append(generateRandomPassword(length))
    print(f'Senha {z}: {passwords[i]},')
    z += 1

passwordsVerification(passwords, length)
