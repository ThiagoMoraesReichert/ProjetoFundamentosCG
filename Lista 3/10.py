# Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que
# simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no
# começo do programa quantas faces quer, para depois fazer o sorteio.
import random

print(
    'Escolha um dos dados a seguir:\n'
    '1) 4 faces.\n'
    '2) 6 faces.\n'
    '3) 8 faces.\n'
    '4) 10 faces.\n'
    '5) 12 faces.\n'
    '6) 16 faces.\n'
)

user_choice = int(input('Quantas faces você deseja? '))

if user_choice == 4:
    random_num = random.randrange(1, 4)
    print(random_num)
elif user_choice == 6:
    random_num = random.randrange(1, 6)
    print(random_num)
elif user_choice == 8:
    random_num = random.randrange(1, 8)
    print(random_num)
elif user_choice == 10:
    random_num = random.randrange(1, 10)
    print(random_num)
elif user_choice == 12:
    random_num = random.randrange(1, 12)
    print(random_num)
elif user_choice == 16:
    random_num = random.randrange(1, 16)
    print(random_num)
else:
    print("Valor não aceito. Por favor, insira um valor de acordo com as alternativas propostas.")



