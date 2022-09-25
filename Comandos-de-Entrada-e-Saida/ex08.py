# Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento de um mês.
#     rendimento = deposito * taxa / 100
#     total = deposito + rendimento

deposito = float(input("Valor do depósito: "))
taxa = float(input("Insira a taxa de juros: "))

rendimento = deposito * taxa / 100
total = deposito + rendimento

print(total)