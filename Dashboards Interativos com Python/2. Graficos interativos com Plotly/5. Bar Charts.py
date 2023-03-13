import plotly.graph_objects as go

animais = ['Macaco', 'Girafa', 'Efalante']

fig = go.Figure(
    data=[
        go.Bar(x=animais, y=[30,5,3], name='Zoo SP'),
        go.Bar(x=animais, y=[10,2,3], name='Zoo RS')
    ]
)

fig.show()