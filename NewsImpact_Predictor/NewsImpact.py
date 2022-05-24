#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

acao='AGRO3.SA'

df=pd.read_csv(f'{acao}.csv', index_col="Date",)

df_emotion=pd.read_csv("new-fake-emotion2.csv", index_col="Date")

#Une os datasets criando um novo, que possua as datas iguais.
m = pd.merge(df, df_emotion, how = 'inner', on = 'Date') 

#Excluí valores nulos.

m.dropna(inplace=True) 
#print (m.tail(10))

#print(m)

# Dataframe com Adj close e emotion
m = m[["Adj Close", 'Emotion']]

print (m.head(10))

# Percentual de mudança entre o valor atual e o anterior do Adj Close
m["% Change Adj Close"] = m["Adj Close"].pct_change()

#Excluí valores nulos.
m.dropna(inplace = True)
print (m.head(10))

'''Com Emoções'''
# A função "intervalo_dados" aceita o número da coluna para os features (X) e o target (y) para a regressão
# Ele fragmenta os dados em um intervalo de Xt-n para prever Xt
# Retornando um vetor numpy de X para qualquer target (y)
def intervalo_dados(m, intervalo, col_1, col_2, col_dest):
    # Cria listas vazias "X_Fechamento_Ajustado", "X_Emotion" e y
    X_Fechamento_Ajustado = []
    X_Emotion = []
    y = []
    for i in range(len(m) - intervalo):
        
        # Get fechamento_ajustado, fake_news_emotion, e target
        Fechamento_ajustado = m.iloc[i:(i + intervalo), col_1]
        emotion = m.iloc[i:(i + intervalo), col_2]
        target = m.iloc[(i + intervalo), col_dest]
        
        # Insere os valores na última posição dos vetores
        X_Fechamento_Ajustado.append(Fechamento_ajustado)
        X_Emotion.append(emotion)
        y.append(target)
    #Criando Variável pra receber um array numpy de X para qualquer target (y)
    vetor = np.hstack((X_Fechamento_Ajustado,X_Emotion)), np.array(y).reshape(-1, 1)  
    return vetor



#Seta o intervalo de dias dos preços de adj close anteriores para predição
dias_intervalo = 1

# Col==0 é a coluna Adj Close 
# Col==1 é a coluna Emotion
# Col_dest == 0, é a coluna target do algoritmo
col_1 = 0
col_2 = 1
col_dest = 0

X, y = intervalo_dados(m, dias_intervalo, col_1, col_2, col_dest)

# Divide o dataset em 75% para treinamento
X_split = int(0.75 * len(X))
y_split = int(0.75 * len(y))

# Seta os conjuntos de dados para treinamento e teste
X_treino = X[: X_split]
X_teste = X[X_split:]
y_treino = y[: y_split]
y_teste = y[y_split:]

#Usando o MinMaxScaler() pra alterar a escala dos dados para ficar entre 0 e 1.
X_treino_escala = MinMaxScaler()
X_teste_escala = MinMaxScaler()
y_treino_escala = MinMaxScaler()
y_teste_escala = MinMaxScaler()

# Fit da escala pros conjuntos de treinamento
X_treino_escala.fit(X_treino)
y_treino_escala.fit(y_treino)

# Escala o conjunto de treinamento
X_treino = X_treino_escala.transform(X_treino)
y_treino = y_treino_escala.transform(y_treino)

# Fit da escala pros conjuntos de teste
X_teste_escala.fit(X_teste)
y_teste_escala.fit(y_teste)

# Escala o conjunto de teste
X_teste = X_teste_escala.transform(X_teste)
y_teste = y_teste_escala.transform(y_teste)

# Instanciando o modelo de XGBoost Regressor
modelo = XGBRegressor(objective='reg:squarederror', n_estimators=1000)

# Printa os parâmetros do modelo e transformando a lista de treino pra 1 dimensão (que é o tipo de dados aceito)
#print(modelo.fit(X_treino, y_treino.ravel()))
#print(modelo.fit(X_treino, y_treino.ravel())).to_csv('parametros-xgbRegressor.txt',index=True,header=True)
f = open("Parâmetros xgbRegressor/Parâmetros xgbRegressor "+acao+".txt", "w")
f.write(f'{modelo.fit(X_treino, y_treino.ravel())}' )
f.close()
# Fazendo a predição
predito = modelo.predict(X_teste)

# Avaliando o modelo
print('Média do erro quadrado:', np.sqrt(mean_squared_error(y_teste, predito)))
print('R² :', r2_score(y_teste, predito))

f = open("Avaliação xgbRegressor/Avaliação xgbRegressor "+acao+".txt", "w")
f.write('Média do erro quadrado: ' + f'{np.sqrt(mean_squared_error(y_teste, predito))}'+
'\nR² : '+ f'{r2_score(y_teste, predito)}')
f.close()

# Converte os valores pra escala original
preco_predito = y_teste_escala.inverse_transform(predito.reshape(-1, 1))
preco_real = y_teste_escala.inverse_transform(y_teste.reshape(-1, 1))

# Criação de um data frame para armazenar os valores reais e previstos
df_final = pd.DataFrame({"Real": preco_real.ravel(),"Predição": preco_predito.ravel()},
index = m.index[-len(preco_real): ]) 
#print (df_final.head(20))

pd.DataFrame(df_final).to_csv('saida'+acao+'.csv',index=True,header=True)
#Plotagem
nome_img = "Peço Real vs Preço Previsto da "+ acao

df_final.plot(title = "Peço Real vs Preço Previsto da "+ acao)
plt.ylabel('Preço das ações da' + acao)
plt.xlabel('Data')
plt.savefig(nome_img +'.png')
plt.show()

