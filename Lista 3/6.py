# Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
# disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
# um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
# soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
# que o programa venceu
import random

user_choice = str(input('Você aposta em PAR ou ÍMPAR? '))
num = int(input('Insira um valor de 0 a 5: '))

random_num = random.randrange(0, 5)

total = num + random_num

if user_choice == 'par' or user_choice == 'ímpar':
    if total % 2 == 0:  
        if user_choice == 'par':
            print('Você ganhou!')
        else:
            print('Você perdeu.')
    else:
        if user_choice == 'ímpar':
            print('Você ganhou!')
        else:
            print('Você perdeu.')
else:
    print('ERRO! Verifique se você escolheu uma das alternativas propostas.')


