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

##################################################################################part 2

#changing the date to Jalali(Persian) calender system

k = 0
for i in daily_data['Date']:
    Year , Month , Day = i.split('-')
    jalili_date =  jdatetime.date.fromgregorian(day=int(Day),month=int(Month),year=int(Year))
    daily_data.iat[k , 0] = str(jalili_date)
    k+=1
k=0
for i in weekly_data['Date']:
    Year , Month , Day = i.split('-')
    jalili_date =  jdatetime.date.fromgregorian(day=int(Day),month=int(Month),year=int(Year))
    weekly_data.iat[k , 0] = jalili_date
    k+=1
k=0
for i in monthly_data['Date']:
    Year , Month , Day = i.split('-')
    jalili_date =  jdatetime.date.fromgregorian(day=int(Day),month=int(Month),year=int(Year))
    monthly_data.iat[k , 0] = jalili_date
    k+=1
daily_data.head()

### data visulization based on Jalali(persian) calender 
pda = daily_data.plot(x= 'Date' , y = 'High', grid = 1, figsize= [12,5])
plt.gcf().autofmt_xdate()
pwe = weekly_data.plot(x= 'Date' , y = 'High', grid = 1, figsize= [12,5], color = 'red')
plt.gcf().autofmt_xdate()
pmo = monthly_data.plot(x= 'Date' , y = 'High', grid = 1, figsize= [12,5], color = 'green')
plt.gcf().autofmt_xdate()

####################################################################### part 3


#opting proportional property
# x=  time
# y = (High + low )/2
####
#This function is a periodic function. So the best function for fitting can be a type of trigonometric function.
###

#daily_data.plot.scatter(x= 'Date' , y = 'High', figsize= [12,5], alpha = 0.8, s =4)

xdate= daily_data.index.values
high = np.array(daily_data['High'])
low = np.array(daily_data['Low'])
meanDay = high/2+low/2
ydata = meanDay
