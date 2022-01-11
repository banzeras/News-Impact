#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas.core.frame import DataFrame

"""
import os
files = os.listdir("fake-meta-information/")
myfile = 'filename.txt'

for filename in files:
    if filename == myfile:
        continue
"""


df = pd.read_csv('fake-meta-information/1-meta.txt', sep=" ", header=None)

celula_2d = df.loc[[3,23]]

"""Verifica Posição e o tipo dos dados no data frame celula_2d"""
#print (celula_2d.dtypes)
#print(celula_2d)

celula_2d = celula_2d.T #Transposição de linhas e colunas

"""Verifica se a transposição ocorreu."""
#print(celula_2d.dtypes)
#print(celula_2d)

"""Grava a data e o sentimento em um csv"""
pd.DataFrame(celula_2d).to_csv('Gravameta.csv',index=False,header=False)



