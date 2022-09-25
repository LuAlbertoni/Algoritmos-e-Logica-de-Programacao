#9. Faça um algoritmo que conheça 4 preços de produtos, some-os e mostre o resultado. Pode implementar com o comando while ou for.

precos = 0
i = 0

while i < 4:
  precos += float(input('Insira o preço do produto: '))
  i += 1

print(f'O preço total dos produtos é de R$ {precos}')