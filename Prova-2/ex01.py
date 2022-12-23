# Em Python, crie um programa que leia a quantidade de linhas e colunas de uma matriz.
# Digite valores da matriz utilizando o tipo de dado int.
# Faça a soma dos valores que estão na diagonal principal, estes estarão armazenados nas linhas que são iguais as colunas, tem exeplo no slide de matriz. Apresente o resultado da soma.
# Mostre a matriz no formato de linha e colunas, conforme foi visto em aula.
# Observação: a implementação que foi feita além do que pede a prova, será descontada na nota.

matriz = []
somaDiagonal = 0

qnt_linhas = int(input('Insira a quantidade de linhas da matriz: '))
qnt_colunas = int(input('Insira a quantidade de colunas da matriz: '))

for i in range(qnt_colunas):
  linhas = []

  for j in range(qnt_linhas):
    num = int(input(f'Insira o número para ocupar a posição [{i}][{j}]: '))

    linhas.append(num)

    if i == j:
      somaDiagonal += num

  matriz.append(linhas)

print(f'Soma dos números da diagonal principal é igual a {somaDiagonal}. Matriz: ')
for i in range(qnt_colunas):
    print(matriz[i])