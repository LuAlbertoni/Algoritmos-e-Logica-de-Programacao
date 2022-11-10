# Faça um programa que:
#   preencha um vetor com seis elementos numéricos inteiros.
# Calcule e mostre:

#   todos os números pares;
#   a quantidade de números pares;
#   todos os números ímpares;
#   a quantidade de números ímpares
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

elementosArray = []
imparesArray = []
paresArray = []
pares = 0

for i in range(6):
    # elementosArray.append(int(input('Insira o número: '))) # Caso queira adicionar manualmente
    elementosArray.append(i) # Adicionando automaticamente

    if elementosArray[i] % 2 != 0:
        imparesArray.append(elementosArray[i])
    else:
        paresArray.append(elementosArray[i])
        pares += 1

print(f'Números pares: {paresArray} ({len(paresArray)} itens). Números ímpares: {imparesArray} ({len(imparesArray)} itens).')