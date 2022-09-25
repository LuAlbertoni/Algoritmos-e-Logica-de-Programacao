# Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que o funcionário tem gratificação de 50,00 sobre o salário base e **paga** imposto que deve ser lido e é aplicado sobre o salário base.

#     LEIA salario, perImposto
#     imposto = salario * perImposto / 100
#     salario_a_receber = salario + 50 - imposto
#     ESCREVA salario_a_receber


salario = float(input("Insira o salário: "))
perImposto = float(input("Insira o imposto: "))

imposto = salario * perImposto / 100

salario_a_receber = salario + 50 - imposto

print(salario_a_receber)