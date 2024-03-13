pesoPrato = int(input("Insira o peso total do prato em gramas: "))

TotalPagar = round(((pesoPrato / 1000) * 40), 2)

print("O valor total a pagar é "+str(TotalPagar)+" reais.")