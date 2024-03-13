gasolina = float(input("Insira o valor da gasolina: "))
valorPago = float(input("Insira o valor a pagar no total: "))

totalLitros = round((valorPago / gasolina), 2)

print("O motorista conseguiu abastecer "+str(totalLitros)+" litro(s)")