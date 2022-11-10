# Faça um programa que:
    # preencha um vetor com sete números inteiros
# Calcule e mostre:
    # os números múltiplos de 2;
    # os números múltiplos de 3;
    # os números múltiplos de 2 e de 3.
# Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

elementosArray = []
multiplos2Array = []
multiplos3Array = []

for i in range(7):
    # elementosArray.append(int(input('Insira o número: '))) # Caso queira adicionar manualmente
    elementosArray.append(i) # Adicionando automaticamente

    if elementosArray[i] % 2 == 0:
        multiplos2Array.append(elementosArray[i])
    elif elementosArray[i] % 3 == 0:
        multiplos3Array.append(elementosArray[i])

print(f'Números múltiplos de 2: {multiplos2Array}. Números múltiplos de 3: {multiplos3Array}. De ambos: {multiplos2Array + multiplos3Array}')