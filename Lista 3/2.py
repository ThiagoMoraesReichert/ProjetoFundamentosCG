# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A
# + C.

A = float(input("Insira o valor de A: "))
B = float(input("Insira o valor de B: "))
C = float(input("Insira o valor de C: "))

if (A + B) > (A + C):
    print('A soma de A + B é maior que A + C')
else:
    print('A soma de A + B não é maior que A + C')
