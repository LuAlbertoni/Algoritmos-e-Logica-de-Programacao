#  Faça um programa que leia uma matriz 2x3 (2 linhas, 3 colunas). Apresente os elementos da matriz e seus respectivos índices.

matriz = []

for lin in range(2):
    vet_linha = []
    for col in range(3):
        vet_linha.append(int(input(f'Digite o valor de [{lin}][{col}]: ')))
        print(vet_linha)
    print(vet_linha)
    matriz.append(vet_linha)
    print(matriz)
print(matriz)

print('\n\nApresentação do conteúdo da matriz')
print('.'*50)
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(matriz[linha][coluna], end='\t')