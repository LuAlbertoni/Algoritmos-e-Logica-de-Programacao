# Faça um programa que:
#   preencha dois vetores com de dez numeros cada
#   preencha um terceiro vetor com os números dos dois vetores anteriores ordenados em ordem crescente

array1 = []
array2 = []
ordenadosArray = []

for i in range(10):
    array1.append(int(input('Insira um número: ')))
    array2.append(int(input('Insira um número: ')))

for i in range(len(array1)):
    ordenadosArray.append(array1[i])
    ordenadosArray.append(array2[i])

ordenadosArray.sort()

print(ordenadosArray)