# Faça um programa que leia números inteiros m e n e os elementos de uma matriz A de números inteiros de dimensão m x n e conte o número de elementos que são iguais a zero.

matriz = []
quant = 0

m = int(input('Insira a quantidade de colunas: '))
n = int(input('Insira a quantidade de linhas: '))

for i in range(m):
    linha = []
    
    for j in range(n):
        linha.append(int(input('Insira um número: ')))
        
    matriz.append(linha)
    
for i in range(m):
    for j in range(n):
        if matriz[i][j] == 0:
            quant += 1
            
print(quant)