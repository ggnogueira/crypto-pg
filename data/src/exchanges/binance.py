import ccxt
import json
import time
import os
from pprint import pprint

def write_json(order_book, trades, symbol):

    file_name_old = time.strftime('%Y%m%d-%H%M%S')
    folder_name_old = time.strftime('%Y%m%d')
    symbol_name = symbol.replace('/', '-')
    folder_name = '../order_book/binance/' + symbol_name + '/' + folder_name_old
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = folder_name + '/' + file_name_old + '.json'
    
    with open(file_name, 'w') as outfile:
        json.dump(order_book, outfile)
    
    trade_folder = '../trades/binance/'+ symbol_name + '/' + folder_name_old
    
    if not os.path.exists(trade_folder):
        os.makedirs(trade_folder)
    
    trade_file = trade_folder + '/' + file_name_old + '.json'
    
    with open(trade_file, 'w') as tradefile:
        json.dump(trades, tradefile)    


def load(symbol, interval, limit):
 
    binance_exchange = ccxt.binance()

    timestamp = [0] * len(symbol)

    binance_exchange_markets = binance_exchange.load_markets()

    print('-> ' + binance_exchange.id + ' market load: OK!\n')

    # Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
    # Parametros (par, intervalo_de_tempo, limite)
    for i in range(0, len(symbol)):
        binance_trade = binance_exchange.fetch_trades(symbol[i], None, limit)
        timestamp[i] = binance_trade[0]['timestamp']

    print('-> ' + binance_exchange.id + ' Order Book:\n')
    
    while(True):
        
        # Retorna os X primeiros bidask em cada lado do livro de ofertas
        for symbols in symbol:
            i = 0
            binance_exchange_orders = binance_exchange.fetch_order_book(symbols, limit)
            binance_trade = binance_exchange.fetch_trades(symbols, timestamp[i])

            write_json(binance_exchange_orders, binance_trade, symbols)
            print(symbols, len(binance_trade))
            if len(binance_trade) > 0:
                timestamp[i] = binance_trade[(len(binance_trade)-1)]['timestamp']
            i += 1
            time.sleep(5)
        time.sleep(interval)