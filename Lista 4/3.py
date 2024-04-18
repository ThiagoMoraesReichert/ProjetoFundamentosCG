# 3. Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número. 

num = int(input('Insira o número de 1 a 9 para a tabuada: '))

for i in range(1, 11):
    calculation = num * i
    print(num, 'x', i, '=', calculation)
