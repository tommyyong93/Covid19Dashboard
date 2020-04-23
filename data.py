import pandas as pd

# Get CSSEGIS data from https://github.com/CSSEGISandData
dfRecovered = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
dfDeaths = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
dfConfirmed = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

# Get cumulative sums
dfTotalRecovered = dfRecovered.iloc[:, 4:].sum(axis=0, skipna=True)
dfTotalDeaths = dfDeaths.iloc[:, 4:].sum(axis=0, skipna=True)
dfTotalConfirmed = dfConfirmed.iloc[:, 4:].sum(axis=0, skipna=True)

# Process data, first sort by number of deaths, add two new columns and calculate 24 hour difference
dfDeathsCountriesSorted = dfDeaths.copy().sort_values(by = dfDeaths.columns[-1], ascending=False)
dfDeathsCountriesSorted['Today'] = dfDeathsCountriesSorted.iloc[:,-1]
dfDeathsCountriesSorted['Difference'] = dfDeathsCountriesSorted.iloc[:,-1] - dfDeathsCountriesSorted.iloc[:,-3]
dfDeathsCountriesCurrent = dfDeathsCountriesSorted[['Country/Region',dfDeathsCountriesSorted.columns[-2]]][0:10]
dfDeathsCountriesDifference = dfDeathsCountriesSorted.sort_values(by = dfDeathsCountriesSorted.columns[-1], ascending=False)[['Country/Region',dfDeathsCountriesSorted.columns[-1]]][0:10]

# Process data, first sort by number of confirmed cases, add two new columns and calculate 24 hour difference
dfConfirmedCountriesSorted = dfConfirmed.copy().sort_values(by = dfConfirmed.columns[-1], ascending=False)
dfConfirmedCountriesSorted['Today'] = dfConfirmedCountriesSorted.iloc[:,-1]
dfConfirmedCountriesSorted['Difference'] = dfConfirmedCountriesSorted.iloc[:,-1] - dfConfirmedCountriesSorted.iloc[:,-3]
dfConfirmedCountriesCurrent = dfConfirmedCountriesSorted[['Country/Region',dfConfirmedCountriesSorted.columns[-2]]][0:10]
dfConfirmedCountriesDifference = dfConfirmedCountriesSorted.sort_values(by = dfConfirmedCountriesSorted.columns[-1], ascending=False)[['Country/Region',dfConfirmedCountriesSorted.columns[-1]]][0:10]

# Process data, first sort by number of recovered cases, add two new columns and calculate 24 hour difference
dfRecoveredCountriesSorted = dfRecovered.copy().sort_values(by = dfRecovered.columns[-1], ascending=False)
dfRecoveredCountriesSorted['Today'] = dfRecoveredCountriesSorted.iloc[:,-1]
dfRecoveredCountriesSorted['Difference'] = dfRecoveredCountriesSorted.iloc[:,-1] - dfRecoveredCountriesSorted.iloc[:,-3]
dfRecoveredCountriesCurrent = dfRecoveredCountriesSorted[['Country/Region',dfRecoveredCountriesSorted.columns[-2]]][0:10]
dfRecoveredCountriesDifference = dfRecoveredCountriesSorted.sort_values(by = dfRecoveredCountriesSorted.columns[-1], ascending=False)[['Country/Region',dfRecoveredCountriesSorted.columns[-1]]][0:10]

# Get data for maps for later
location = dfConfirmed.copy()[["Country/Region", "Lat", "Long"]]
location['Confirmed'] = dfConfirmed.iloc[:, -1]
location['Deaths'] = dfDeaths.iloc[:, -1]
location['Recovered'] = dfRecovered.iloc[:, -1]
location.fillna(0, inplace=True)

# Top 10 Country time series data
dfConfirmedCountriesSortedTop10TimeSeries = dfConfirmedCountriesSorted.iloc[0:10,1]
dfConfirmedCountriesSortedTop10TimeSeriesSum = dfConfirmedCountriesSorted.iloc[0:10,4:-2]

if __name__ == '__main__':
    print(dfConfirmedCountriesSortedTop10TimeSeries)
    print(dfConfirmedCountriesSortedTop10TimeSeriesSum)