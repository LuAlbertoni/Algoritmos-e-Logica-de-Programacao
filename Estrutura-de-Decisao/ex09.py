# Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

num = int(input("Insira o número: "))

if (num % 2) == 0:
  tipo = "par"
else:
  tipo = "ímpar"

if num >= 0:
  print("O número é positivo e", tipo)
else:
  print("O número é negativo e", tipo)