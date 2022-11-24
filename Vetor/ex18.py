# Faça um programa que:
#   leia um vetor de 10 números inteiros
#   exiba na tela os números positivos e seus respectivos índices.
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

array = []

for i in range(10):
    array.append(int(input('Insira o número: ')))

for i in range(len(array)):
    if array[i] % 2 == 0:
        print(f'Número "{array[i]}" na posição "{i}"')