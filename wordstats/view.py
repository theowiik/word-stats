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

sample_data = [('I', 22),
               ('a', 18),
               ('the', 16),
               ('you', 15),
               ("I'm", 12),
               ('me', 11),
               ('it', 11),
               ("don't", 9),
               ('in', 8),
               ("can't", 8)]

values = [x[1] for x in sample_data]
labels = [x[0] for x in sample_data]

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

# ------------------------------

pie_labels = ['Swear', 'Other']
pie_values = [2, 8]

pie = go.Figure(go.Pie(
    labels=pie_labels,
    values=pie_values,
    # hole=.2,
    marker_colors=[color, '#494949'],
    textinfo='label+percent',
))

pie.update_layout(
    title='Percentage curse words',
    template=custom_template,
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(size=40),
    textinfo='none'
)

# hide labels
pie.update_traces(textposition='inside', textinfo='none')

# pie.show()

