# app.py — Optimized Task 4 Dashboard: clean layout, region filter, key event marker

import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

# === 配色方案 ===
COLORS = {
    "primary": "#F9F6FE",     # 背景色
    "secondary": "#D598EB",   # 组件色
    "font": "#522A61"         # 字体色
}

# === 加载数据 ===
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["region"] = df["region"].str.lower()

# === 创建 Dash 应用 ===
app = Dash(__name__)
app.title = "Pink Morsel Sales Visualizer"

# === 图表生成函数 ===
def generate_figure(filtered_df):
    daily_sales = filtered_df.groupby("date")["sales"].sum().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily_sales["date"],
        y=daily_sales["sales"],
        mode="lines",
        name="Total Sales",
        line=dict(color="#5B2C6F"),
        hovertemplate="Date: %{x|%Y-%m-%d}<br>Sales: $%{y:,.2f}<extra></extra>"
    ))

    # 添加涨价标记线
    price_change = "2021-01-15"
    fig.add_shape(
        type="line",
        x0=price_change,
        x1=price_change,
        y0=0,
        y1=daily_sales["sales"].max(),
        line=dict(color="red", dash="dash")
    )
    fig.add_annotation(
        x=price_change,
        y=daily_sales["sales"].max(),
        text="Price Increase",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40
    )

    # 样式美化
    fig.update_layout(
        title="Pink Morsel Sales Over Time",
        xaxis_title="Date",
        yaxis_title="Total Sales ($)",
        plot_bgcolor=COLORS["primary"],
        paper_bgcolor=COLORS["primary"],
        font=dict(color=COLORS["font"]),
        margin=dict(t=50, l=40, r=40, b=40)
    )
    return fig

# === 页面组件 ===
header = html.H1("📈 Pink Morsel Visualizer", id="header", style={
    "backgroundColor": COLORS["secondary"],
    "color": COLORS["font"],
    "borderRadius": "12px",
    "padding": "12px",
    "textAlign": "left"
})

region_picker = dcc.RadioItems(
    options=[
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All", "value": "all"}
    ],
    value="all",
    id="region-picker",
    inline=True,
    style={"marginBottom": "20px"}
)

tip = html.Div("💡 Hover over the line to see daily sales. Red line shows price increase date.",
               style={"fontStyle": "italic", "color": "#555", "textAlign": "left"})

graph = dcc.Graph(id="sales-graph", figure=generate_figure(df))

# === 页面布局 ===
app.layout = html.Div([
    header,
    html.Label("Choose a region:", style={"fontWeight": "bold", "textAlign": "left"}),
    region_picker,
    graph,
    tip
], style={
    "backgroundColor": COLORS["primary"],
    "padding": "40px",
    "fontFamily": "Arial",
    "color": COLORS["font"]
})

# === 回调交互 ===
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_graph(region):
    filtered = df if region == "all" else df[df["region"] == region]
    return generate_figure(filtered)

# === 启动应用 ===
if __name__ == "__main__":
    app.run(debug=True)
