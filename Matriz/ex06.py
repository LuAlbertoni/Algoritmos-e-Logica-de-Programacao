# Faça um programa que carregue: *um vetor com oito posições com os nomes das lojas; * um outro vetor com quatro posições com os nomes dos produtos; * uma matriz (8 x 4) com os preços de todos os produtos em cada loja. O programa deve mostrar todas as relações (nome da loja - nome do produto e preço), nas quais o preço não ultrapasse R$ 120,00.

nomesArray = []
produtosArray = []
matriz = []

for i in range(8):
    nomesArray.append(input('Insira o nome da loja: '))

for i in range(4):
    produtosArray.append(input('Insira o nome dos produtos: '))
    
for i in range(8):
    linha = []
    
    for j in range(4):
        linha.append(float(input(f'Insira o preço do {produtosArray[j]} na loja {nomesArray[i]}: ')))
        
    matriz.append(linha)
    
for i in range(8):
    for j in range(4):
        if matriz[i][j] <= 120:
            print(f'Loja "{nomesArray[i]}", produto "{produtosArray[j]}" e preço R$ {matriz[i][j]}')