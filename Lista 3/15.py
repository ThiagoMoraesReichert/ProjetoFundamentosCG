# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#* 1 - À vista em dinheiro, recebe 15% de desconto
#* 2 - À vista no cartão de crédito, recebe 10% de desconto
#* 3 - Em duas vezes, preço normal de etiqueta sem juros
#* 4 - Em três vezes, preço normal de etiqueta mais juros de 10%

value = float(input('Insira o valor do produto: '))
print('Qual é o método de pagamento?\n1 - À vista em dinheiro, recebe 15% de desconto\n2 - À vista no cartão de crédito, recebe 10% de desconto\n3 - Em duas vezes, preço normal de etiqueta sem juros\n4 - Em três vezes, preço normal de etiqueta mais juros de 10%\n')

user_choice = int(input('Escolha uma das alternativas: '))

if user_choice == 1:
    promotion = round((value*0.15), 2)
    finalValue = value - promotion
    print('O total a pagar é:', finalValue)
elif user_choice == 2:
    promotion = round((value*0.10), 2)
    finalValue = value - promotion
    print('O total a pagar é:', finalValue)
elif user_choice == 3:
    print('O total a pagar é:', value)
elif user_choice == 4:
    interest = round((value*0.10), 2)
    finalValue = value + interest
    print('O total a pagar é:', finalValue)
else:
    print('ERRO! Alternativa não reconhecida.')

