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

def plot_bar(labels, values):
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

    fig.show()

# # ------------------------------

# pie_labels = ['Swear', 'Other']
# pie_values = [2, 8]

# pie = go.Figure(go.Pie(
#     labels=pie_labels,
#     values=pie_values,
#     # hole=.2,
#     marker_colors=[color, '#494949'],
#     textinfo='label+percent',
# ))

# pie.update_layout(
#     title='Percentage curse words',
#     template=custom_template,
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     font=dict(size=40),
#     textinfo='none'
# )

# # hide labels
# pie.update_traces(textposition='inside', textinfo='none')

# # pie.show()

