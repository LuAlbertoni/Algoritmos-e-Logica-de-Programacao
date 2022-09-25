# Faça um algoritmo que leia duas notas de um aluno, calcule a média e verifique, apresentando, se está aprovado ou reprovado.

nota1 = float(input("Insira a 1a nota: "))
nota2 = float(input("Insira a 2a nota: "))

if ((nota1 + nota2) / 2) >= 6:
  print("Aluno aprovado")
else:
  print("Aluno reprovado")