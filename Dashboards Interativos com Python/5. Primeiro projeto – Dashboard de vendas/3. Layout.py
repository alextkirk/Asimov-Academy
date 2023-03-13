import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server

# =================== Tratamento de Dados ============= #

df_data = pd.read_csv('supermarket_sales.csv') #A coluna Date esta como Object então precisa converter para datetime
df_data['Date'] = pd.to_datetime(df_data['Date'])


# =================== Layout ========================== #
app.layout = html.Div(children=[
    html.H6('Cidades:'),
    dcc.Checklist(df_data['City'].value_counts().index, df_data['City'].value_counts().index, id='check_city'),

    html.H5('Variável de Análise:'),
    dcc.RadioItems(['Gross Income', 'Rating'], 'Gross Income', id='main_variable'),

    dcc.Graph(id='city_fig'),
    dcc.Graph(id='pay_fig'),
    dcc.Graph(id='income_per_product_fig')
])

# =================== Callbacks ======================= #


# =================== Run server ====================== #
if __name__ == '__main__':
    app.run_server(port=8050, debug=True)