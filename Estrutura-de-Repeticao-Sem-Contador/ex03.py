# Faça um programa que receba a altura de várias pessoas. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes. Para encerrar a entrada de dados, zero na altura, mas esta não poderá ser considerada como resposta da altura da pessoa mais baixa.

altura = float(input('Insira a altura: '))
nome = input('Insira o nome da pessoa: ')

maior = altura
menor = altura
nomeMaior = nome
nomeMenor = nome

while altura != 0:
  if altura != 0:
    if altura > maior:
      nomeMaior = nome
      maior = altura
    elif altura < menor:
      nomeMenor = nome
      menor = altura
      
  altura = float(input('Insira a altura ou "0" para finalizar: '))

  if altura != 0:
    nome = input('Insira o nome da pessoa: ')


print(f'Pessoa mais baixa: {nomeMenor} - {menor:.2f}, pessoa mais alta: {nomeMaior} - {maior:.2f}')