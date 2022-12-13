import plotly.graph_objects as go
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 1])

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    name="spline",
    text=["tweak line smoothness<br>with 'smoothing' in line object"],
    hoverinfo='text+name',
    line_shape='spline',
    line=dict(width=4)
))

fig.update_traces(hoverinfo='text+name', mode='lines+markers')
fig.update_layout(
    legend=dict(
        y=0.5,
        traceorder='reversed',
        font_size=16,
    ),
    template="plotly_dark"
)
fig.update_traces(marker=dict(size=20))

fig.show()
