# 15. Faça um programa para o curso de ADS (6 módulos), cada sala tem 30 alunos, calcule e apresente os seguintes itens:
# *  Quantidade de homens e mulheres de cada módulo;
# *  Média de idades de cada módulo;
# *  Quantidade de homens e mulheres do curso todo;
# *  Média de idades do curso todo.

# Observação: este exercício utiliza DUAS estruturas de repetição.

homensCurso = 0
mulheresCurso = 0
idadesCurso = 0

for modulo in range(1, 7):
    print(modulo,'º módulo:')

    homensModulo = 0
    mulheresModulo = 0
    idadesModulo = 0
    idade = 0

    for alunos in range(30):
      genero = input('Insira o sexo (M ou F): ')
      idade += int(input('Insira a idade: '))

      if genero == 'M' or genero == 'm':
        homensModulo += 1
        homensCurso += 1
        idadesModulo += idade
        idadesCurso += idade
      elif genero == 'F' or genero == 'f':
        mulheresModulo += 1
        mulheresCurso += 1
        idadesModulo += idade
        idadesCurso += idade
      
    print(f'Quantidade de homens no módulo: {homensModulo}. Quantidade de mulheres no módulo: {mulheresModulo}. Idade média: {idadesModulo / 30}')

print(f'Quantidade de homens no curso: {homensCurso}. Quantidade de mulheres no curso: {mulheresCurso}. Idade média: {idadesCurso / (homensCurso + mulheresCurso)}')