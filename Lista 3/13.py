# Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme
# as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou
# em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau
# A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o
# grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.

# Média 6.

grauA = float(input('Insira a nota final do Grau A: '))
grauB = float(input('Insira a nota final do Grau B: '))

media = round(((grauA + 2 * grauB) / 3), 2)

print('A média final é:', media)

if media >= 6:
    print('Aluno passou pela média')
else:
    print('Aluno em recuperação.\n')
    newGrade = input('Você quer substituir o Grau A ou o Grau B? Digite "a" ou "b": ')
    grauC = float(input('Insira a nota final do Grau C: '))

    if newGrade == 'a':
        media = round(((grauC + 2 * grauB) / 3), 2)
        print('A média final é:', media)
        if media >= 6:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')

    elif newGrade == 'b':
        media = round(((grauA + 2 * grauC) / 3), 2)
        print('A média final é:', media)
        if media >= 6:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
    else:
        print('ERRO! Alternativa não reconhecida.')









