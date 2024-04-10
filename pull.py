import json
import websocket
import pandas as pd

assets = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']

assets = [coin.lower() + "@kline_1m" for coin in assets]

assets = '/'.join(assets)

def on_message(ws, message):
    message = json.loads(message)
    df_ = manipulation(message)
    df_.to_csv('coinprices.csv', mode='a', header=False)
    df_file = pd.read_csv('coinprices.csv')
    trimmed_df = df_file.tail(1000)
    print(trimmed_df)   
    trimmed_df.to_csv('coinprices.csv', mode='w', index=False, header=False)

def manipulation(source):
    rel_data = source['data']['k']['c']
    sym = source['data']['s']
    evt_time = pd.to_datetime(source['data']['E'],  unit='ms')
    df = pd.DataFrame(data=[[rel_data, sym]], index=[evt_time])
    return df

socket = "wss://stream.binance.com:9443/stream?streams="+assets

ws = websocket.WebSocketApp(url=socket, on_message=on_message)

ws.run_forever()