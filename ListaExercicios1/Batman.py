print("Qual é o verdadeiro nome do super-herói Batman?")

print("a) Bruce Wayne \nb) Clark Kent\nc) Peter Parker\nd) Tony Stark\ne) Steve Rogers")

answer = input("Insira a alternativa: ")

if answer == "a" or answer == "b" or answer == "c" or answer == "d" or answer == "e":
   print("Você respondeu a alternativa " + answer + ". A resposta correta é a alternativa a.")
else:
   print("Nenhuma alternativa selecionada ou alternativa inválida.")