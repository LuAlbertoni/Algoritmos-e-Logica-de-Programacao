# No final do ano muitas pessoas compram presentes. Faça um programa que registre alguns dados das pessoas, usando como critério de parada a letra ‘n’, para a pergunta “Deseja cadastrar outro (‘s’/’n’)?”, para identificar o perfil dos compradores numa loja de roupas e apresente como resultado a:
#   a) Quantidade de mulheres e de homens;
#   b) Quantidade de mulheres e de homens abaixo e acima de 18 anos.

homens = 0
mulheres = 0
homensMaiores = 0
mulheresMaiores = 0
homensMenores = 0
mulheresMenores = 0

res = input('Deseja cadastrar outro ("s"/"n")? ')

while res != 'N' and res != 'n':
    idade = int(input('Insira a idade: '))
    genero = input('Insira o gênero da pessoa ("h" para homem/"m" para mulher): ')

    if genero == 'h' or genero == 'H':
        homens += 1

        if idade >= 18:
            homensMaiores += 1
        else:
            homensMenores += 1
    elif genero == 'm' or genero == 'M':
        mulheres += 1

        if idade >= 18:
            mulheresMaiores += 1
        else:
            mulheresMenores += 1

    res = input('Deseja cadastrar outro ("s"/"n")? ')

print(f'Total homens: {homens}. Total mulheres: {mulheres}. Homens maiores: {homensMaiores}. Homens menores: {homensMenores}. Mulheres maiores: {mulheresMaiores}. Mulheres menores: {mulheresMenores}')