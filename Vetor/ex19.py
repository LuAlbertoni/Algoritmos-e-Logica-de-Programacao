# Faça um programa que:
#   insira dez números inteiros em um vetor
#   crie um segundo vetor, substituindo os números multiplos de 3 por "999""
#   exiba os dois vetores
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

array = []
arrayMultiplos = []

for i in range(10):
    array.append(int(input('Insira o número: ')))

for i in range(len(array)):
    if array[i] % 3 == 0:
        arrayMultiplos.append(999)
    else:
        arrayMultiplos.append(array[i])

print(arrayMultiplos)