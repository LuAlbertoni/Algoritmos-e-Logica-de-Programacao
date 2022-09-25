#6. Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a quantidade de pessoas maiores de idade, sendo que a maioridade é obtida após completar 18 anos. Pode implementar com o comando while ou for.

quant = 0

for i in range(10):
  idade = int(input('Insira sua idade: '))

  if idade >= 18:
    quant += 1

print(quant)