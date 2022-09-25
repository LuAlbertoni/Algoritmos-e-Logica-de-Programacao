# Faça um algoritmo que calcule e apresente o que foi requerido no exercício anterior e também avalie a condição de aprovar/reprovar, apenas quando o aluno tem frequência acima de 75%, este valor deve ser lido.

nota1 = float(input("Insira a 1a nota: "))
nota2 = float(input("Insira a 2a nota: "))
freq = int(input("Insira a frequência do aluno: "))

if freq >= 75:
  if ((nota1 + nota2) / 2) >= 6:
    print("Aluno aprovado")
  else:
    print("Aluno reprovado")
else:
  print("Frequência baixa")