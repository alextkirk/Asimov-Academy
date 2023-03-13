import dash
from dash import html, dcc, Input, Output, callback_context

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn_1_sample'),
    html.Button('Button 2', id='btn_2_sample'),
    html.Button('Button 3', id='btn_3_sample'),
    html.Div(id='container_ctx_example')
])

@app.callback(Output('container_ctx_example', 'children'),
    Input('btn_1_sample', 'n_clicks'),
    Input('btn_2_sample', 'n_clicks'),
    Input('btn_3_sample', 'n_clicks'))

def display(btn1, btn2, btn3):
    # import pdb
    # pdb.set_trace()
    id_triggered = callback_context.triggered[0]['prop_id'].split('.')[0]
    return id_triggered

if __name__ == '__main__':
    app.run_server(debug=True)