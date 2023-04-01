# import nasdaqdatalink
# from config import QuandlConstants
import yfinance as yf
import pandas as pd
import datetime


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

tdg = yf.Ticker('tdg')
print(tdg)
data = tdg.history()
print(data.head())


class Stock: 
    def __init__(self, stock_name) -> None:
        self.name = stock_name
        self.ticker = yf.Ticker(self.name)
        # CALL THE MULTIPLE FUNCTIONS AVAILABLE AND STORE THEM IN VARIABLES.
        self.actions = self.ticker.get_actions()
        # self.analysis = self.ticker.get_analysis()
        # self.balance = self.ticker.get_balance_sheet()
        # self.calendar = self.ticker.get_calendar()
        # self.cf = self.ticker.get_cashflow()
        # self.info = self.ticker.get_info()
        # self.inst_holders = self.ticker.get_institutional_holders()
        # self.news = self.ticker.get_news()
        # self.recommendations = self.ticker.get_recommendations()
        # self.sustainability = self.ticker.get_sustainability()

    def __str__(self) -> str:
        return f"Welcome to Information about {self.name}"


def options_data(ticker): 
    tick_options = ticker.option_chain()

    # ACCESS BOTH THE CALLS AND PUTS AND STORE THEM IN THEIR RESPECTIVE VARIABLES
    tick_puts = tick_options.puts
    tick_calls = tick_options.calls


msft = Stock("MSFT")
print(msft)