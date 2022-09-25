# Faça um programa que receba um número, calcule e mostre:
# * O número digitado ao quadrado
# * O número digitado ao cubo
# * A raiz do número digitado
# * A raiz cúbica do número digitado

#       LEIA numero
#       quadrado = numero ** 2
#       cubo = numero ** 3
#       raiz_quadrada = numero ** (½) (meio, ou 0.5)
#       raiz_cubica = numero ** (⅓) (um terço, ou 0.33)
#       ESCREVA quadrado, cubo, raiz_quadrada, raiz_cubica


#       raiz_quadrada = numero ** (1/2) ou
#       raiz_quadrada = numero ** 0.5

num = float(input("Insira o número: "))

print("Número digitado ao quadrado:", num ** 2)
print("Número digitado ao cubo:", num ** 3)
print("Raíz quadrada do número digitado:", num ** 0.5)
print("Raíz cúbica do número digitado:", num ** 0.33)