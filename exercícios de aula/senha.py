# Faça um programa que permita o usuário entrar com uma senha no máximo em 3 tentativas

senhaCadastrada = input("Insira uma senha: ")

tentativas = 0

while tentativas < 3:
    senha = input('Digite sua senha: ')

    if senha != senhaCadastrada:
        print('Senha invalida.')
        tentativas += 1
    elif senha == senhaCadastrada:
        print('Bem-vindo(a) usuário!')
        break

if tentativas == 3:
    print('Número máximo de tentativas realizadas. Tente novamente mais tarde.')
