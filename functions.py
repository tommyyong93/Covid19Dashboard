import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import datetime
import data


def drawGlobalTimeSeriesCumulative(dataframe, seconddf, thirddf):
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
                             line=dict(color='#FF6347', width=2),
                             fill='tozeroy', ))
    fig.add_trace(go.Scatter(x=dataframe.index, y=thirddf,
                             mode='lines+markers',
                             name='Recovered',
                             line=dict(color='#228B22', width=2),
                             fill='tozeroy', ))
    fig.update_layout(
        hovermode='x',
        font=dict(
            family="Courier New, monospace",
            size=14,
            color='#FFFFFF',
        ),
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            font=dict(
                family="monospace",
                size=12,
                color='#000000'
            ),
            bgcolor='#ccc9dc',
            borderwidth=1
        ),
        paper_bgcolor='#3a506b',
        plot_bgcolor='#3a506b',
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


def drawGlobalTimeSeriesDaily(dataframe, seconddf, thirddf):
    dataframe.index = pd.to_datetime(dataframe.index)

    dataframe = (dataframe - dataframe.shift(1)).drop(dataframe.index[0])
    seconddf = (seconddf - seconddf.shift(1)).drop(seconddf.index[0])
    thirddf = (thirddf - thirddf.shift(1)).drop(thirddf.index[0])

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe,
                             mode='lines+markers',
                             name='Confirmed',
                             line=dict(color='#3372FF', width=2),
                             fill='tozeroy', ))
    fig.add_trace(go.Scatter(x=dataframe.index, y=seconddf,
                             mode='lines+markers',
                             name='Deaths',
                             line=dict(color='#FF6347', width=2),
                             fill='tozeroy', ))
    fig.add_trace(go.Scatter(x=dataframe.index, y=thirddf,
                             mode='lines+markers',
                             name='Recovered',
                             line=dict(color='#228B22', width=2),
                             fill='tozeroy', ))
    fig.update_layout(
        hovermode='x',
        font=dict(
            family="Courier New, monospace",
            size=14,
            color='#FFFFFF',
        ),
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            font=dict(
                family="monospace",
                size=12,
                color='#000000'
            ),
            bgcolor='#ccc9dc',
            borderwidth=1
        ),
        paper_bgcolor='#3a506b',
        plot_bgcolor='#3a506b',
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


def drawSingleCountryTimeSeries(confirmed, deaths, recovered, country):
    fig = go.Figure()

    colors = ['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#ffcdb2', '#ffb4a2', '#e5989b', '#6d6875',
              '#0000FF']

    fig.add_trace(go.Scatter(x=pd.to_datetime(confirmed.iloc[country, 4:].index), y=confirmed.iloc[country, 4:],
                             mode='lines+markers',
                             name="Confirmed",
                             line=dict(color=colors[1], width=2),
                             fill='none', ))
    fig.add_trace(go.Scatter(x=pd.to_datetime(deaths.iloc[country, 4:].index), y=deaths.iloc[country, 4:],
                             mode='lines+markers',
                             name="Deaths",
                             line=dict(color=colors[2], width=2),
                             fill='none', ))
    fig.add_trace(go.Scatter(x=pd.to_datetime(recovered.iloc[country, 4:].index), y=recovered.iloc[country, 4:],
                             mode='lines+markers',
                             name="Recovered",
                             line=dict(color=colors[3], width=2),
                             fill='none', ))

    fig.update_layout(
        hovermode='x',
        font=dict(
            family="Courier New, monospace",
            size=14,
            color='#FFFFFF',
        ),
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            font=dict(
                family="monospace",
                size=12,
                color='#000000'
            ),
            bgcolor='#ccc9dc',
            borderwidth=1
        ),
        paper_bgcolor='#3a506b',
        plot_bgcolor='#3a506b',
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


def drawTenCountryTimeSeries(dataframe):
    fig = go.Figure()

    colors = ['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#ffcdb2', '#ffb4a2', '#e5989b', '#6d6875',
              '#0000FF']

    for i in range(0, 10):
        fig.add_trace(go.Scatter(x=pd.to_datetime(dataframe.iloc[i, :-1].index), y=dataframe.iloc[i, :-1],
                                 mode='lines+markers',
                                 name=dataframe.iloc[i, -1],
                                 line=dict(color=colors[i], width=2),
                                 fill='none', ))

    fig.update_layout(
        hovermode='x',
        font=dict(
            family="Courier New, monospace",
            size=14,
            color='#FFFFFF',
        ),
        legend=dict(
            x=0.02,
            y=1,
            traceorder="normal",
            font=dict(
                family="monospace",
                size=12,
                color='#000000'
            ),
            bgcolor='#ccc9dc',
            borderwidth=1
        ),
        paper_bgcolor='#3a506b',
        plot_bgcolor='#3a506b',
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


def generateTable(dataframe, max_rows=10):
    return html.Table([
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ], className='topTable')


def drawMap(mapdata):
    fig = px.scatter_mapbox(mapdata, lat=mapdata["Lat"], lon=mapdata["Long"], hover_name=mapdata["Country/Region"],
                            size=np.log(mapdata['Confirmed'] + 1), opacity=0.7, size_max=20,
                            color_discrete_sequence=['#ccc9dc'], zoom=1, width=1000,
                            center=dict(lat=37.0902, lon=-95.7129),
                            hover_data=[mapdata['Confirmed'], mapdata['Deaths'], mapdata['Recovered']],
                            )
    fig.update_layout(mapbox_style="dark",
                      mapbox_accesstoken="pk.eyJ1IjoidG9tbXl5b25nIiwiYSI6ImNrOWU5czh3ajAwMWkzbHBjbjBmN2Z5ZzAifQ.iO1gg5UlrfEf8UhpZcOWtQ",
                      )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, autosize=True)
    return fig