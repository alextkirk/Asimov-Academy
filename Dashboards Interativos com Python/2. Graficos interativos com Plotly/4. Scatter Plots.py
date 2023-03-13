import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='lines+markers'))

fig.show()

#=========================== Outro exemplo =====================================

n = 100
x = np.linspace(0,1,n)
rand_y0 = np.random.randn(n) + 5
rand_y1 = np.random.randn(n)
rand_y2 = np.random.randn(n) - 5

fig = go.Figure()

fig.add_traces(go.Scatter(x=x, y=rand_y0, mode='markers', name='Markers'))
fig.add_traces(go.Scatter(x=x, y=rand_y1, mode='lines+markers', name='Lines+Markers'))
fig.add_traces(go.Scatter(x=x, y=rand_y2, mode='lines', name='Line'))

fig.show()


#==================================== Outro exemplo ============================================

fig = go.Figure(
    data=go.Scatter(
        x=[1,2,3,4],
        y=[10,35,23,19],
        mode='markers',
        marker=dict(size=[40,30,20,10],
                    color= [4,2,1,3]),
        hovertemplate='RS %{y} - %{marker.size}'
    )
)

fig.show()
