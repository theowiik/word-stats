import plotly.graph_objects as go

color = '#A20000'
secondary_color = '#00FFA1'

custom_template = dict(
    layout=go.Layout(
        titlefont=dict(size=30),
        font=dict(family="Martian Mono", size=15, color="#ffffff"),
        colorway=[color],
    )
)


def create_bar_plot(labels, values):
    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation='h'
    ))

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        title='Most used words',
        template=custom_template,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig


def create_line_plot(labels, values):
    fig = go.Figure(go.Scatter(
        x=labels,
        y=values,
        mode='lines+markers',
        line=dict(width=4)
    ))

    fig.update_layout(
        title='Most used words over time',
        template=custom_template,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig
