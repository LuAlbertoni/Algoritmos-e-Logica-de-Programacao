#14. Faça um programa que calcule e apresente as tabuadas do 3 ao 7. Este exercício utiliza DUAS estruturas de repetição.

for i in range(3, 8):
  for j in range(1, 11):
    print(f'{i} * {j} = {i * j}')