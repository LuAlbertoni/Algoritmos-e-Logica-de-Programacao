# Faça um programa que mostre a data e a hora do sistema nos seguintes formatos: **dia/mês/ano – mês por extenso e hora:minuto**.

# Observação: ***from*** carrega um módulo/biblioteca da linguagem Python e o ***import*** é usado para informar qual objeto desta biblioteca queremos importar/carregar no nosso programa

#     from datetime import datetime
#       # Este comando obtém a data e hora de hoje de algum país onde esta o servidor que executa nosso programa em Python.
#       # Quando eu testei, o servidor era do fuso horário de Dakar-Senegal
#     hoje = datetime.now()
#     print ('Ano atual.:',hoje.year)
#     print ('Mês.......:',hoje.month)
#     print ('Dia.......:',hoje.day)
#     print ('Hora......:',hoje.hour)
#     print ('Minuto....:',hoje.minute)
#     print ('Segundos..:',hoje.second)

# DICA - curiosidade, o trecho de código a seguir, mostra como trocar o fuso horário para o país que deseja

# from datetime import datetime, timezone, timedelta

# data_e_hora_atuais = datetime.now()
# fuso_horario = timezone(timedelta(hours=-3))
# print('UTC - Tempo Universal Coordenado:', fuso_horario)
# data_e_hora_SP = data_e_hora_atuais.astimezone(fuso_horario)
# data_e_hora_SP_em_texto = data_e_hora_SP.strftime('%d/%m/%Y %H:%M')
# print('Data e horário de São Paulo:',data_e_hora_SP_em_texto)

from datetime import datetime, timezone, timedelta

hoje = datetime.now()
fuso = timezone(timedelta(hours=-3))
dataTimeSP = hoje.astimezone(fuso)

month = dataTimeSP.strftime('%m')

if month == "01":
    month = "Janeiro"
elif month == "02":
    month =  "Fevereiro"
elif month == "03":
    month =  "Março"
elif month == "04":
    month =  "Abril"
elif month == "05":
    month =  "Maio"
elif month == "06":
    month =  "Junho"
elif month == "07":
    month =  "Julho"
elif month == "08":
    month =  "Agosto"
elif month == "09":
    month =  "Setembro"
elif month == "10":
    month =  "Outubro"
elif month == "11":
    month =  "Novembro"
elif month == "12":
    month =  "Dezembro"

dataTime = dataTimeSP.strftime(f'%d/%m/%Y - {month} - %H:%M ({fuso})')

print(dataTime)