import dash
from dash import html, dcc 
import plotly.express as px
import pandas as pd

#external_stylesheet = ['http://endereço.com']

app = dash.Dash(__name__) #, external_stylesheets = external_stylesheet)

app.layout = html.Div(id="div_0",
    children=[
        html.H1("Hello Dash", id="Hello"),
        html.Div("Dash: Um Framework Web para Python", style={"font-family":"Times New Roman"}),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)