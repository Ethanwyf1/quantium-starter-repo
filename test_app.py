
from app import app

def test_layout_has_header():
    layout = app.layout
    header = next((c for c in layout.children if getattr(c, 'id', None) == 'header'), None)
    assert header is not None
    assert "Pink Morsel Visualizer" in header.children

def test_layout_has_graph():
    layout = app.layout
    graph = next((c for c in layout.children if getattr(c, 'id', None) == 'sales-graph'), None)
    assert graph is not None

def test_layout_has_radio():
    layout = app.layout
    radio = next((c for c in layout.children if getattr(c, 'id', None) == 'region-picker'), None)
    assert radio is not None
