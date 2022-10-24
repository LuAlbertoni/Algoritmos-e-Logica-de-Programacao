# Construir um algoritmo para calcular e apresentar a idade atual de algumas pessoas em relação ao ano atual, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no ano de nascimento para sair.

ano = int(input('Insira o ano de nascimento ou "0" para finalizar: '))

while ano != 0:
    print(f'Idade: {2022 - ano}')

    ano = int(input('Insira o ano de nascimento ou "0" para finalizar: '))