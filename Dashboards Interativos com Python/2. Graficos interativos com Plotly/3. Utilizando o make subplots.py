import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Bar(y=[1,2,3],x=[4,5,6], marker_color='green'), row=1, col=1)
fig.add_trace(go.Scatter(y=[1,2,3],x=[4,5,6], marker_color='red'), row=1, col=2) #se col=1 ele une os dois gráficos

fig.update_layout(title_text='Usando update_layout()', title_font_size=40)

fig.show()

======================== Outro gráfico - Desabilitar o de cima =============================================

fig2 = go.Figure(
    data=[
        go.Bar(x=[1,2,3], y=[8,4,1]),
        go.Scatter(y=[5,9,2])
    ]
)

fig2.update_layout(height= 500, width=1000)
fig2.data[0].marker.line.width = 1
fig2.data[0].marker.line.color = 'black'
fig2.data[1].marker.line.width = 2

fig2.show()
