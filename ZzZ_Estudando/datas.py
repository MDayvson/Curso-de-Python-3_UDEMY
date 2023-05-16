from datetime import datetime
from dateutil.relativedelta import relativedelta


nasc = datetime(1987, 8, 26, 10, 30)
delta_anos = relativedelta(years=15)
data_final = nasc + delta_anos

print(f'{nasc} + {delta_anos}: {data_final}')

data_atual = datetime.now()
print(f'data atual: {data_atual}')

data_formatada = print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))

# tempo em segundos ate nasc
print(f'Segundos até nasc: {nasc.timestamp()}')

########################################################################
data_nasc = datetime.strptime('26/08/1987 10:30:00', '%d/%m/%Y %H:%M:%S')
data_atual = datetime.strptime('16/05/2023', '%d/%m/%Y')
idade = relativedelta(data_atual, data_nasc)
print(f'Idade: {idade}')
