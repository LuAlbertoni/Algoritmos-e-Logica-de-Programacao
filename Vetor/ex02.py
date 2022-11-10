# Faça um programa que calcule e apresente a média de alturas de uma sala de 35 alunos. Informe também quantos alunos e quais (índice/posição) são os que possuem idade superior a 25 anos.​ Use dois vetores, um para altura e outro para idade. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

# Criação das listas
altura = []
idade = []
maiores = []

# Criação de variáveis
alturaTotal = 0

# Capturar valores
for i in range(35):
    alturaPessoa = float(input('Insira a altura: '))
    altura.append(alturaPessoa)
    idadePessoa = int(input('Insira a idade: '))
    idade.append(idadePessoa)

# Média de altura
for i in range(len(altura)):
    alturaTotal += altura[i]

    if idade[i] >= 25:
        maiores.append(i)

print(f'Média de altura: {alturaTotal / len(altura)}')

print(f'Maiores de idade: {len(maiores)}')

for i in range(len(maiores)):
    print(f'Idade: {idade[maiores[i]]:.2f}, altura: {altura[maiores[i]]:.2f}')