import mysql.connector
import pandas as pd
import os
import plotly.graph_objects as go

os.system('cls')

def Pesquisa(Tabela):
    conexão = mysql.connector.connect(
        host='br468.hostgator.com.br',
        user='cont9917_contab',
        password='contabifi.com.br',
        database='cont9917_Sistema_de_Informacoes')

    consulta = conexão.cursor()
    consulta.execute("select * from " + Tabela)
    resultado = consulta.fetchall()
    return resultado

def Pesquisa_Nome_Colunas(Tabela):
    conexão = mysql.connector.connect(
        host='br468.hostgator.com.br',
        user='cont9917_contab',
        password='contabifi.com.br',
        database='cont9917_Sistema_de_Informacoes')

    consulta = conexão.cursor()
    consulta.execute("select * from " + Tabela)
    colunas = [column[0] for column in consulta.description]
    return colunas


Tabela_Pesquisa = 'Fundo_Responsavel'
Fundo_Responsavel = pd.DataFrame(Pesquisa(Tabela_Pesquisa), columns=Pesquisa_Nome_Colunas(Tabela_Pesquisa))
Responsavel_Nome = pd.DataFrame(Pesquisa('Prestador_de_Servico'), columns=Pesquisa_Nome_Colunas('Prestador_de_Servico'))

# ============ Gráfico de barras mostrando quantas entradas determinado prestador fez num mes de escrituração ======== 

# dados = Fundo_Responsavel[Fundo_Responsavel['Mes_Escrituracao'] == '11.2022']['ID_Prestador_Servico'].value_counts()
# df_dados = pd.DataFrame(data=dados.values, index=dados.index)
# df_dados.rename_axis('ID_Prestador_Servico', inplace=True)
# df_dados.rename(columns={0: 'Total de entradas no Mes'}, inplace=True)
# result = pd.merge(Responsavel_Nome, df_dados, how='outer', on='ID_Prestador_Servico')

# fundo_prestador_qtd = go.Figure(
#     data=[
#         go.Bar(x=result['Nome_Prestador'], y=result['Total de entradas no Mes'], hovertemplate='%{x} atualizou um total de %{y}x este mês')
#     ]
# )

# fundo_prestador_qtd.show()

