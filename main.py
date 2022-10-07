import pandas as pd
import plotly.graph_objects as go
import datetime
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
dogecoin_data = cg.get_coin_market_chart_by_id(id='dogecoin', vs_currency='gbp', days=30)
dogecoin_price_data = dogecoin_data['prices']
data = pd.DataFrame(dogecoin_price_data, columns=['TimeStamp', 'Price'])

#TRANSLATES TIMESTAMP TO DATETIME
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

print(data)