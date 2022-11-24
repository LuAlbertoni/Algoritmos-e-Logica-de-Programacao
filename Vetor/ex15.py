# Faça um programa que:
#   preencha um vetor com quinze números
# Determine e mostre:
#   o maior número e a posição por ele ocupada no vetor
#   o menor número e a posição por ele ocupada no vetor
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

numArray = []

for i in range(15):
    numArray.append(int(input('Insira o número: ')))

maior = 0
menor = 0

for i in range(len(numArray)):
    if numArray[i] > numArray[maior]:
        maior = i
    elif numArray[i] < numArray[menor]:
        menor = i

print(f'Maior número é {numArray[maior]} na posição {maior}. Menor número é {numArray[menor]} na posição {menor}')