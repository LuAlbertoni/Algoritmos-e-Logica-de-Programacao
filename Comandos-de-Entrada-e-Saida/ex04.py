# Faça um programa que:
# * receba o salário de um funcionário
# * calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.

#       LEIA salario
#       novoSalario = salario + (salario * 25 / 100)
#       ESCREVA novoSalario


salario = float(input("Insira o salário atual: "))

novoSalario = salario + (salario * 25 / 100)

print(novoSalario)