import streamlit as st
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import NewsImpact

###################
#   barra lateral #
###################
option = st.sidebar.selectbox('Selecione um ticker: ', ( 'AGRO3.SA', 'FRTA3.SA',"SLCE3.SA"))

data_inicial =  datetime(2015,5,2)
data_final =  datetime(2017,11,30)

data_ini = st.sidebar.date_input('Data Inicial', data_inicial)
data_fin = st.sidebar.date_input('Data Final', data_final)

if data_ini < data_fin:
    st.sidebar.success('Data Inicial: `%s`\n\nData Final:`%s`' % (data_ini, data_fin))
else:
    st.sidebar.error('Erro: A data final deve começar após a data inicial.')

##############
# CoreStock data #
##############


###################
# Set up main app #
###################

# Plot the prices and the bolinger bands
st.write('Stock Bollinger Bands')
st.line_chart(bb)

progress_bar = st.progress(0)

# Plot MACD
st.write('Stock Moving Average Convergence Divergence (MACD)')
st.area_chart(macd)

# Plot RSI
st.write('Stock RSI ')
st.line_chart(rsi)

# Data of recent days
st.write('Recent data ')
st.dataframe(df.tail(10))

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="download.xlsx">Download excel file</a>' # decode b'abc' => abc

st.markdown(get_table_download_link(df), unsafe_allow_html=True)
