import pandas as pd

# Get CSSEGIS data from https://github.com/CSSEGISandData
dfRecovered = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
dfDeaths = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
dfConfirmed = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

dfTotalRecovered = dfRecovered.iloc[:, 4:].sum(axis=0, skipna=True)
dfTotalDeaths = dfDeaths.iloc[:, 4:].sum(axis=0, skipna=True)
dfTotalConfirmed = dfConfirmed.iloc[:, 4:].sum(axis=0, skipna=True)