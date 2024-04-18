# Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo.
# A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima.

import random

randomNum = random.randrange(1, 10)

userAttemps = 3

while userAttemps > 0:
    userChoice = int(input('Qual é o número sorteado (1 a 10)? '))

    if userChoice == randomNum:
        print('Você acertou!')
        break
    if userChoice != randomNum:
        userAttemps -= 1

if userAttemps == 0:
    print('Você perdeu! O número era:', randomNum)



