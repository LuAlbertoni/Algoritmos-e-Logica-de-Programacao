# Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra. Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.

# SE numero4 > numero3
#     ESCREVA “A ordem decrescente é: “,numero4,“-”,numero3,“-”,numero2,“-”,numero1
# SENÃO SE numero4 > numero2 E numero4 < numero3
#     ESCREVA “A ordem decrescente é: “,numero3,“-”,numero4,“-”,numero2,“-”,numero1
# SENÃO SE numero4 > numero1 E numero4 < numero2
#     ESCREVA “A ordem decrescente é: “,numero3,“-”,numero2,“-”,numero4, “-”,numero1
# SENÃO SE numero4 < numero1
#     ESCREVA “A ordem decrescente é: “,numero3,“-”,numero2,“-”,numero1,“-”,numero4

num2 = 0
num3 = 0

num1 = float(input("Insira um número: "))

while num1 > num2:
    num2 = float(input(f"Insira um número maior que {num1}: "))

while num1 > num3 and num2 > num3:
    num3 = float(input(f"Insira um número maior que {num2}: "))

num4 = float(input("Insira mais um número: "))

if num4 > num3:
    print(num4, num3, num2, num1)
elif num4 > num2 and num4 < num3:
    print(num3, num4, num2, num1)
elif num4 > num1 and num4 < num2:
    print(num3, num2, num4, num1)
else:
    print(num3, num2, num1, num4)