# Faça um programa que:
    # preencha um vetor com dez números reais
# Calcule e mostre:
    # a quantidade de números negativos
    # a soma dos números positivos desse vetor
    # não use nenhuma função pronta da linguagem Python

elementosArray = []
quantNegativos = 0
somaPositivos = 0

for i in range(10):
    elementosArray.append(int(input('Insira o número: ')))

    if elementosArray[i] < 0:
        quantNegativos += 1
    else:
        if elementosArray[i] % 2 == 0:
            somaPositivos += elementosArray[i]

print(f'Quantidade de números negativos: {quantNegativos}. Soma dos números positivos: {somaPositivos}')