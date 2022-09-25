# Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário, número 1 para a escolha da soma, ou número 2 para a raiz quadrada, também receba os dados necessários para executar cada operação.

#     Menu de opções:
#     1. Somar dois números.
#     2. Raiz quadrada de um número.

# Observação: raiz = numero ** (1/2), ou 
# import math
# raiz = math.sqrt(numero), assim como foi programado no exercício 18, da lista anterior.

print("Menu de opções:\n"
"\n1. Somar dois números."
"\n2. Raiz quadrada de um número.")

option = int(input("\nInsira a opção desejada: "))

if option == 1:
    n1 = float(input("Insira o 1o número: "))
    n2 = float(input("Insira o 2o número: "))

    print(f"O resultado da soma de {n1:.2f} e {n2:.2f} é {n1 + n2:.2f}")
elif option == 2:
    n = float(input("Insira o número: "))

    print(f"A raiz quadrada de {n:.2f} é {n ** (1/2):.2f}")
else:
    print("Opção inválida!")
