# Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de
# cédulas para um determinado valor informado pelo usuário considerando notas de:
# *R$ 100, R$ 50, R$ 20, R$ 10 e R$ 5 e R$ 1.
# Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao
# solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram
# exibidas informações sobre as demais cédulas):
# 1 nota(s) de R$ 10.
# 1 nota(s) de R$ 5.
# 3 nota(s) de R$ 1.

value = int(input('Insira o valor: '))

cash100 = 0
cash50 = 0
cash20 = 0
cash10 = 0
cash5 = 0
cash1 = 0

while value != 0:
    if value >= 100:
        value -= 100
        cash100 += 1
    elif value >= 50 and value < 100:
        value -= 50
        cash50 += 1
    elif value >= 20 and value < 50:
        value -= 20
        cash20 += 1
    elif value >= 10 and value < 20:
        value -= 10
        cash10 += 1
    elif value >= 5 and value < 10:
        value -= 5
        cash5 += 1
    elif value < 5:
        value -= 1
        cash1 += 1

if cash100 > 0:
    print(cash100, 'nota(s) de R$ 100.')
if cash50 > 0:
    print(cash50, 'nota(s) de R$ 50.')
if cash20 > 0:
    print(cash20, 'nota(s) de R$ 20.')
if cash10 > 0:
    print(cash10, 'nota(s) de R$ 10.')
if cash5 > 0:
    print(cash5, 'nota(s) de R$ 5.')
if cash1 > 0:
    print(cash1, 'nota(s) de R$ 1.')





