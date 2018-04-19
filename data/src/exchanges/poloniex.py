import ccxt
import json
import time
import os
from pprint import pprint

def write_json(order_book, trades, symbol):

    file_name_old = time.strftime('%Y%m%d-%H%M%S')
    folder_name_old = time.strftime('%Y%m%d')
    symbol_name = symbol.replace('/', '-')
    folder_name = '../order_book/poloniex/' + symbol_name + '/' + folder_name_old
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = folder_name + '/' + file_name_old + '.json'
    
    with open(file_name, 'w') as outfile:
        json.dump(order_book, outfile)
    
    trade_folder = '../trades/poloniex/'+ symbol_name + '/' + folder_name_old
    
    if not os.path.exists(trade_folder):
        os.makedirs(trade_folder)
    
    trade_file = trade_folder + '/' + file_name_old + '.json'
    
    with open(trade_file, 'w') as tradefile:
        json.dump(trades, tradefile)    


def load(symbol, interval, limit):
 
    poloniex_exchange = ccxt.poloniex()

    timestamp = [0] * len(symbol)

    poloniex_exchange_markets = poloniex_exchange.load_markets()

    print('-> ' + poloniex_exchange.id + ' market load: OK!\n')

    # Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
    # Parametros (par, intervalo_de_tempo, limite)
    for i in range(0, len(symbol)):
        poloniex_trade = poloniex_exchange.fetch_trades(symbol[i], None, limit)
        timestamp[i] = poloniex_trade[0]['timestamp']

    print('-> ' + poloniex_exchange.id + ' Order Book:\n')
    
    while(True):
        
        # Retorna os X primeiros bidask em cada lado do livro de ofertas
        for symbols in symbol:
            i = 0
            poloniex_exchange_orders = poloniex_exchange.fetch_order_book(symbols, limit)
            poloniex_trade = poloniex_exchange.fetch_trades(symbols, timestamp[i])

            write_json(poloniex_exchange_orders, poloniex_trade, symbols)
            print(symbols, len(poloniex_trade))
            if len(poloniex_trade) > 0:
                timestamp[i] = poloniex_trade[(len(poloniex_trade)-1)]['timestamp']
            i += 1
            time.sleep(5)
        time.sleep(interval)