# O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
# * o valor correspondente ao lucro do distribuidor;
# * o valor correspondente aos impostos;
# * o preço final do veículo.
#         LEIA preco_fabrica
#         LEIA percentual_lucro_distribuidor
#         LEIA percentual_imposto
#         lucro_distribuidor = preco_fabrica * percentual_lucro_distribuidor / 100
#         valor_imposto = preco_fabrica * percentual_imposto / 100
#         preco_final = preco_fabrica + lucro_distribuidor + valor_imposto
#         ESCREVA lucro_distribuidor
#         ESCREVA valor_imposto
#         ESCREVA preco_final

preco_fabrica = float(input("Insira o preço de fábrica: "))
percentual_lucro_distribuidor = float(input("Insira o percentual de lucro do distribuidor: "))
percentual_imposto = float(input("Insira o percentual de imposto: "))

lucro_distribuidor = preco_fabrica * percentual_lucro_distribuidor / 100
valor_imposto = preco_fabrica * percentual_imposto / 100
preco_final = preco_fabrica + lucro_distribuidor + valor_imposto

print("O lucro do distribuidor é de R$", lucro_distribuidor, ", o valor do imposto é de R$", valor_imposto, "e o preço final é de R$", preco_final)