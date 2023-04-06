# import nasdaqdatalink
# from config import QuandlConstants
import yfinance as yf
import pandas as pd
import datetime

import numpy as np
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

from moving_avg import getSimpleMovingAvgList
# import pandas_datareader as pdr
# import pandas_datareader.data as web
# import ffn
# import plotly.express as px


# -----------------------------------------------------------------------
#                           QUANDL 

# quandl_url = 'https://demo.quandl.com/docs-and-help'
# quandl.ApiConfig.api_key = '6-hx7s4DShK4AMpTd_PH'

# NASDAQ_DATA_LINK_API_KEY = QuandlConstants.NASDAQ_DATA_LINK_API_KEY
# NASDAQ_DATA_LINK_BASE_DOMAIN = ''

# data = nasdaqdatalink.get_table('ZACKS/FC', authtoken=NASDAQ_DATA_LINK_API_KEY, ticker='AAPL')
# print(data)

# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
#                           YFINANCE 

# data = yf.download('MSFT', period='1mo', interval='5m')

# import yfinance as yf

# apple= yf.Ticker("aapl")

# # show actions (dividends, splits)
# apple.actions

# # show dividends
# apple.dividends

# # show splits
# apple.splits

class StockConstants:
    favorites_list = ["AAPL", "MSFT", "TSLA", "DDOG", "AMD", "NVDA"]
    ETF_list = ["SPY", "VOO", "QQQ", "XLF"]
    financial_list = ["BX", "BLK", "BRK.B", "JPM"]

class TimeConstants: 
    default_period = ''
    default_interval = ''
    curr_end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    curr_period = '6mo'

class Stock: 
    def __init__(self, stock_name) -> None:
        self.name = stock_name
        self.ticker = yf.Ticker(self.name)
        self.history_5y = self.ticker.history(period='5y')
        self.ticker_close = self.history_5y['Close']
        # CALL THE MULTIPLE FUNCTIONS AVAILABLE AND STORE THEM IN VARIABLES.
        self.actions = self.ticker.get_actions()
        self.institutional_holders = self.ticker.get_institutional_holders()
        # self.analysis = self.ticker.get_analysis()
        # self.balance = self.ticker.get_balance_sheet()
        # self.calendar = self.ticker.get_calendar()
        # self.cf = self.ticker.get_cashflow()
        # self.info = self.ticker.get_info()
        # self.news = self.ticker.get_news()
        # self.recommendations = self.ticker.get_recommendations()
        # self.sustainability = self.ticker.get_sustainability()
    
    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return f"Welcome to Information about {self.name}"
    
    def analyze_dividends(self):
        return self.ticker.dividends()

    def options_data(self): 
        tick_options = self.ticker.option_chain()
        # ACCESS BOTH THE CALLS AND PUTS AND STORE THEM IN THEIR RESPECTIVE VARIABLES
        tick_puts = tick_options.puts
        tick_calls = tick_options.calls
 
    def plot_volume_stock(self): 
        self.ticker.history(period='5y')['Volume'].plot(label='{self.name} Volume', figsize=(15,5))

    def save_to_csv(self):
        tickers_hist = self.ticker.history(period='max',interval='1m',)
        tickers_hist.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index(level=1)
        tickers_hist.to_csv(f'{self.name}_all_data.csv')


def plotMultiStock(stocks_arr): 
    for stock in stocks_arr: 
        stock.ticker.plot(label='{stock.name} Close', figsize=(15,5))
    plt.legend()

def printBlank():
    print('*'*20)

# def test():
#     tdg = yf.Ticker('tdg')
#     print(tdg)
#     data = tdg.history()
#     print(data.head())


def stockInfo(stock_ticker):
    stock = Stock(stock_ticker)
    print(stock)
    stock.plot_volume_stock()
    # print_blank()
    # print(stock.institutional_holders)

def getCrossMovingAvgList(stock_lst):
    getSimpleMovingAvgList(stock_lst)

def main(): 
    stockInfo("MSFT")

    stock_lst = []
    for tick in StockConstants.favorites_list:
        stock = Stock(tick)
        stock_lst.append(stock)

    print(stock_lst)        
    getCrossMovingAvgList(stock_lst)


    # for tick in StockConstants.favorites_list:
    #     tick = Stock(tick)
    #     print(tick)

main()