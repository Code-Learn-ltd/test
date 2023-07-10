import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import jdatetime
import matplotlib.dates as mdate
import datetime as dt
from scipy.optimize import curve_fit

#read dara from a link
daily_url ="https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1657064859&period2=1688608059&interval=1d&events=history&includeAdjustedClose=true"
weekly_url = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1656933255&period2=1688476455&interval=1wk&events=history&includeAdjustedClose=true"
monthly_url = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1656933255&period2=1688476455&interval=1mo&events=history&includeAdjustedClose=true"
daily_data = pd.read_csv(daily_url, parse_dates=True)
weekly_data = pd.read_csv(weekly_url, parse_dates=True)
monthly_data = pd.read_csv(monthly_url, parse_dates=True)

#plot data
stokDataDay = pd.read_csv(daily_url, index_col= 'Date')

plt.figure(figsize=(10, 5))
plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdate.DayLocator(interval = 30))
x_date = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in stokDataDay.index.values ]

plt.plot(x_date, stokDataDay['High'], label = 'High')
plt.plot(x_date, stokDataDay['Low'], label = 'Low')
plt.legend()
plt.gcf().autofmt_xdate()

plt.show()
