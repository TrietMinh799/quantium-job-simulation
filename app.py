from dash import Dash, html, dcc
import plotly.express as px
from process import data

app = Dash()

data.drop(columns=["region"], inplace=True)

fig = px.line(data, x="date", y="sales", title="Pink Morsel Sales over Time")

app.layout = html.Div(
    children=[
        html.H1(children="Pink Morsel Sales", style={"textAlign": "center"}),
        dcc.Graph(id="graph", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
