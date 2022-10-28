# Faça um programa que receba um conjunto de valores inteiros, calcule e exiba o maior e o menor valor do conjunto.
#   Para encerrar a entrada de dados, deve ser digitado o valor zero;
#   Para valores negativos, deve ser enviada uma mensagem;
#   Esses valores (zero e negativos) não entrarão na lógica de encontrar o maior e o menor valor.

maior = 0
menor = 0

num = int(input('Insira um número positivo inteiro: '))

while num != 0:
    if num < 0:
        print('Números negativos não são permitidos!')
    else:
        if menor == 0:
            menor = num
            
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    num = int(input('Insira um número positivo inteiro ou "0" para finalizar: '))

print(f'Maior: {maior}, menor: {menor}')
