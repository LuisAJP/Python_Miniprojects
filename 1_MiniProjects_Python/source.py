#https://www.youtube.com/watch?v=pxe13_562Vs&ab_channel=ThePyCoach
#convertir archivo py en exe
#https://www.youtube.com/watch?v=FFE1VNMAZfc&ab_channel=ThePyCoach

#%%
#---------------------------------------------------------------------
#1 Create multiple folders
import calendar
from pathlib import Path
months = list(calendar.month_name[1:])
# days=list(calendar.day_name)
#print(calendar.month(2023, 2))
days=['Dia 1','Dia 10','Dia 20','Dia 20','Dia 30' ]
for i,month in enumerate(months):
    for u,day in enumerate(days):
        Path(f'2022/{i+1} {month}/{u+1} {day}').mkdir(parents=True, exist_ok=True)



# %%
#---------------------------------------------------------------------
#2 Extract tables from html
import pandas as pd 
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
simpsons[5]



# %%
#---------------------------------------------------------------------
#3 Extract tables from pdf
#pip installl camelot-py no me funciona este ultimo ya luego investigare
import camelot
tabla=camelot.read_pdf('foo.pdf', pages='1')
print(tabla)
tabla.export('foo.csv', f='csv', compress=True)
tabla[0].to_csv('foo.csv')
# %%
