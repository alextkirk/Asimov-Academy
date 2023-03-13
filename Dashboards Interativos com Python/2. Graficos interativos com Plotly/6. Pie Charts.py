import plotly.graph_objects as go

labels = ['Oxigênio', 'Gás Carbônico', 'Hidrogênio', 'Nitrogênio']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=go.Pie(labels=labels, values=values, pull=[0,0,0.5,0]))

fig.update_traces(hoverinfo='value+percent', textinfo='label+percent')

fig.show()