question = "Qual é o verdadeiro nome do super-herói Batman?"
print(question)

alternativeA = "a) Bruce Wayne"
alternativeB = "b) Clark Kent"
alternativeC = "c) Peter Parker"
alternativeD = "d) Tony Stark"
alternativeE = "e) Steve Rogers"

print(alternativeA)
print(alternativeB)
print(alternativeC)
print(alternativeD)
print(alternativeE)

answer = input("Insira a alternativa: ")

if answer == "a" or answer == "b" or answer == "c" or answer == "d" or answer == "e":
   print("Você respondeu a alternativa " + answer + ". A resposta correta é a alternativa a.")
else:
   print("Nenhuma alternativa selecionada ou alternativa inválida.")