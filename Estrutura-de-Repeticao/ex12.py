#12. Faça um programa que receba a idade e a altura de 20 pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos.

alturaMedia = 0
quant = 0
i = 0

while i < 2:
  idade = int(input('Insira sua idade: '))
  altura = float(input('Insira sua altura: '))

  if idade > 20:
    quant += 1
    alturaMedia += altura
 
  i += 1

print(f'Média de altura de pessoas com mais de 20 anos é de {alturaMedia / quant}')