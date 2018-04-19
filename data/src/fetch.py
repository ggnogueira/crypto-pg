import argparse
import exchange

parser = argparse.ArgumentParser(description='Collect some data from Cryptocurrency Exchanges.')

parser.add_argument('--symbol', nargs='+', help='Symbol of a currency pair (BTC/USDT | ETH/BTC).')
parser.add_argument('--exchange', help='The name of a Exchange (Binance | Bitfinex).')
parser.add_argument('--limit', nargs='?', default=10, type=int, help='Limit of asks/bids of the Order Book (10 | 100 | 1000).')
parser.add_argument('--interval', default=60, type=int, help='Interval to retrieve the Order Book in seconds.')

args = parser.parse_args()

exchange_name = args.exchange.lower()

if (exchange_name == 'binance'):
    exchange.binance(args.symbol, args.interval, args.limit)
elif (exchange_name == 'bittrex'):
    exchange.bittrex(args.symbol, args.interval, args.limit)
elif (exchange_name == 'bitfinex'):
    exchange.bitfinex(args.symbol, args.interval, args.limit)
elif (exchange_name == 'poloniex'):
    exchange.poloniex(args.symbol, args.interval, args.limit)
elif (exchange_name == 'huobi'):
    exchange.huobi(args.symbol, args.interval, args.limit)
else:
    print('Exchange options: Binance, Bittrex, Bitfinex, Poloniex, Huobi\n')

exit()