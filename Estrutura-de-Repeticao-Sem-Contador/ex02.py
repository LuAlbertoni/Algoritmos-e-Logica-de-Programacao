# Faça um programa que receba a altura de 5 pessoas. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes.

for pessoas in range(5):
    altura = float(input('Informe a altura: '))
    nome = input('Informe o nome: ')

    if pessoas == 0:
        alto = altura
        nomea = nome
        baixo = altura
        nomeb = nome
    if altura >= alto:
        alto = altura
        nomea = nome
    elif altura <= baixo:
        baixo = altura
        nomeb = nome
print(nomea,'é mais alto, com',alto,'metros')
print(nomeb,'é mais baixo, com',baixo,'metros')