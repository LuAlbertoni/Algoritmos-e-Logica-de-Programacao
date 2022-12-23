#  Foi realizada uma pesquisa sobre algumas características físicas de ALGUNS habitantes de uma região, NÃO FOI INFORMADA A QUANTIDADE TOTAL, então use como critério de parada, idade igual a zero para encerrar a repetição. Preste atenção nesse detalhe, pois somente poderá usar a função append, quando for digitado uma idade válida.
# Foram coletados os seguintes dados de cada habitante: idade, gênero (M/F), cor dos olhos (A - azuis ou V - verdes). Escolha se quer armazenar uma letra ou a palavra, para cor dos olhos.
# Em Python crie um programa que leia esses dados, armazenando-os em vetores, uma para idade, outro para gênero (apenas uma letra) e outro para cor dos olhos.
# Calcule e apresente:
#   Média de idades das pessoas com olhos verdes;
#   Quantidade de pessoas que foram entrevistadas com olhos verdes e quantidade com olhos azuis
#   Quantidade de pessoas do gênero masculino com idade entre 29 e 40 anos e que tenham olhos azuis.

# Observação: pode usar o operador in e a função len()e a append() apenas. Outras funções prontas da linguagem Python, não serão aceitas.

idade = 0
qntOlhosVerdes = 0
idadeOlhosVerdes = 0
olhosAzuisRestringido = 0

idadeArray = []
sexoArray = []
olhosArray = []

idade = int(input('Insira a idade: '))

while idade != 0:
  sexo = ''
  olhos = ''

  if idade > 0:
    while sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
      sexo = input('Insira o sexo da pessoa (M/F): ')

      if sexo == 'm' or sexo == 'M' or sexo == 'f' or sexo == 'F':
        while olhos != 'a' and olhos != 'A' and olhos != 'v' and olhos != 'V':
          olhos = input('Insira a cor do olho (A/V): ')

          if olhos == 'a' or olhos == 'A' or olhos == 'v' or olhos == 'V':
            idadeArray.append(idade)
            sexoArray.append(sexo)
            olhosArray.append(olhos)
          else:
            print('Cor inválida, insira outra.')
      else:
        print('Sexo inválido, insira outro.')
  else:
    print('Idade inválida, insira outra.')

  idade = int(input('Insira a idade: '))

for i in range(len(idadeArray)):
  if olhosArray[i] == 'v' or olhosArray[i] == 'V':
    qntOlhosVerdes += 1
    idadeOlhosVerdes += idadeArray[i]
  else:
    if sexoArray[i] == 'm' or sexoArray[i] == 'M':
      if idadeArray[i] > 29 and idadeArray[i] < 40:
        olhosAzuisRestringido += 1

if qntOlhosVerdes == 0:
  idadeOlhosVerdes = 0
else:
  idadeOlhosVerdes = idadeOlhosVerdes / qntOlhosVerdes

print(f'A média de idade das pessoas com olhos verdes é de {idadeOlhosVerdes:.2f} anos. Foram entrevistadas um total de {qntOlhosVerdes} pessoas com olhos verdes e {len(idadeArray) - qntOlhosVerdes} com olhos azuis. Foram entrevistadas {olhosAzuisRestringido} pessoas do sexo masculino com idade entre 29 e 40 anos e que possuem olhos azuis.')