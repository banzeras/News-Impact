#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from operator import index
import matplotlib.pyplot as plt
import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping

df=pd.read_csv("NewsImpact_Predictor/VALE.csv")
print("Quantidade de linhas e colunas:", df.shape, "\n")
print(df.head(4), "\n")

#O interessante para o presente trabalho é predizer o valor de fechamento da ação.

training_set = df.iloc[:800, 1:2].values
test_set = df.iloc[800:, 1:2].values

# Estamos analisando no intervalo diário
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)# Criação de uma estrutura de dados com 60 time-steps e 1 saída 
X_train = []
y_train = []
for i in range(60, 800):
    X_train.append(training_set_scaled[i-50:i, 0])#Alterei pra i-50 por causa da plotagem no gráfico fica melhor
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
#(740, 60, 1)


#Depois de remodular os valores
""" Observação: Dropout é um método de regularização onde as conexões de entrada 
e recorrentes para unidades LSTM são probabilisticamente excluídas da ativação e atualizações de peso durante o treinamento de uma rede.
 Isso tem o efeito de reduzir o sobreajuste e melhorar o desempenho do modelo."""

model = Sequential()#Adicionando a primeira camada LSTM e regularização de Dropout
model.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
model.add(Dropout(0.2))# Adicionando uma segunda camada LSTM e regularização de Dropout
model.add(LSTM(units = 50, return_sequences = True))
model.add(Dropout(0.2))# Adicionando uma terceira camada LSTM e regularização de Dropout
model.add(LSTM(units = 50, return_sequences = True))
model.add(Dropout(0.2))# Adicionando uma quarta camada LSTM e regularização de Dropout
model.add(LSTM(units = 50))
model.add(Dropout(0.2))# Adicionando a camada de saída
model.add(Dense(units = 1))# Compilando a RNN
model.compile(optimizer = 'adam', loss = 'mean_squared_error')# Ajustando a RNN ao conjunto de treinamento
model.fit(X_train, y_train, epochs = 100, batch_size = 32)

"""Observação: O tamanho do batch é um número de amostras processadas antes da atualização do modelo.
O número de epochs é o número de passagens completas pelo conjunto de dados de treinamento."""

# Obtendo o preço de ação previsto para 2017
dataset_train = df.iloc[:800, 1:2]
dataset_test = df.iloc[800:, 1:2]
dataset_total = pd.concat((dataset_train, dataset_test), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 519):
    X_test.append(inputs[i-50:i, 0])#Alterei pra i-50 por causa da plotagem no gráfico fica melhor alteirei para 60
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

print(X_test.shape)
# (459, 60, 1)


predicted_stock_price = model.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)


# Plotando os resultados
plt.plot(df.loc[800:, "Date"],dataset_test.values, color = "red", label = "Preço real das ações da VALE")
true_df = pd.DataFrame(dataset_test.values)
true_df.to_csv = ('TRUE_VALE.csv')
plt.plot(df.loc[800:, "Date"],predicted_stock_price, color = "green", label = "Preço previsto das ações da VALE")
prev_df = pd.DataFrame(predicted_stock_price, index=False)
prev_df.to_csv('prediction_VALE.csv')
plt.xticks(np.arange(0,459,50))
plt.title('Previsão do preço das ações da VALE')
plt.xlabel('Tempo')
plt.ylabel('Preço das ações da VALE')
plt.legend()
plt.show()
