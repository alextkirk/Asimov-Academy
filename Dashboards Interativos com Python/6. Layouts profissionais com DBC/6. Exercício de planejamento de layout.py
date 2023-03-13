import dash_bootstrap_components as dbc
from dash import html
import dash


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

#==================== Card =============================#
card_content = [
    dbc.CardHeader('Card Header'),
    dbc.CardBody([
        html.H5('Card Title', className='card-title'),
        html.P(
            'This is some card content that we will reuse',
            className='card-text',
        ),
    ]),
]


#==================== Layout ===========================#
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(card_content, color='primary', inverse=True, style={'height': '100vh'}),
        ], sm=2),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color='info', inverse=True)),
                dbc.Col(dbc.Card(card_content, color='info', inverse=True))
                ]),
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color='warning', inverse=True, style={'margin-top':'10px', 'padding-left': '20px'})),
                dbc.Col(dbc.Card(card_content, color='warning', inverse=True, style={'margin-top':'10px'})),
                dbc.Col(dbc.Card(card_content, color='warning', inverse=True, style={'margin-top':'10px'}))
            ])
        ])
    ]),
])

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)