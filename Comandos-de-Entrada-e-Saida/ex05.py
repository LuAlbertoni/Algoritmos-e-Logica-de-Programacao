# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

sal = float(input("Insira o salário atual: "))
perc = float(input("Insira o percentual de aumento: "))

aum = sal * perc / 100

print("O valor do aumento é de R$", aum)

print("O novo salário é de R$", sal + aum)