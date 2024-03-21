# Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor
# da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço
# for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na
# tela o valor de venda.

num = float(input('insira o valor da compra do produto: '))

if num < 20.00:
    worth = round((num*0.45), 2)
    total = num + worth
    print('O valor total para a venda do produto é de R$', total)
elif num > 20 and num <= 50:
    worth = round((num*0.35), 2)
    total = num + worth
    print('O valor total para a venda do produto é de R$', total)
else:
    worth = round((num*0.25), 2)
    total = num + worth
    print('O valor total para a venda do produto é de R$', total)