#Faça um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia.
#Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias.
from datetime import datetime, timedelta 
from calendar import isleap

data_atual = datetime.now() 
amanha = data_atual + timedelta(1) 
  
print("A próxima data será: ", amanha.strftime('%d/%m/%Y'))

ano = int(amanha.strftime('%Y'))
if isleap(ano):
    print('...E o ano será bissexto')
else:
    print('...E o ano não será bissexto')