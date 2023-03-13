import plotly
import plotly.graph_objects as go

fig = go.Figure(
    data = [go.Bar(x = [1,2,3], y= [3,2,1])],
    layout = go.Layout(
        title = go.layout.Title(text='Gráfico')
    )
)

fig.show()