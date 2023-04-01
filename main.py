import nasdaqdatalink
from config import QuandlConstants
import yfinance as yf

quandl_url = 'https://demo.quandl.com/docs-and-help'
quandl.ApiConfig.api_key = '6-hx7s4DShK4AMpTd_PH'

NASDAQ_DATA_LINK_API_KEY = QuandlConstants.NASDAQ_DATA_LINK_API_KEY
# NASDAQ_DATA_LINK_BASE_DOMAIN = ''

# data = nasdaqdatalink.get_table('ZACKS/FC', authtoken=NASDAQ_DATA_LINK_API_KEY, ticker='AAPL')
# print(data)

data = yf.download('MSFT', period='1mo', interval='5m')

