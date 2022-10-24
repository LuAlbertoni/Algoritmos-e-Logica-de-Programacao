# Faça um programa que receba a idade e a altura de várias pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.

quant = 0
alturaTotal = 0

idade = int(input('Insira a idade ou algum número igual ou abaixo de "0" para finalizar: '))

while idade > 0:
    altura = float(input('Insira a altura: '))

    if idade > 20:
        quant += 1
        alturaTotal += altura

    idade = int(input('Insira a idade ou algum número igual ou abaixo de "0" para finalizar: '))

print(f'Média: {alturaTotal/quant:.2f}')