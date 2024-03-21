# Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa
# deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
# segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
# 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20

salary = float(input('Insira o valor total do salário: '))

total = round((salary*0.11), 2)

if total > 318.20:
    total = 318.20

print('O valor do desconto previdenciário é:', total)
