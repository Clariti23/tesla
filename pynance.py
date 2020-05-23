import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import quandl
quandl.ApiConfig.api_key = "KptHVXnYi7RdK5YUNGkx"

style.use('ggplot')

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2019, 12, 31)

# # symbol =
# # df = web.DataReader('TSLA', 'quandl', start, end,
# #                     api_key == 'KptHVXnYi7RdK5YUNGkx')
# df = quandl.get("BITFINEX/BTCUSD")
# print(df)
# df.to_csv('btc.csv')
df = pd.read_csv('datasets/btc.csv', parse_dates=True, index_col=0)
# print(df.head())
df.plot()
