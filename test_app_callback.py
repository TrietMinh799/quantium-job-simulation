from asyncio import graph

from dash import dash, dcc, html
from app import update_graph, app, data
import plotly.graph_objects as go


def test_header_layout():
    layout = app.layout
    children = layout.children
    assert isinstance(children[0], html.H1), "First child should be an H1 header"


def test_visualization():
    children = app.layout.children
    graph_present = any(isinstance(child, dcc.Graph) for child in children)
    assert graph_present, "Layout should contain a Graph component"


def test_region_picker():
    children = app.layout.children
    radio_present = any(isinstance(child, dcc.RadioItems) for child in children)
    assert radio_present, "Layout should contain a RadioItems component"
