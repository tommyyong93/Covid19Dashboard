import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import datetime
import data


def drawTimeSeries(dataframe,seconddf,thirddf):
    dataframe.index = pd.to_datetime(dataframe.index)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe,
                             mode='lines+markers',
                             name='Confirmed',
                             line=dict(color='#3372FF', width=2),
                             fill='tozeroy', ))
    fig.add_trace(go.Scatter(x=dataframe.index, y=seconddf,
                             mode='lines+markers',
                             name='Deaths',
                             line=dict(color='#654312', width=2),
                             fill='tozeroy', ))
    fig.add_trace(go.Scatter(x=dataframe.index, y=thirddf,
                             mode='lines+markers',
                             name='Recovered',
                             line=dict(color='#123456', width=2),
                             fill='tozeroy', ))
    fig.update_layout(
        hovermode='x',
        font=dict(
            family="Courier New, monospace",
            size=14,
            color='#000000',
        ),
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color='#000000'
            ),
            bgcolor='#FFFFFF',
            borderwidth=5
        ),
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        margin=dict(l=0,
                    r=0,
                    t=0,
                    b=0
                    ),
        height=300,
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#3A3A3A')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#3A3A3A')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='#3A3A3A')

    return fig


def generate_table(dataframe, max_rows=15):
    return html.Table([
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
