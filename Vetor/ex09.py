# Criar um algoritmo que leia dados para um vetor de 100 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. Obs.: percentual = quantidade contada * 100 / quantidade total. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

elementosArray = []
extremos = []
media = 0
pares = 0

for i in range(100):
    # elementosArray.append(int(input('Insira o número: '))) # Caso queira adicionar manualmente
    elementosArray.append(i) # Adicionando automaticamente
    media += elementosArray[i]

    print(elementosArray[i])
    if (elementosArray[i] % 2) == 0:
        pares += 1

media /= len(elementosArray)
extremos = [elementosArray[0], elementosArray[0]]

for i in range(len(elementosArray)):
    if elementosArray[i] > extremos[0]:
        extremos[0] = elementosArray[i]
    elif elementosArray[i] < extremos[1]:
        extremos[1] = elementosArray[i]

print(f'Maior número: {extremos[0]}. Menor número: {extremos[1]}. Percentual de números pares: {(pares * 100) / len(elementosArray):.2f}%. Média: {media:.2f}')