# Faça um algoritmo que leia o nome e a idade de uma pessoa, verifique se a idade de uma pessoa é menor ou maior de idade. Considera-se maior de idade uma pessoa com 18 anos ou mais. Como saída o algoritmo deve informar o nome e a idade da pessoa e depois uma mensagem se ela é ou não maior de idade.

nome = input("Insira o nome: ")
idade = int(input("Insira a idade: "))

if idade >= 18:
  print(nome, "possui", idade, "anos, portanto é maior de idade")
else:
  print(nome, "possui", idade, "anos, portanto é menor de idade")