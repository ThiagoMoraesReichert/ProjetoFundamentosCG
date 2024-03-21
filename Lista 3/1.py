# Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
# diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada

num_1 = float(input("Insira o dividendo: "))
num_2 = float(input("Insira o divisor: "))

if num_2 != 0:
    total = num_1 / num_2
    print("Resultado:", num_2)
else:
    print("ERRO! O divisor não pode ser 0.")

