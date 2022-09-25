# Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa de 1% para carros fabricados antes de 1990 e uma taxa de 1.5% para os fabricados de 1990 em diante, taxa esta incidindo sobre o valor de tabela do carro. Faça um algoritmo que leia o ano e o preço do carro, calcule e apresente o imposto a ser pago."""

preco = float(input("Insira o preço do carro: "))
ano = int(input("Insira o ano do carro: "))

if ano >= 1990:
  preco *= 0.015
else:
  preco *= 0.01

print("O imposto é de R$", preco)