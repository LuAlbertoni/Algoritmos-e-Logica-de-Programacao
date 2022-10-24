# Você está em uma festa de aniversário e está tendo confusão para distribuir de modo justo a quantidade de brigadeiros entre os participantes.
# Todos, por alguma coincidência, entendem de Python, então você planeja o seguinte exemplo de código:
#   brigadeiros = 150
#   pessoas = 16
#   Por você ter feito a conta e evitado aumento da confusão, todos decidiram dar a você além da divisão justa, o resto dos brigadeiros que sobraram da conta.

# Crie um algoritmo utilizando a linguagem Python para calcular e apresentar a sua quantidade de brigadeiros. Adote os nomes das variáveis apresentadas para o desenvolvimento e siga o planejamento.

brigadeiros = 150
pessoas = 16

resto = brigadeiros % 16
divisaoBrigadeiros = (brigadeiros - resto) / pessoas

print(divisaoBrigadeiros + resto)