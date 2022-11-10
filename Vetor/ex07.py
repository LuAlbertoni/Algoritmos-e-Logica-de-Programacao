# Faça um algoritmo que calcule e apresente a média de alturas superior a 1,80 de 10 alunos. Informe também quantos e quais (índice/posição) são os alunos. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

alturaArray = []
nomeArray = []
maiores = []

media = 0

for i in range(10):
    nomeArray.append(input('Insira o nome: '))
    alturaArray.append(float(input('Insira a altura: ')))

    if alturaArray[i] > 1.8:
        maiores.append(i)
        media += alturaArray[i]
        print(alturaArray[i])

print(media)
media /= len(maiores)

print(f'Média de altura: {media:.2f}. Quantidade: {len(maiores)}. Índices: {maiores}')