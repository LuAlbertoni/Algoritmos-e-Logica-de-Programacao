#8. Faça um algoritmo que calcule e exiba o salário reajustado de dez funcionários de acordo com a seguinte regra (pode implementar com o comando while ou for): 

# Salário até 300, reajuste de 50%; 
# Salários maiores que 300, reajuste de 30%.

i = 0

while i < 10:
  sal = float(input('Insira o salário atual: '))
  
  if sal < 300:
    print('Novo salário:', sal + (sal * 0.5))
  else:
    print('Novo salário:', sal + (sal * 0.3))

  i += 1