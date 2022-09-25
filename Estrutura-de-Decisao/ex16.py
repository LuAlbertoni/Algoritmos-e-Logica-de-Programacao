# Faça um programa que receba dois números e mostre o maior.

num1 = float(input("Insira o 1o número: "))
num2 = float(input("Insira o 2o número: "))

if num1 > num2:
    print(num1, "é maior que", num2)
else:
    print(num2, "é maior que", num1)