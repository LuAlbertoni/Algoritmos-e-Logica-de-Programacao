#7. Escreva um algoritmo que receba 23 números, calcule e exiba a quantidade de números pares e impares. Pode implementar com o comando while ou for.

par = 0
impar = 0
i = 0

while i < 23:
  num = int(input('Insira o número: '))

  if num % 2 == 0:
    par += 1
  else:
    impar += 1

  i += 1

print(f'Pares: {par}. Ímpar: {impar}')