# Faça um programa que:
    # preencha um vetor com quinze elementos inteiros
    # verifique a existência de elementos iguais a 30, mostrando os índices/posições em que apareceram.
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

elementosArray = []
indicesArray = []

for i in range(15):
    elementosArray.append(int(input('Insira o número: ')))

for i in range(len(elementosArray)):
    if elementosArray[i] == 30:
        indicesArray.append(i)

if len(indicesArray) > 0:
    print(f'Elemento "30" encontrado no(s) índice(s) {indicesArray}')
else:
    print('Nenhum elemento igual a "30" localizado')