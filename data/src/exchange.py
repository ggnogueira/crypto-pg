import exchanges.binance as binance_exchange
import exchanges.bittrex as bittrex_exchange
import exchanges.poloniex as poloniex_exchange
import exchanges.huobi as huobi_exchange
import exchanges.bitfinex as bitfinex_exchange


def binance(symbol, interval, limit):
    binance_exchange.load(symbol, interval, limit)

def bittrex(symbol, interval, limit):
    bittrex_exchange.load(symbol, interval, limit)

def bitfinex(symbol, interval, limit):
    bitfinex_exchange.load(symbol, interval, limit)

def poloniex(symbol, interval, limit):
    poloniex_exchange.load(symbol, interval, limit)

def huobi(symbol, interval, limit):
    huobi_exchange.load(symbol, interval, limit)