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
    binance_exchange = ccxt.binance()

    binance_exchange_markets = binance_exchange.load_markets()

    print('-> ' + binance_exchange.id + ' market load: OK!\n')

    # Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
    # Parametros (par, intervalo_de_tempo, limite)
    binance_trade = binance_exchange.fetch_trades(symbol, None, limit)
    timestamp = binance_trade[0]['timestamp']

    print('-> ' + binance_exchange.id + ' Order Book of ' + symbol + ':\n')

    while(True):
        
        # Retorna os X primeiros bidask em cada lado do livro de ofertas
        binance_exchange_orders = binance_exchange.fetch_order_book(symbol, limit)
        binance_trade = binance_exchange.fetch_trades(symbol, timestamp)

        write_json(binance_exchange_orders, binance_trade)

        timestamp = binance_trade[(len(binance_trade)-1)]['timestamp']

        time.sleep(19)