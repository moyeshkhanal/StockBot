import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt


yf.pdr_override()
end = dt.datetime.now()
now = end - dt.timedelta(days=5)

print()
stock = "AAPL"

df = pdr.get_data_yahoo(stock, start=now, end=end, period="1d", interval="5m")

print(df)

df["High"].plot(label="high")

pivots = []
dates = []
counter = 0
lastPivot = 0

Range = [0 for i in range(10)]
dateRange = [0 for i in range(10)]

for i in df.index:
    currentMax = max(Range, default=0)
    value = round(df["High"][i],2)


    Range = Range[1:9]
    Range.append(value)

    dateRange = dateRange[1:9]
    dateRange.append(i)

    if currentMax == max(Range, default=0):
        counter += 1
    else:
        counter = 0
    if counter == 5:
        lastPivot = currentMax
        dateLocation = Range.index(lastPivot)
        lastDate = dateRange[dateLocation]

        pivots.append(lastPivot)
        dates.append(lastDate)


timeD = dt.timedelta(days=2)

for index in range(len(pivots)):
    print(str(pivots[index]) + ": " + str(dates[index]))

    plt.plot_date([dates[index], dates[index]+timeD],
                  [pivots[index], pivots[index]], linestyle="-", linewidth=2, marker=",")



plt.show()