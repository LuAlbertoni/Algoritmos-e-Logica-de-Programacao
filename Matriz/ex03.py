# Faça um programa que carregue uma matriz 3 x 2, que representa preços de produtos, crie OUTRA matriz que armazene todos os preços com 7% de aumento.

preco = []
aumento = []
for linha in range(3):
    vet_linha = []
    for coluna in range(2):
        vet_linha.append(float(input(f'Digite o preço[{linha}][{coluna}] R$: ')))
    preco.append(vet_linha)    

print('\nApresentação da matriz aumento........')
for linha in range(len(preco)):
    vet_linha = []
    for coluna in range(len(preco[0])):
        vet_linha.append(preco[linha][coluna]*7/100+preco[linha][coluna])
        print(vet_linha[coluna],end='\t')
    aumento.append(vet_linha)
    print()