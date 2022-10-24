# Um professor de uma instituição de ensino, pediu ajuda para você organizar as notas dos alunos de três provas, que ocorreram ao longo do semestre. Ele informou que para o aluno ser aprovado é necessário ter a média das notas igual a 7.
# O professor passou algumas diretrizes:
#   a) media = 7
#   b) numero_provas = 3
#   c) O aluno é considerado reprovado de forma direta, se não realizar uma das provas.

# Crie um programa utilizando a linguagem Python, para calcular e apresentar a média e avaliar a situação de aprovação ou não do aluno. Adote os nomes das variáveis apresentadas para o desenvolvimento e siga as diretrizes.

media = 7
numero_provas = 3
notas = 0
i = 0

while i < numero_provas:
  nota = float(input('Insira a nota ou "-1" para caso não tenha sido realizada: '))

  if nota == -1:
    i = numero_provas
    notas = -1
  else:
    notas += nota
    i += 1

if notas == -1 or (notas / numero_provas) < 7:
  print('Reprovado')
else:
  print('Aprovado')