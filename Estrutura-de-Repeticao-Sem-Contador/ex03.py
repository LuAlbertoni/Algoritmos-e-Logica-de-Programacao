# Faça um programa que receba a altura de várias pessoas. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes. Para encerrar a entrada de dados, zero na altura, mas esta não poderá ser considerada como resposta da altura da pessoa mais baixa.

altura = float(input('Insira a altura ou "0" para finalizar: '))

maior = altura
menor = altura

while altura != 0:
  if altura != 0:
    if altura > maior:
      maior = altura
    elif altura < menor:
      menor = altura
      
  altura = float(input('Insira a altura ou "0" para finalizar: '))

print(f'Pessoa mais baixa: {menor:.2f}, pessoa mais alta: {maior:.2f}')