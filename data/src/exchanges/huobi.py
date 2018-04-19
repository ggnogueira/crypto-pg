import ccxt
import json
import time
import os
from pprint import pprint

def write_json(order_book, trades, symbol):

    file_name_old = time.strftime('%Y%m%d-%H%M%S')
    folder_name_old = time.strftime('%Y%m%d')
    symbol_name = symbol.replace('/', '-')
    folder_name = '../order_book/huobi/' + symbol_name + '/' + folder_name_old
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = folder_name + '/' + file_name_old + '.json'
    
    with open(file_name, 'w') as outfile:
        json.dump(order_book, outfile)
    
    trade_folder = '../trades/huobi/'+ symbol_name + '/' + folder_name_old
    
    if not os.path.exists(trade_folder):
        os.makedirs(trade_folder)
    
    trade_file = trade_folder + '/' + file_name_old + '.json'
    
    with open(trade_file, 'w') as tradefile:
        json.dump(trades, tradefile)    


def load(symbol, interval, limit):
 
    huobi_exchange = ccxt.huobipro()

    timestamp = [0] * len(symbol)

    huobi_exchange_markets = huobi_exchange.load_markets()

    print('-> ' + huobi_exchange.id + ' market load: OK!\n')

    # Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
    # Parametros (par, intervalo_de_tempo, limite)
    for i in range(0, len(symbol)):
        huobi_trade = huobi_exchange.fetch_trades(symbol[i], None, limit)
        timestamp[i] = huobi_trade[0]['timestamp']

    print('-> ' + huobi_exchange.id + ' Order Book:\n')
    
    while(True):
        
        # Retorna os X primeiros bidask em cada lado do livro de ofertas
        for symbols in symbol:
            i = 0
            huobi_exchange_orders = huobi_exchange.fetch_order_book(symbols, limit)
            huobi_trade = huobi_exchange.fetch_trades(symbols, timestamp[i])

            write_json(huobi_exchange_orders, huobi_trade, symbols)
            print(symbols, len(huobi_trade))
            if len(huobi_trade) > 0:
                timestamp[i] = huobi_trade[(len(huobi_trade)-1)]['timestamp']
            i += 1
            time.sleep(5)
        time.sleep(interval)