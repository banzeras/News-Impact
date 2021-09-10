#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd 
from pandas_datareader import data as dreader 
import matplotlib.pyplot as plt
from datetime import datetime
"""
Formato de datas aceito pelo datareader estão no Padrão Americano: Mês-Dia-ANO ou ANO-MÊS-DIA
Para evitar confusão decidi adotar, o padrão ANO-MÊS-DIA.
"""
#ANO-MÊS-DIA
#Mês-dia-ANO
#data_inicial = '2015-05-02'
#data_final = '2017-11-30'

data_inicial =  datetime(2015,5,2)
data_final =  datetime(2017,11,30)
"""
empresas_tickers = pd.read_excel("Equipamentos e Serviços.xlsx")

for empresa in empresas_tickers["Empresas"]: 
    print(f"{empresa}:")
    df = dreader.DataReader(f"{empresa}.SA", data_source='yahoo', start=data_inicial, end=data_final)
    print(df.head(4), "\n")
    df.to_csv(f"{empresa}.SA.csv", encoding='utf-8')

3.SA',

"""
tickers = ['VALE3.SA']

#for i in tickers:
    #dreader.DataReader(i,'yahoo',start=datetime(2015,5,2),end=datetime(2017,11,30)).to_csv(i+'.csv')

for i in tickers:
    try:
        dreader.DataReader(i, data_source='yahoo',start=data_inicial,end=data_final).to_csv(i+'.csv')
    except KeyError: #Exception caso a data da existência da ação não for compatível com o intervalo de tempo limitado.
        pass

    