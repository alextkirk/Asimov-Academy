import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash_bootstrap_templates import ThemeSwitchAIO

#=============================== App =========================================#
FONT_AWESOME = []
dbc_css = []

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.scripts.config.serve_locally = True
server = app.server

#============================== Styles ========================================#
template_theme1 = 'flatly'
template_theme2 = 'vapor'
url_theme_1 = dbc.themes.FLATLY
url_theme_2 = dbc.themes.VAPOR

#============================== Reading and cleaning File ======================#
df_main = pd.read_csv('data_gas.csv')
#df_main.info()
df_main['DATA INICIAL'] = pd.to_datetime(df_main['DATA INICIAL'])
df_main['DATA FINAL'] = pd.to_datetime(df_main['DATA FINAL'])

df_main['DATA MEDIA'] = ((df_main['DATA FINAL'] - df_main['DATA INICIAL']) / 2) + df_main['DATA INICIAL']
df_main = df_main.sort_values(by='DATA MEDIA', ascending=True)
df_main.rename(columns= {'DATA MEDIA': 'DATA'}, inplace=True)
df_main.rename(columns= {'PREÇO MÉDIO REVENDA': 'VALOR REVENDA (R$/L)'}, inplace=True)

df_main['ANO'] = df_main['DATA'].apply(lambda x: str(x.year))

df_main = df_main[df_main.PRODUTO == 'GASOLINA COMUM']

df_main = df_main.reset_index()

df_main.drop(['UNIDADE DE MEDIDA', 'COEF DE VARIÂO REVENDA', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO',
'NÚMERO DE POSTOS PESQUISADOS', 'DATA INICIAL', 'DATA FINAL', 'PREÇO MÁXIMO DISTRIBUIÇÃO',
'DESVIO PADRÂO DISTRIBUIÇÃO', 'MARGEM MÉDIA REVENDA', 'PREÇO MÍNIMO REVENDA', 'PREÇO MÁXIMO REVENDA',
'PRODUTO', 'PREÇO MÉDIO DISTRIBUIÇÃO'], inplace=True, axis=1)

#============================== Layout =========================================#
app.layout = dbc.Container(children=[

], fluid=True, style={'height': 100%})


#============================== Callback ========================================#

#============================== Run App =========================================#
if __name__ == '__main__':
    app.run_server(debug=True)