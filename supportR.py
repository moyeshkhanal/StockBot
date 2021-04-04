import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt



class Database():
    def __init__(self, ticker, days):
        yf.pdr_override()
        end = dt.datetime.now()
        now = end - dt.timedelta(days=days)
        self.ticker = ticker
        self.df = pdr.get_data_yahoo(self.ticker, start=now, end=end, period="1d", interval="5m")
        # No Weekend
        self.df = self.df[self.df.index.dayofweek < 5]
        # limit the data to days
        # self.df =self.df[-days:]

    def quote(self):
        return self.df


db = Database("TSLA", 4)
df = db.quote()
open = []

open.append(df["Open"][1])

print(f"First Item: {df.index[0]}, Last Item: {df.index[-1]}, Open: {open}, Close: {df['Close'][1]}")
