# Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre:

# * o valor de cada quilowatt;
# * o valor a ser pago por essa residência;
# * o valor a ser pago com desconto de 15%.
#       LEIA valor_salario
#       LEIA qtde_quilowatt
#       valor_quilowatt = valor_salario / 5
#       valor_em_reais = valor_quilowatt * qtde_quilowatt
#       valor_descontado = valor_em_reais * 15 / 100
#       valor_com_desconto =  valor_em_reais − valor_descontado
#       ESCREVA valor_quilowatt
#       ESCREVA valor_em_reais
#       ESCREVA valor_com_desconto

valor_salario = float(input("Insira o valor do salário: "))
qtde_quilowatt = float(input("Insira a quantidade de quilowatt: "))

valor_quilowatt = valor_salario / 5
valor_em_reais = valor_quilowatt * qtde_quilowatt
valor_descontado = valor_em_reais * 15 / 100
valor_com_desconto =  valor_em_reais - valor_descontado

print("O valor de quillowatt é de", valor_quilowatt, ", o valor é de R$", valor_em_reais, "e o valor com desconto é de R$", valor_com_desconto)