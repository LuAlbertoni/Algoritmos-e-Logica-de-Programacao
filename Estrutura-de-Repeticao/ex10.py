#10. Faça um algoritmo que calcule e informe a média de idades de 5 alunos. Pode implementar com o comando while ou for.

idade = 0
i = 0

while i < 5:
  idade += int(input('Insira a idade: '))
  i += 1

print(f'A média de idades dos 5 alunos é de {idade / 5} anos.')