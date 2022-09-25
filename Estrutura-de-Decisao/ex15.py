# Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exigida é 6,0.

# MÉDIA ARITMÉTICA | MENSAGEM
#     ---|---
#     0 <= média < 3 |Reprovado
#     3 <= média < 6|Exame
#     6 <= média <= 10|Aprovado

# ```
# SE media >= 3 E media < 6
#     ESCREVA “Exame”
#     nota_exame = 12 - media
#     ESCREVA “Você deve tirar a nota”, nota_exame, “para ser aprovado.”

nota1 = float(input("Insira a 1a nota: "))
nota2 = float(input("Insira a 2a nota: "))
nota3 = float(input("Insira a 3a nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 0 and media < 3:
    print("Reprovado!")
elif media >= 3 and media < 6:
    print("Exame! Você deve tirar", (12 - media), "para ser aprovado")
elif media >= 6 and media <= 10:
    print("Aprovado")