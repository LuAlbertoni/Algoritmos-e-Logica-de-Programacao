#Faça um algoritmo que leia o gênero de uma pessoa. Se for digitado M ou F, apresentar 'Gênero válido!'. Caso contrário, 'Gênero inválido!'."""

value = input("Insira: ")

if value != "M" and value != "F" and value != "m" and value != "f":
  print("Inválido")
else:
  print("Válido")