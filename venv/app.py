import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
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
    html.H4(children='COVID 19 - Deaths'),
    generate_table(data.dfDeaths),
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
                  })])
    ], className='row'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
