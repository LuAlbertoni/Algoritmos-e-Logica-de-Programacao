# Faça um programa que:
#   leia dois vetores (A e B) com cinco posições para números inteiros.
#   o programa deve, então, subtrair o primeiro elemento de A do último de B, armazenando o resultado num terceiro vetor, subtrair o segundo elemento de A do penúltimo de B, armazenando o resultado num terceiro vetor e assim por diante.
#   ao final, mostre o resultado do terceiro vetor
# O índice de um dos vetores terá que ser decrementado (slide 2 de Vetor) , ou seja, você implementara ele manualmente.

# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

arrayA = []
arrayB = []
resultadosArray = []

for i in range(5):
    arrayA.append(int(input('Insira o número para array A: ')))
    arrayB.append(int(input('Insira o número para array B: ')))

for i in range(len(arrayA)):
    resultadosArray.append(arrayB[(len(arrayB) - 1) - i] - arrayA[i])
    
print(resultadosArray)