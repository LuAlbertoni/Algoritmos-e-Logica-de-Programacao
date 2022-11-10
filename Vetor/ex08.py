# Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores que receberão os elementos positivos e negativos e ao final apresente-os. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

elementos = []
positivos = []
negativos = []

for i in range(4):
    elementos.append(int(input('Insira o número: ')))

    if elementos[i] % 2 == 0:
        positivos.append(elementos[i])
    else:
        negativos.append(elementos[i])

print(f'Números positivos: {positivos}. Números negativos: {negativos}')