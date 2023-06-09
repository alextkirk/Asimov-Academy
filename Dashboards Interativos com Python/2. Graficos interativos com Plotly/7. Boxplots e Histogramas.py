import plotly.graph_objects as go
import numpy as np

# x = np.random.randn(500)

# # fig = go.Figure(data=[go.Histogram(x=x)])
# # fig.show()

# x1 = np.random.randn(500) + 1

# fig = go.Figure()
# fig.add_trace(go.Histogram(x=x))
# fig.add_trace(go.Histogram(x=x1))

# fig.update_layout(barmode='overlay')
# fig.update_traces(opacity=0.75)
# fig.show()


#-------------------//------------------------

np.random.seed(1)

y0 = np.random.randn(50) + 1
y1 = np.random.randn(50) - 1

fig = go.Figure()
fig.add_trace(go.Box(y=y0))
fig.add_trace(go.Box(y=y1))

fig.update_layout(height=600)

fig.show()