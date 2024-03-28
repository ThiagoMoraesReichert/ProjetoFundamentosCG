# Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do
# conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes)
# conforme a seguinte tabela:
# a) crianças com menos de 10 anos pagam R$100;
# b) dependentes com idade entre 10 e 30 anos pagam R$220;
# c) dependentes com idade entre 31 e 60 anos pagam R$ 395; e
# d) dependentes com mais de 60 anos pagam R$ 480

totalValue = 300

conveniado = int(input('Insira a idade do conveniado: '))

userChoice = input('Possui dependentes? Digite "sim" ou "não": ')

if userChoice == 'sim':
    dependentesQtd = int(input('Quantos? '))
    for i in range(dependentesQtd):
        dependentesAge = int(input('Insira a idade de cada um deles (um por vez):'))

        if dependentesAge < 10:
            totalValue += 100
        if dependentesAge >= 10 and dependentesAge <= 30:
            totalValue += 220
        if dependentesAge >= 31 and dependentesAge <= 60:
            totalValue += 395
        if dependentesAge > 60:
            totalValue += 480
    print('O conveniado possui '+str(conveniado)+' anos de idade.\nO valor total a pagar considerando os dependentes é de: R$ '+str(totalValue)+'.')
elif userChoice == 'não':
    print('O conveniado possui '+str(conveniado)+' anos de idade.\nO valor total a pagar é de: R$ '+str(totalValue)+'.')

else:
    print('ERRO! Por favor, escolha uma das alternativas propostas.')