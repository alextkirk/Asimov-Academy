import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash_bootstrap_templates import ThemeSwitchAIO

#=============================== App =========================================#
FONT_AWESOME = ['https://use.fontawesome.com/releases/v5.10.2/css/all.css']
dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.scripts.config.serve_locally = True
server = app.server

#============================== Styles ========================================#
template_theme1 = 'flatly'
template_theme2 = 'vapor'
url_theme_1 = dbc.themes.FLATLY
url_theme_2 = dbc.themes.VAPOR
tab_card={'height':'100%'}
#============================== Reading and cleaning File ======================#
df_main = pd.read_csv(r'C:\Users\alext\OneDrive - Contabifi\Documentos\Patches Python\Asimov Academy\Dashboards Interativos com Python\GasPrices – Dashboard de Análise da gasolina no Brasil\data_gas.csv')
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

df_main.drop(['UNIDADE DE MEDIDA', 'COEF DE VARIAÇÃO REVENDA', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO',
'NÚMERO DE POSTOS PESQUISADOS', 'DATA INICIAL', 'DATA FINAL', 'PREÇO MÁXIMO DISTRIBUIÇÃO',
'DESVIO PADRÃO DISTRIBUIÇÃO', 'MARGEM MÉDIA REVENDA', 'PREÇO MÍNIMO REVENDA', 'PREÇO MÁXIMO REVENDA',
'PRODUTO', 'PREÇO MÉDIO DISTRIBUIÇÃO'], inplace=True, axis=1)

df_store = df_main.to_dict()

#============================== Layout =========================================#
app.layout = dbc.Container(children=[

    # Armazenar o dataset
    dcc.Store(id='dateset', data=df_store),
    dcc.Store(id='dateset_fixed', data=df_store),

    # Layout
    #Row 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Legend('Gas Prices Analysis')
                        ], sm=8),
                        dbc.Col([
                            html.I(className='fa fa-filter', style={'font-size': '300%'})
                        ], sm=4, align='center')
                    ]),
                    dbc.Row([
                        dbc.Col([
                            ThemeSwitchAIO(aio_id='theme', themes=[url_theme_1, url_theme_2]),
                            html.Legend('Asimov Academy')
                        ])
                    ], style={'margin-top': '10px'}),
                    dbc.Row([
                        dbc.Col(
                            dbc.Button('Visite o Site', href='https://asmiov.academy/', target='blank')
                        )
                    ], style={'margin-top': '10px'})
                ])
            ], style=tab_card)
        ], sm=4, lg=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H3('Máximos e Mínimos'),
                            dcc.Graph(id='static-maxmin', config={'displayModeBar': False, 'showTips': False})
                        ])
                    ])
                ])
            ], style=tab_card)
        ], sm=8, lg=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Ano de Análise'),
                            dcc.Dropdown(
                                id='select_ano',
                                value= df_main.at[df_main.index[1], 'ANO'],
                                clearable=False,
                                className='dbc',
                                options=[
                                    {'label':x, 'value': x} for x in df_main.ANO.unique()
                                ]
                            )
                        ], sm=6),
                        dbc.Col([
                            html.H6('Região de análise:'),
                            dcc.Dropdown(
                                id='select_regiao',
                                value=df_main.at[df_main.index[1], 'REGIÃO'],
                                clearable= False,
                                className='dbc',
                                options=[
                                    {'label': x, 'value': x} for x in df_main.REGIÃO.unique()
                                ]
                            ),
                        ], sm=6)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='regiaobar_graph', config={'displayModeBar': False, 'showTips': False})
                        ], sm=12, md=6),
                        dbc.Col([
                            dcc.Graph(id='estadobar_graph', config={'displayModeBar': False, 'showTips': False})
                        ], sm=12, md=6),
                    ], style={'column-gap': '0px'})
                ])
            ], style=tab_card)
        ], sm=12, lg=6)
    ])

], fluid=True, style={'height': '100%'})


#============================== Callback ========================================#

#============================== Run App =========================================#
if __name__ == '__main__':
    app.run_server(debug=True)