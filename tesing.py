from binance import Client
import config as cn

client = Client(cn.API_KEY,cn.API_SEC,tld='com')

tiker = client.get_all_tickers()
print(tiker)