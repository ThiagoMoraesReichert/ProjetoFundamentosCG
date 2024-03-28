# A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um
# algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:
# Categoria Idade
# *Infantil A 5-7 anos
# *Infantil B 8-10 anos
# *Juvenil A 11-13 anos
# *Juvenil B 14-17 anos
# *Sênior Maiores de 18 anos

swimmerAge = int(input("Insira a idade do jogador: "))

if swimmerAge >= 18:
    print("Categoria: Sênior")
elif swimmerAge >= 14 and swimmerAge <= 17:
    print("Categoria: Juvenil B")
elif swimmerAge >= 11 and swimmerAge <= 13:
    print("Categoria: Juvenil A")
elif swimmerAge >= 8 and swimmerAge <= 10:
    print("Categoria: Infantil B")
elif swimmerAge >= 5 and swimmerAge <= 7:
    print("Categoria: Infantil A")

