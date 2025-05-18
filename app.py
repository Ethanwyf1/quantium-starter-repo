# app.py

import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html

# 加载清洗后的数据
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])

# 按日期汇总销量
daily_sales = df.groupby("date")["sales"].sum().reset_index()

# 创建 Dash 应用
app = Dash(__name__)

# 创建折线图
line_chart = go.Figure()

line_chart.add_trace(go.Scatter(
    x=daily_sales["date"],
    y=daily_sales["sales"],
    mode="lines+markers",
    name="Total Sales"
))

# 设置涨价日期
price_increase_date = "2021-01-15"

# 添加垂直线标记涨价
line_chart.add_shape(
    type="line",
    x0=price_increase_date,
    x1=price_increase_date,
    y0=0,
    y1=daily_sales["sales"].max(),
    line=dict(color="red", dash="dash"),
)

line_chart.add_trace(go.Scatter(
    x=daily_sales["date"],
    y=daily_sales["sales"],
    mode="lines",
    name="Total Sales",
    line=dict(color="blue")
))


# 设置图表标题和轴标签
line_chart.update_layout(
    title="Sales of Pink Morsels Over Time",
    xaxis_title="Date",
    yaxis_title="Total Sales",
)

# 定义 Dash 页面布局
app.layout = html.Div([
    html.H1("📈 Pink Morsel Sales Visualisation"),
    dcc.Graph(figure=line_chart)
])

# 启动服务器
if __name__ == "__main__":
    app.run(debug=True)

