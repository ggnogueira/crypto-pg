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
    bitfinex_exchange = ccxt.bitfinex()

    bitfinex_exchange_markets = bitfinex_exchange.load_markets()

    print('-> ' + bitfinex_exchange.id + ' market load: OK!\n')

    # Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
    # Parametros (par, intervalo_de_tempo, limite)
    bitfinex_trade = bitfinex_exchange.fetch_trades(symbol, None, limit)
    timestamp = bitfinex_trade[0]['timestamp']

    print('-> ' + bitfinex_exchange.id + ' Order Book of ' + symbol + ':\n')
    
    while(True):
        
        # Retorna os X primeiros bidask em cada lado do livro de ofertas
        bitfinex_exchange_orders = bitfinex_exchange.fetch_order_book(symbol, limit)
        bitfinex_trade = bitfinex_exchange.fetch_trades(symbol, timestamp)

        write_json(bitfinex_exchange_orders, bitfinex_trade)

        timestamp = bitfinex_trade[(len(bitfinex_trade)-1)]['timestamp']

        time.sleep(19)