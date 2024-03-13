shirts = int(input("Insira a quantidade de camisetas: "))
pants = int(input("Insira a quantidade de calças: "))
belts = int(input("Insira a quantidade de cintos: "))

price = (shirts*25) + (pants*100) + (belts*40)
discount = round(( price * 0.10), 2)
total = price - discount


print("O valor total gasto é de: "+str(total)+" Reias.")


