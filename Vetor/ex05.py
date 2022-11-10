# Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas índices/posições. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

elementosArray = []
positivosArray = []
posicoesArray = []

for i in range(8):
    num = int(input('Insira o número: '))
    elementosArray.append(num)

    if (num % 2) == 0:
        positivosArray.append(num)
        posicoesArray.append(i)

print(f'Números pares: {positivosArray} nas respectivas posições: {posicoesArray}')