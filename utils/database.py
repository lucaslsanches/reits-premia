from pandas.tseries.holiday import USFederalHolidayCalendar
from utils.dicts import REITS, ETFS, START_DATES
from datetime import datetime
import pandas as pd
import numpy as np

data = pd.read_excel('data/data.xlsx', sheet_name='total_return', index_col=0)
BDAYS = pd.bdate_range(start=data.index[0], end=data.index[-1],
                       freq=pd.tseries.offsets.CustomBusinessDay(calendar=USFederalHolidayCalendar()))
data.index = pd.to_datetime(data.index)
data = data.loc[BDAYS]
monthly_data = np.log(data.resample('M').last()).diff().dropna()

# Fama-French portfolios
ff_factors = (pd.read_excel('data/data.xlsx', sheet_name='fama_french_mom', index_col=0)/100)

# Brazil Fama-French portfolios
bz_factors = (pd.read_excel('data/data.xlsx', sheet_name='nefin_ff_mom', index_col=0))
monthly_bz_factors = np.log(1+bz_factors).resample('M').sum()

# Additional data for miscellaneous experiments with international real estate ETFs
data_rates = pd.read_excel('data/data.xlsx', sheet_name='rates', index_col=0)
data_rates.index = pd.to_datetime(data_rates.index)
data_rates = data_rates.loc[BDAYS].dropna(how='all').fillna(method='ffill')
monthly_data_rates = np.log(1+data_rates[['US0003M Index','JY0003M Index','EUR003M Equity']].resample('M').last()/100)/12

# Extracting excess returns for REITs, with 3-month Libor
for reit in list(REITS.values()):
    monthly_data[reit] -= monthly_data_rates['US0003M Index']