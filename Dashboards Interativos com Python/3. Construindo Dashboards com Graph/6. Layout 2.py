import dash
from dash import html, dcc 
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        id="dp-1",
        options=[{'label': 'Rio Grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Rio de Janeiro', 'value': 'RJ'},],
            value=''
    ),
    html.Label("Checklist"),
    dcc.Checklist(
        id="cl-1",
        options=[{'label': 'Rio Grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Rio de Janeiro', 'value': 'RJ'},],
            value=['']),
    html.Label('Text Input'),
    dcc.Input(value= 'Digite o que quiser', type='text',style={'margin-left': 10}),
    html.Label('Slider'),
    dcc.Slider(
        min=0, 
        max=9, 
        marks=None, 
        value=5,
        ),
])

if __name__ == '__main__':
    app.run_server(debug=True)

#  ===============
