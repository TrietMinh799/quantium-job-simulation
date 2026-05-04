from dash import Dash, Input, Output, callback, html, dcc
import plotly.express as px
from process import data

app = Dash()

fig = px.bar(data, x="date", y="sales", title="Pink Morsel Sales over Time")
list_options = [
    {"label": region, "value": region} for region in data["region"].unique()
]
list_options.append({"label": "All Regions", "value": "all"})

app.layout = html.Div(
    children=[
        html.H1(
            children="Pink Morsel Sales",
            style={"textAlign": "center"},
        ),
        dcc.Graph(id="graph", figure=fig),
        dcc.RadioItems(
            id="region-dropdown",
            options=list_options,
            value=data["region"].unique()[0],
            style={
                "width": "50%",
                "border": "1px solid #ccc",
                "border-radius": "4px",
                "margin": "20px auto",
                "padding": "10px",
            },
        ),
    ]
)


@callback(Output("graph", "figure"), [Input("region-dropdown", "value")])
def update_graph(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]
    fig = px.bar(
        filtered_data,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales in {selected_region}",
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
