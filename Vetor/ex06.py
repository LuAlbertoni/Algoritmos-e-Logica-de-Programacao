# Faça um programa que carregue um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

nomeArray = []

for i in range(10):
    nomeArray.append(input('Insira o nome: '))

nome = input('Insira o nome que deseja buscar: ')

for i in range(len(nomeArray)):
    if(nome == nomeArray[i]):
        print('Nome encontrado!')