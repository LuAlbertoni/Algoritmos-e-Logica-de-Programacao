# Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: Salário até 500, reajuste de 50%; Salários maiores que 500, reajuste de 30%.

sal = float(input('Insira o salário: '))

if sal < 500:
  sal *= 1.5
else:
  sal *= 1.3

print("O salário foi reajustado e o novo valor é de R$", sal)