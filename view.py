import plotly.express as px

# Create some data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create the scatter plot
fig = px.scatter(x=x, y=y)
fig.show()
