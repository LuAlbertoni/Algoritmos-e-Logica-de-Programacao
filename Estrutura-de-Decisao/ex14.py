# A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:

#  NOTA |  PESO |
#  ---|---
# Trabalho de laboratório  |   2   |
# Avaliação semestral      |   3   |
# Exame final              |   5   |

# Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela

# MÉDIA PONDERADA    | CONCEITO|
# ---|---
# 8,0 <= média <= 10  |    A 
# 7,0 <= média < 8,0  |    B 
# 6,0 <= média < 7,0  |    C 
# 5,0 <= média < 6,0  |    D 
#  0,0 <= média < 5,0  |    E
       
# media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10

trabalho = float(input("Insira a nota do trabalho: "))
avaliacao = float(input("Insira a nota da avaliação: "))
exame = float(input("Insira a nota do exame final: "))

notaFinal = ((trabalho * 0.2) + (avaliacao * 0.3) + (exame * 0.5))

if notaFinal >= 0 and notaFinal < 5:
    conceito = "E"
elif notaFinal >= 5 and notaFinal < 6:
    conceito = "D"
elif notaFinal >= 6 and notaFinal < 7:
    conceito = "C"
elif notaFinal >= 7 and notaFinal < 8:
    conceito = "B"
elif notaFinal >= 8 and notaFinal <= 10:
    conceito = "A"

print("Média ponderada", notaFinal, "e conceito", conceito)