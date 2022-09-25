# Sabe-se que:

# * pé = 12 polegadas
# * 1 jarda = 3 pés
# * 1 milha = 1760 jarda

# Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.

# * Polegadas;
# * Jardas;
# * Milhas.

#       LEIA pes
#       polegadas = pes * 12
#       jardas = pes / 3
#       milhas = jardas / 1760
#       ESCREVA polegadas, jardas, milhas

pes = float(input("Insira a medida em pés: "))

polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

print("Medida em polegadas:", polegadas, ". Medida em jardas:", jardas, ". Medida em milhas:",  milhas)