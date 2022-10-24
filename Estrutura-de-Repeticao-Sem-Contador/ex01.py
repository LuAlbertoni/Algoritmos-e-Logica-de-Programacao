# Construir um algoritmo para calcular e apresentar o total de salários pagos de funcionários, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no salário para sair.

salario = float(input('...Para encerrar digite zero. Informe o salário R$ '))
total = 0
while salario > 0:
    total = total + salario
    salario = float(input('Para encerrar digite zero. Informe o salário R$ '))
print(f'Total de salários pagos R$ {total:.2f}')