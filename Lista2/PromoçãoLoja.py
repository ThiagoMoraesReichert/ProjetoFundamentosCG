compra = float(input("Insira o valor do produto: "))

promocao = round((compra*0.15), 2)
valorFinal = compra - promocao

print("O valor do produto com o desconto é de: "+str(valorFinal)+" Reais")