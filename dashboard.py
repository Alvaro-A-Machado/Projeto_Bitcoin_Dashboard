import streamlit as st
import sqlite3
import pandas as pd


st.title("O Meu Primeiro Painel de Variação de Preço do Bitcoin")
st.write("Este painel foi construído 100% em Python!")

st.markdown("---")
st.subheader("Evolução do Preço do Bitcoin")

conexao = sqlite3.connect('banco_join.db')
df_bitcoin = pd.read_sql_query("SELECT * FROM Cotacoes_Bitcoin", conexao)
conexao.close()

if not df_bitcoin.empty:
    df_bitcoin = df_bitcoin.set_index('data_hora')
    st.subheader("Cotação do Bitcoin em Reais (BRL)")
    st.line_chart(df_bitcoin['preco_BRL'])
    st.subheader("Cotação do Bitcoin em Dólares (USD)")
    st.line_chart(df_bitcoin['preco_USD'])
else:
    st.info("Ainda não há dados históricos de Bitcoin recolhidos.")
