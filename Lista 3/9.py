# Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação
# de cada moeda em relação ao real. Depois apresente o seguinte menu:
# 1) Converter de Real para Euro
# 2) Converter de Real para Dólar
# 3) Converter de Euro para Dólar
# 4) Converter de Euro para Real
# 5) Converter de Dólar para Euro
# 6) Converter de Dólar para Real
# Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda
# destino

dolar = float(input('Insira o valor do dólar em relação ao real: '))
euro = float(input('Insira o valor do euro em relação ao real: '))

user_choice = int(input(
    'Escolha uma alternativa:\n'
    '1) Converter de Real para Euro:\n'
    '2) Converter de Real para Dólar:\n'
    '3) Converter de Euro para Dólar:\n'
    '4) Converter de Euro para Real:\n'
    '5) Converter de Dólar para Euro:\n'
    '6) Converter de Dólar para Real:\n'
))

if user_choice == 1:
    real = float(input('insira o valor em real: '))
    euro = round((real / euro), 2)
    print('O resultado é: €', euro)
elif user_choice == 2:
    real = float(input('insira o valor em real: '))
    dolar = round((real / dolar), 2)
    print('O resultado é: US$', dolar)
elif user_choice == 3:
    euroUserChoice = float(input('insira o valor em euro: '))
    euro = euroUserChoice * euro
    dolar = round(( euro / dolar), 2)
    print('O resultado é: US$', dolar)
elif user_choice == 4:
    euroUserChoice = float(input('insira o valor em euro: '))
    real = round(( euroUserChoice * euro), 2)
    print('O resultado é: R$', real)
elif user_choice == 5:
    dolarUserChoice = float(input('insira o valor em dolar: '))
    dolar = dolarUserChoice * dolar
    euro = round(( dolar / euro), 2)
    print('O resultado é: €', euro)
elif user_choice == 6:
    dolarUserChoice = float(input('insira o valor em dolar: '))
    real = round(( dolarUserChoice * dolar), 2)
    print('O resultado é: R$', real)
else:
    print("ERRO! Verifique se selecionou uma das alternativas propostas.")










