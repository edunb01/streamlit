import streamlit as st
import numpy as np
import pandas as pd

# with open('../servicos.txt') as json_file:
#     data = json.load(json_file)

# dados = pd.DataFrame.from_dict(data['resposta'])
# digitais = dados.loc[(dados.servicoDigital),'nome'].sort_values()


st.write("Painel para visualização das recomendações de um serviço")

cooc_final = np.load('resumido300.npy')
tabela_servicos = pd.read_csv('servicos_com_id.csv',sep=";")
indice_servicos = np.load("indice_servicos.npy")
#number = st.number_input('Escolha a id do serviço',value=60)
#st.write(indice_servicos)
digitais = tabela_servicos.iloc[indice_servicos,1]
servico = st.selectbox('Escolha o serviço',digitais)

servico_indice = tabela_servicos.loc[tabela_servicos['nome']==servico,:].index[0]
#st.write(servico_indice)
linha_tabela =  np.where(indice_servicos == servico_indice)[0][0]
#st.write(indice_servicos==servico_indice)
servico_nome = tabela_servicos.iloc[servico_indice,1]
st.write("O serviço escolhido foi: " + servico)

st.write("Os serviços recomendados são:")
#st.write(linha_tabela)
aa = cooc_final[linha_tabela,].argsort()[::-1][1:10]
#st.write(aa)
st.write(tabela_servicos.loc[aa,'nome'])
