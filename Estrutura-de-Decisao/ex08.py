# Uma faculdade faz o pagamento de seus professores por hora/aula. Faça um algoritmo que receba o nível e a quantidade de hora/aula, calcule e exiba o salário de um professor e a frase a seguira tabela abaixo:
# Professor Nível 1 - 11,00 reais por hora/aula, salário: ...

# Professor Nível 2 - 15,00 reais por hora/aula, salário: ...

# Professor Nível 3 - 19,00 reais por hora/aula, salário: ...

nivel = int(input("Insira o nível do professor: "))
horas = int(input("Insira a quantidade de horas de aulas dadas: "))

if nivel == 1:
  print("O salário deve ser de R$", horas * 11)
elif nivel == 2:
  print("O salário deve ser de R$", horas * 15)
elif nivel == 3:
  print("O salário deve ser de R$", horas * 19)