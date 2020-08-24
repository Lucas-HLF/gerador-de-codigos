from Password.functions import generateRandomPassword, passwordsVerification, savePasswords

passwords = []
loop = int(input('Quantas senhas você quer gerar? \n'))
length = int(input('Quantos caracteres a senha deve ter? (mínimo 5, máximo 25) \n'))
z = 1

for i in range(loop):
    passwords.append(generateRandomPassword(length))
    verify = passwordsVerification(passwords, length)
    if verify == False:
        break
    print(f'Senha {z}: {passwords[i]},')
    z += 1
print(f'{len(passwords)} senhas geradas')

if verify:
    print('1- Salvar senhas em um arquivo')
    print('2- Não salvar')
    opcao = int(input())

    if opcao == 1:
        savePasswords(passwords)
        print('Arquivo txt salvo na pasta atual')
else:
    print('Exit')
    exit()
