import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import data
import functions

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_external_path='/assets')

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}

app.layout = html.Div(className='main', style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Coronavirus (COVID-19) Dashboard',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

    html.Div(children='A simple web application for visualizing up-to-date COVID-19 data',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }),
    html.Div([
        html.Div([html.H4(children='Total Cases: ',
                          style={
                              'textAlign': 'center',
                          }
                          ),
                  html.P(data.dfTotalConfirmed[-1], style={
                      'textAlign': 'center',
                  })]),
        html.Div([html.H4(children='Total Deaths: ',
                          style={
                              'textAlign': 'center',
                          }
                          ),
                  html.P(data.dfTotalDeaths[-1], style={
                      'textAlign': 'center',
                  })]),
        html.Div([html.H4(children='Total Recovered: ',
                          style={
                              'textAlign': 'center',
                          }
                          ),
                  html.P(data.dfTotalRecovered[-1], style={
                      'textAlign': 'center',
                  })]),
    ], className='large'
    ),
    html.Div([html.Div([
        html.Div([html.P("Top 10 Countries with COVID-19 (Total)"),
                  functions.generate_table(data.dfConfirmedCountriesCurrent)
                  ], className='column'),
        html.Div([html.P("Top 10 Countries with COVID-19 (Single Day)"),
                  functions.generate_table(data.dfConfirmedCountriesDifference)
                  ], className='column'),
        html.Div([html.P("Top 10 Most Deaths from COVID-19 (Total)"),
                  functions.generate_table(data.dfDeathsCountriesCurrent)
                  ], className='column'),
        html.Div([html.P("Top 10 Most Deaths from COVID-19 (Single Day)"),
                  functions.generate_table(data.dfDeathsCountriesDifference)
                  ], className='column'),
        html.Div([html.P("Top 10 Highest Recoveries from COVID-19 (Total)"),
                  functions.generate_table(data.dfRecoveredCountriesCurrent)
                  ], className='column'),
        html.Div([html.P("Top 10 Highest Recoveries from COVID-19 (Single Day)"),
                  functions.generate_table(data.dfRecoveredCountriesDifference)
                  ], className='column'),
    ], className='table')
    ]),
    html.Div(
        dcc.Graph(figure=functions.drawTimeSeries(data.dfTotalConfirmed, data.dfTotalDeaths, data.dfTotalRecovered)),
        className="timeseries")
])

if __name__ == '__main__':
    app.run_server(debug=True)
