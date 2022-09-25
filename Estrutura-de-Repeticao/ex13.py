#13. Faça um algoritmo que leia o preço de 20 TV, determine e apresente a média dos preços que possuem valor maior que R$ 1000. Pode implementar com o comando while ou for.

precosMedia = 0
quant = 0
i = 0

while i < 20:
  preco = float(input('Insira o preço da TV: '))

  if preco > 1000:
    precosMedia += preco
    quant += 1

  i += 1

print(f'O preço médio das TV que custam mais que R$ 1.000 é de R$ {precosMedia / quant}')