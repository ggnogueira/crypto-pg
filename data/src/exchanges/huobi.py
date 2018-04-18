import ccxt
import json
import time
import os
from pprint import pprint

def write_json(order_book, trades):

    file_name_old = time.strftime('%Y%m%d-%H%M%S')
    folder_name_old = time.strftime('%Y%m%d')
    folder_name = '../order_book/' + folder_name_old
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = folder_name + '/' + file_name_old + '.json'
    
    with open(file_name, 'w') as outfile:
        json.dump(order_book, outfile)
    
    trade_folder = '../trades/' + folder_name_old
    
    if not os.path.exists(trade_folder):
        os.makedirs(trade_folder)
    
    trade_file = trade_folder + '/' + file_name_old + '.json'
    
    with open(trade_file, 'w') as tradefile:
        json.dump(trades, tradefile)    


def load(symbol, interval, limit):
    huobi_exchange = ccxt.huobipro()

    huobi_exchange_markets = huobi_exchange.load_markets()

    print('-> ' + huobi_exchange.id + ' market load: OK!\n')

    # Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
    # Parametros (par, intervalo_de_tempo, limite)
    huobi_trade = huobi_exchange.fetch_trades(symbol, None, limit)
    timestamp = huobi_trade[0]['timestamp']

    print('-> ' + huobi_exchange.id + ' Order Book of ' + symbol + ':\n')
    
    while(True):
        
        # Retorna os X primeiros bidask em cada lado do livro de ofertas
        huobi_exchange_orders = huobi_exchange.fetch_order_book(symbol, limit)
        huobi_trade = huobi_exchange.fetch_trades(symbol, timestamp)

        write_json(huobi_exchange_orders, huobi_trade)

        timestamp = huobi_trade[(len(huobi_trade)-1)]['timestamp']

        time.sleep(19)