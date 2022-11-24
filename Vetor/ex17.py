# Faça um programa que:
#   carregue dois vetores com 10 números cada
#   faça a multiplicação dos números na mesma posição
#   o resultado deverá ser adicionada em um terceiro vetor
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

array1 = []
array2 = []
resultadosArray = []

for i in range(5):
    array1.append(int(input('Insira um número: ')))
    array2.append(int(input('Insira um número: ')))

for i in range(len(array1)):
    resultadosArray.append(array1[i] * array2[i])

print(resultadosArray)