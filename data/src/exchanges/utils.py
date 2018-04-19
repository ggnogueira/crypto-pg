import ccxt
from pprint import pprint

def commom_elements():
    binance_exchange = ccxt.binance()
    binance_exchange.load_markets()

    bittrex_exchange = ccxt.bittrex()
    bittrex_exchange.load_markets()

    bitfinex_exchange = ccxt.bitfinex()
    bitfinex_exchange.load_markets()

    poloniex_exchange = ccxt.poloniex()
    poloniex_exchange.load_markets()

    huobi_exchange = ccxt.huobipro()
    huobi_exchange.load_markets()

    list1 = binance_exchange.symbols
    list2 = bittrex_exchange.symbols
    list3 = bitfinex_exchange.symbols

    for i in range(0, len(list3)):
        if 'USD' in list3[i]:
            list3[i] = list3[i] + 'T'
    
    list4 = poloniex_exchange.symbols
    list5 = huobi_exchange.symbols

    '''
    commom1 = list(set(list1).intersection(list2))
    commom2 = list(set(commom1).intersection(list3))
    commom3 = list(set(commom2).intersection(list4))
    commom4 = list(set(commom3).intersection(list5))
    '''
    return [element for element in list1 if (element in list2) and (element in list3) and (element in list4) and (element in list5)]
