# Tendo como dados de entrada a altura e o gênero (M/F) de uma pessoa (M-masculino ou F-feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# masculino: (72.7 * altura) - 58;
# feminino: (62.1 * altura) - 44.7

altura = float(input("Insira a altura da pessoa: "))
sexo = input("Insira o sexo da pessoa (M/F): ")

if sexo == "m" or sexo  == "M":
  peso = (72.7 * altura) - 58
elif sexo == "f" or sexo == "F":
  peso = (62.1 * altura) - 44.7

print("Peso ideal é de", peso, "kg.")