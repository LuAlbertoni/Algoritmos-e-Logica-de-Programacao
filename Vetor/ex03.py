# Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso, encontre qual a pessoa mais gorda e mais magra e apresente o nome o peso das mesmas.​ Use dois vetores, um para peso e outro para nome. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

nomeArray = []
pesoArray = []

pesada = 0
leve = 0

for i in range(10):
    nome = input('Insira o nome: ')
    nomeArray.append(nome)
    peso = float(input('Insira o peso: '))
    pesoArray.append(peso)

for i in range(len(pesoArray)):
    if pesoArray[i] > pesoArray[pesada]:
        pesada = i
    elif pesoArray[i] < pesoArray[leve]:
        leve = i

print(f'Pessoa mais pesada: {nomeArray[pesada]} com {pesoArray[pesada]}kg. Pessoa mais leve: {nomeArray[leve]} com {pesoArray[leve]}kg.')