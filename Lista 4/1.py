
# *a. Gerar e escrever todos os números inteiros do intervalo [0,100].

# for i in range(0, 100):
#     print(i)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *b. Gerar e escrever os números pares do intervalo [20,50].

# for i in range(20, 50):
#     if i % 2 == 0:
#         print(i)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *c. Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente.

# list = []

# for i in range(25, 70):
#     list.append(i)

# list.sort(reverse=True)
# print(list)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *d. Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente.

# list = []

# for i in range(25, 70):
#     if i % 2 != 0:
#         list.append(i)

# list.sort(reverse=True)
# print(list)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *e. Ler 15 números e escrever a soma e a média dos números lidos.

# result = 0

# for i in range(15):
#     num = float(input('Insira o número: '))

#     result += num

# result = result / 15
# print(result)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *f. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos

# par = []
# impar = []

# for i in range(10):
#     num = int(input('Insira o número: '))

#     if num % 2 == 0:
#         par.append(num)
#     elif num % 2 != 0:
#         impar.append(num)

# tamanhoPar = len(par)
# tamanhoImpar = len(impar)

# print('Pares:', tamanhoPar)
# print('Impares:', tamanhoImpar)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *g. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem
# *“POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de
# *números positivos e negativos lidos.

# import random

# positivo = []
# negativo = []

# for i in range(20):
#     random_num = random.randrange(-10, 10)

#     if random_num > 0:
#         positivo.append(random_num)
#         print(random_num, '- POSITIVO')
#     elif random_num < 0:
#         negativo.append(random_num)
#         print(random_num, '- NEGATIVO')
#     elif random_num == 0:
#         print(random_num, '- NULO')

# tamanhoPositivo = len(positivo)
# tamanhoNegativo = len(negativo)

# print('Positivos:', tamanhoPositivo)
# print('Negativos:', tamanhoNegativo)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# *h. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números
# *que deverão ser lidos e também deve ser lido do teclado)

# result = 0

# numRange = int(input('Insira a quantidade de números a serem lidos: '))

# for i in range(numRange):
#     num = float(input('Insira o número: '))

#     result += num

# print(result)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
