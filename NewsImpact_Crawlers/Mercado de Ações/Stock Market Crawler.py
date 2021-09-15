#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd 
from pandas_datareader import data as dreader 
from datetime import datetime

data_inicial =  datetime(2015,5,2)
data_final =  datetime(2017,11,30)


tickers = pd.read_csv("Equipamentos e Serviços.csv")

for i in tickers:
    try:
        dreader.DataReader(i+'.SA', data_source='yahoo',
        start=data_inicial,end=data_final).to_csv(i+'.csv')
        
    except KeyError: #Exceção para caso a data da existência da ação
    #Não for compatível com o intervalo de tempo limitado.
    
        print(' A ação ' + i +
        ' não se encontra no intervalo de tempo pesquisado.')
        pass
