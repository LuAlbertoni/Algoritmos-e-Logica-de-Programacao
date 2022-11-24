# Faça um programa que:
#   receba dez números inteiros e armazene-os em um vetor
#   classifique os números em dois vetores, um com números pares e o outra com os ímpares
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

parArray = []
imparArray = []

for i in range(10):
    num = int(input('Insira o número: '))

    if num % 2 == 0:
        parArray.append(num)
    else:
        imparArray.append(num)

print(f'Números pares: {parArray}. Números Ímpares: {imparArray}')