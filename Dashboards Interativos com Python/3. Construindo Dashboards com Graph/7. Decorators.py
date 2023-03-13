import dash
from dash import html, dcc 
from dash.dependencies import Input, Output, State

# Apresentando callback pela primeira vez

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6('Altere o valor abaixo para ver o callback..'),
    html.Div(["Entrada:",
        dcc.Input(id='Input_1', value='Digite alguma coisa', type='text')]),
    html.Br(),
    html.Div(id='Output_1'),
])

@app.callback(
    Output(component_id='Output_1', component_property='children'),
    [Input(component_id='Input_1', component_property='value')]
)

def update_output_div(value):
    return 'Saída: {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)