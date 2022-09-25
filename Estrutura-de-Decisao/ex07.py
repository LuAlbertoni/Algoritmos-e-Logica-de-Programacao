# Faça um algoritmo que leia dois números inteiros e mostre o resultado da **diferença** do maior valor pelo menor."""

num1 = int(input("Insira o 1o número: "))
num2 = int(input("Insira o 2o número: "))

if num1 > num2:
  print("A diferença entre", num1, "e", num2, "é de", num1 - num2)
else:
  print("A diferença entre", num2, "e", num1, "é de", num2 - num1)