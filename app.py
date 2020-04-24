import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import data
import functions



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_external_path='/assets')

app.layout = html.Div(className='main', children=[
    html.H1(className='heading', children='Coronavirus (COVID-19) Dashboard'),
    html.Div(className='headingSubtext', children='A simple web application for visualizing up-to-date COVID-19 data'),
    html.Br(),
    html.Div([
        html.Div([html.H4(children='Total Cases: '),
                  html.P(data.dfTotalConfirmed[-1])], className='headerTitle confirmed'),
        html.Div([html.H4(children='Total Deaths: '),
                  html.P(data.dfTotalDeaths[-1])], className='headerTitle death'),
        html.Div([html.H4(children='Total Recovered: '),
                  html.P(data.dfTotalRecovered[-1])], className='headerTitle recovered'),
    ], className='topBanner'
    ),
    html.Div([html.Div([
        html.Div([html.P(className='titleTable confirmed', children="Top 10 Countries with COVID-19 (Total)"),
                  functions.generateTable(data.dfConfirmedCountriesCurrent)
                  ], className='column'),
        html.Div([html.P(className='titleTable confirmed', children="Top 10 Countries with COVID-19 (24 hr)"),
                  functions.generateTable(data.dfConfirmedCountriesDifference)
                  ], className='column'),
        html.Div([html.P(className='titleTable death', children="Top 10 Most Deaths from COVID-19 (Total)"),
                  functions.generateTable(data.dfDeathsCountriesCurrent)
                  ], className='column'),
        html.Div([html.P(className='titleTable death', children="Top 10 Most Deaths from COVID-19 (24 hr)"),
                  functions.generateTable(data.dfDeathsCountriesDifference)
                  ], className='column'),
        html.Div([html.P(className='titleTable recovered', children="Top 10 Highest Recoveries from COVID-19 (Total)"),
                  functions.generateTable(data.dfRecoveredCountriesCurrent)
                  ], className='column'),
        html.Div([html.P(className='titleTable recovered', children="Top 10 Highest Recoveries from COVID-19 (24 hr)"),
                  functions.generateTable(data.dfRecoveredCountriesDifference)
                  ], className='column'),
    ], className='table')
    ]),
    html.Div([dcc.Graph(figure=functions.drawMap(data.location))],className='map'),
    html.Br(),
    html.Div([
        html.Div(
            dcc.Graph(
                figure=functions.drawTimeSeries(data.dfTotalConfirmed, data.dfTotalDeaths, data.dfTotalRecovered)),
            className="timeseries"),
        html.Div(
            dcc.Graph(figure=functions.drawCountryTimeSeries(data.dfConfirmedCountriesSortedTop10TimeSeriesSum)),
            className="timeseries", )
    ], className='timeseriesContainer'),
    html.Div([dt.DataTable(id='largeTable',
                           columns=[
                               {"name": i, "id": i, "deletable": False, "selectable": True} for i in
                               ['Province/State', 'Country/Region', 'Confirmed',
                                'Deaths', 'Recovered']
                           ],
                           data=data.location.to_dict('records'), fixed_rows={'headers': True, 'data': 0},
                           editable=False,
                           sort_action="native",
                           sort_mode="single",
                           row_selectable="single",
                           row_deletable=False,
                           selected_columns=[],
                           selected_rows=[],
                           page_size=500,
                           page_current=0, )], className='largeTableContainer'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
