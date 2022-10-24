# No estado de São Paulo, o IPVA (Imposto sobre a Propriedade de Veículos Automotores) possui valor da alíquota de imposto de 4%.
# Dependendo do ano de fabricação, pode ocorrer isenção de IPVA, ou seja, não é pago nada, referente a este imposto.
# O estado de São Paulo concede isenção a partir de 20 anos de fabricação.
# Atendendo a 10 proprietários de automóveis, a partir dos anos de fabricação e dos valores dos carros, crie um programa utilizando a linguagem Python que, calcule e apresente:
#   a) Quantidade de carros isentos.
#   b) Valor do IPVA de cada carro.
#   c) Média de valores dos carros.
#   d) Total dos IPVAs pagos.

# Curiosidade: O valor do carro geralmente é avaliado pela tabela FIPE (Fundação Instituto de Pesquisas Econômicas).

qntProprietarios = 10
mediaValores = 0
totalIPVA = 0
totalIsentos = 0

for i in range(qntProprietarios):
  ano = int(input('Insira o ano: '))
  valor = float(input('Insira o valor: '))

  mediaValores += valor

  if ano <= 2002:
    totalIsentos += 1
    print('Isento')
  else:
    valor *= 0.04
    totalIPVA += 1
    print(f'IPVA: {valor:.2f}')

print(f'Carros isentos: {totalIsentos} | Total de IPVAs pagos: {totalIPVA} | Média de valores dos carros: {mediaValores / qntProprietarios}')
