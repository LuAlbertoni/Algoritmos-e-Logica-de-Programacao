# Faça um programa que receba três números e mostre-os em ordem crescente. Suponha que o usuário digitará três números diferentes.

# SE numero1 < numero2 E numero1 < numero3
#     SE numero2 < numero3
#         ESCREVA “A ordem crescente é: “,numero1,“-”,numero2,“-”,numero3
#     SENÃO
#         ESCREVA “A ordem crescente é: “,numero1,“-”,numero3,“-”,numero2
# SE numero2 < numero1 E numero2 < numero3
#     SE numero1 < numero3
#         ESCREVA “A ordem crescente é: “,numero2,“-”,numero1,“-”,numero3
#     SENÃO
#         ESCREVA “A ordem crescente é: “,numero2,“-”,numero3,“-”,numero1
# SE numero3 < numero1 E numero3 < num2
#     SE numero1 < numero2
#         ESCREVA “A ordem crescente é: “,numero3,“-”,numero1,“-”,numero2
#     SENÃO 
#         ESCREVA “A ordem crescente é: “,numero3,“-”,numero2,“-”,numero1

num1 = float(input("Insira o 1o número: "))
num2 = float(input("Insira o 2o número: "))
num3 = float(input("Insira o 3o número: "))

if num1 > num2:
    if num2 > num3:
        print(num3, "-", num2, "-", num1)
    else:
        print(num2, "-", num3, "-", num1)
else:
    if num1 > num3:
        print(num3, "-", num1, "-", num2)
    else:
        if num3 > num2:
            print(num1, "-", num2, "-", num3)
        else:
            print(num1, "-", num3, "-", num2)