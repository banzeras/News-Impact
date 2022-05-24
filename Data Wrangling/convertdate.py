#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas.core.frame import DataFrame


df_open = pd.read_csv('fake-emotions_sorted.csv',header=None)

df_emotion=df_open.set_axis(['Date', 'Emotion'], axis='columns')

df_emotion['Date']=df_emotion['Date'].astype('datetime64[D]')


df_emotion = df_emotion.sort_values(by="Date")

df=df_emotion.groupby("Date").mean()


print(df.head(20))


pd.DataFrame(df).to_csv('new-fake-emotion2.csv',index=True,header=True)

