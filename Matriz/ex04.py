# Faça um programa para armazenar em uma matriz 5x2 preços. Encontre e apresente os ÍNDICES dos valores menores que 23 reais.

matriz = []

for i in range(5):
    linha = []
    
    for j in range(2):
        linha.append(float(input('Insira o preço: ')))
        
    matriz.append(linha)
    
for i in range(5):
    for j in range(2):
        if matriz[i][j] < 23:
            print(f'Valor R$ {matriz[i][j]} encontrado na posição [{i}][{j}] da matriz')