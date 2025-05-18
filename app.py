# app.py — Task 4: Improved UI with Region Filter using Dash Bootstrap Components

import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Load data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["region"] = df["region"].str.lower()

# Use Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Pink Morsel Sales Dashboard"

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("📈 Pink Morsel Sales by Region"), width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Choose a region:", className="fw-bold"),
            dcc.RadioItems(
                id='region-selector',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'margin-right': '15px'}
            )
        ])
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="sales-graph"), width=12)
    ]),

    dbc.Row([
        dbc.Col(html.Div(
            "💡 Tip: Hover over the line to see detailed daily sales. "
            "The red dashed line indicates when the price was increased.",
            className="fst-italic text-muted"
        ), width=12)
    ])
], fluid=True, style={"padding": "40px", "fontFamily": "Arial"})

# Callback to update the figure
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"] == selected_region]

    daily_sales = filtered_df.groupby("date")["sales"].sum().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily_sales["date"],
        y=daily_sales["sales"],
        mode="lines",
        name="Total Sales",
        line=dict(color="royalblue"),
        hovertemplate="Date: %{x|%Y-%m-%d}<br>Sales: $%{y:.2f}<extra></extra>"
    ))

    price_increase_date = "2021-01-15"
    fig.add_shape(
        type="line",
        x0=price_increase_date,
        x1=price_increase_date,
        y0=0,
        y1=daily_sales["sales"].max(),
        line=dict(color="red", dash="dash")
    )
    fig.add_annotation(
        x=price_increase_date,
        y=daily_sales["sales"].max(),
        text="Price Increase",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40
    )

    fig.update_layout(
        title=f"Sales Trend - Region: {selected_region.title()}",
        xaxis_title="Date",
        yaxis_title="Total Sales ($)",
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f9f9f9",
        font=dict(color="#2c3e50")
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
