# Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.

custo = float(input("Insira o custo do espetáculo: "))
preco = float(input("Insira o preço do convite: "))

print("Para que o custo do espetáculo se pague, deverão ser vendidos cerca de", round(custo / preco), "convites.")