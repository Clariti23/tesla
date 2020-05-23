import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2019, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head)