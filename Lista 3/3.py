# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
# o resultado.

num = float(input("Insira o valor a ser lido: "))

if num > 0:
    print(num * 2)
else: #Poderia ser um "elif num < 0, mas nesse caso não faz diferença."
    print(num * 3)