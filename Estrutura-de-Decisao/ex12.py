# Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. Mostre uma mensagem informando o saldo médio e o valor do crédito.

#         Saldo médio
#         * de 0 a 200 nenhum crédito
#         * de 201 a  400 20% do valor do saldo médio
#         * de 401 a  600 30% do valor do saldo médio
#         * acima de 601 40% do valor do saldo médio

sal = float(input("Insira o salário médio: "))

if sal >= 0 and sal <= 200:
    print("Salário médio é de R$", sal, "e não há crédito disponível")
elif sal >= 201 and sal <= 400:
    print("Salário médio é de R$", sal, "e há R$", (sal * 0.2), "de crédito disponível")
elif sal >= 401 and sal <= 600:
    print("Salário médio é de R$", sal, "e há R$", (sal * 0.3), "de crédito disponível")
elif sal > 600:
    print("Salário médio é de R$", sal, "e há R$", (sal * 0.4), "de crédito disponível")