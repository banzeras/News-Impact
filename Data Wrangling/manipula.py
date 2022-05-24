#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas.core.frame import DataFrame
import os

pasta_buscada = 'fake-meta-information'

"""Verifica os arquivos na pasta"""
#print (os.listdir(pasta_buscada))

df_init=pd.DataFrame(columns=['Date','Emotion']) #Instancia o data frame vazio 

for arquivo in os.listdir(pasta_buscada):

    df = pd.read_csv(f'{pasta_buscada}/{arquivo}', header=None)

    celula_2d = df.loc[[3,23]]
    celula_2d = celula_2d.T 
    
    if '/' in celula_2d.iloc[0,0]:
        d = celula_2d.iloc[0, 0]
        d = d[6:10] + '-' + d[3:5] + '-' + d[0:2]
        if d == '0201-09-03':
            d=None
            celula_2d.iloc[0,3011]
        celula_2d.iloc[0, 0] = d
        
   
    df_init=df_init.append(celula_2d, ignore_index = True) 
   
df_init.drop(df_init.columns[[2,3]], axis=1, inplace=True)

df_emotion=df_init.set_axis(['Date', 'Emotion'], axis='columns')

pd.DataFrame(df_emotion).to_csv('date-order-fake-emotions.csv',index=False,header=False)

df_emotion['Date']=df_emotion['Date'].astype('datetime64[D]')



print(df_emotion.head(4))

print (df_emotion.dtypes)