# Faça um programa que carregue uma matriz 2 x 2, que representa o salário de 4 funcionários, calcule e mostre a soma total de todos os elementos que será o montante pago pela empresa a esses funcionários.

total = 0
matriz = []

for i in range(2):
    linha = []
    
    for j in range(2):
        linha.append(float(input('Insira o salário: ')))
    
    matriz.append(linha)
    
for i in range(2):
    for j in range(2):
        total += matriz[i][j]
        
print(f'R$ {total}')