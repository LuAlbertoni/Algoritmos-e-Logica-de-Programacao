# Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e **paga imposto** de 7% também sobre o salário base.

sal = float(input("Insira o salário base: "))

grat = sal + (sal * 5 / 100)

print(grat)

print("Valor do salário a receber R$", grat - (grat * 7 / 100))