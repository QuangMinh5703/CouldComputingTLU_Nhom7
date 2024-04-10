import pandas as pd

df = pd.read_csv('coinprices.csv', header=None)

df.columns = ['ts', 'price', 'coin']

def getreturn(coin):
    coin_f = df[df.coin == coin]
    coin_f = coin_f.sort_values('ts')
    coin_f = coin_f.set_index('ts')
    return coin_f

print(getreturn('ETHUSDT'))