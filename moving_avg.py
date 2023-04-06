import math
import time
import datetime
import pandas_ta as ta
import yfinance as yf


asset_list = [
    {'ticker':'SPY', 'yfticker':yf.Ticker('SPY'),'holding':False},
    {'ticker':'AMZN', 'yfticker':yf.Ticker('AMZN'),'holding':False},
    {'ticker':'GOOG', 'yfticker':yf.Ticker('GOOG'),'holding':False},
    {'ticker':'MSFT', 'yfticker':yf.Ticker('MSFT'),'holding':False},
    {'ticker':'TSLA', 'yfticker':yf.Ticker('TSLA'),'holding':False},
    {'ticker':'BTC-USD', 'yfticker':yf.Ticker('BTC-USD'),'holding':False},
    {'ticker':'ETH-USD', 'yfticker':yf.Ticker('ETH-USD'),'holding':False},
]

def getPause():
    now = datetime.datetime.now()
    next_min = now.replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)
    pause = math.ceil((next_min - now).seconds)
    print(f"Sleep for {pause}")
    return pause


def getMovingAvgList(stock_lst):
    interval_fast = 10
    interval_slow = 30
    # currently_holding = False
    # tradelog = []
    # while True:
    for i in range(2):
        for asset in stock_lst:
            start_date = (datetime.datetime.now()-datetime.timedelta(days=2)).strftime('%Y-%m-%d')
            df = asset.ticker.history(start=start_date, interval='1m')

            del df['Dividends']
            del df['Stock Splits']
            del df['Volume']

            df['SMA_fast'] = ta.sma(df['Close'], interval_fast)
            df['SMA_slow'] = ta.sma(df['Close'], interval_slow)

            price = df.iloc[-1]['Close']
            if df.iloc[-1]['SMA_fast'] > df.iloc[-1]['SMA_slow']: # and not currently_holding:
                print(f"Buy {asset.name}@{price}")
                # tradelog.append({'date': datetime.now(), 'ticker': asset.name, 'side': 'buy', 'price': price})
                # currently_holding = True

            elif df.iloc[-1]['SMA_fast'] < df.iloc[-1]['SMA_slow']: # and currently_holding:
                print(f"Sell {asset.name}@{price}")
                # tradelog.append({'date': datetime.now(), 'ticker': asset.name, 'side': 'sell', 'price': price})
                # currently_holding = False

        time.sleep(getPause())

