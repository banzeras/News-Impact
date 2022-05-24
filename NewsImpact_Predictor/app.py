import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import core



st.title('NEWS IMPACT')
st.subheader('**Predição com NLP**')
st.markdown('Este app faz a predição do valor de fechamento ajustado das ações.')
###################
#   barra lateral #
###################
option = st.sidebar.selectbox('Selecione uma ação: ', ( 'AGRO3.SA', 'FRTA3.SA',"SLCE3.SA"))

data_inicial =  datetime(2015,5,2)
data_final =  datetime(2017,11,30)

data_ini = st.sidebar.date_input('Data Inicial', data_inicial)
data_fin = st.sidebar.date_input('Data Final', data_final)

if data_ini < data_fin:
    st.sidebar.success('Data Inicial: `%s`\n\nData Final:`%s`' % (data_ini, data_fin))
else:
    st.sidebar.error('Erro: A data final deve começar após a data inicial.')

