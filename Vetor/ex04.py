# Faça um programa que carregue um vetor com a média de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

notasArray = []
media = 0
acima = 0

for i in range(10):
    nota = float(input('Insira a nota: '))
    notasArray.append(nota)

for i in range(len(notasArray)):
    media += notasArray[i] / len(notasArray)

for i in range(len(notasArray)):
    if nota >= media:
        acima += 1

print(f'A média da sala é {media:.2f}. {acima} estão acima da média e {len(notasArray) - acima} estão abaixo.')