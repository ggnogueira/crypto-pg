import argparse
import exchange

parser = argparse.ArgumentParser(description='Collect some data from Cryptocurrency Exchanges.')

parser.add_argument('--symbol', help='Symbol of a currency pair (BTC/USDT | ETH/BTC).')
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

# Binance - OrderBook com limite 1000
binance_exchange = ccxt.binance()

print("-> Exchange " + binance_exchange.id + " pronta!")

binance_exchange_markets = binance_exchange.load_markets()

print("-> " + binance_exchange.id + " carregou o mercado")

options = input('-> Menu Binance:\n1- Exchange Info\t2- Lista de Pares\n3- Lista de Moedas\t4- Outros\n')
if options == 1:
    pprint(binance_exchange)
elif options == 2:
    pprint(binance_exchange.symbols)
    symbol = raw_input('-> Escolha uma moeda (ETH/BTC, BTC/USDT, LTC/BTC): ')
elif options == 3:
    pprint(binance_exchange.currencies)
else:
    pprint('Em andamento...')

print('-> Buscando no livro de ofertas da ' + binance_exchange.id + ' ' + symbol +' (Limite = 10):\n')


# Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
# Parametros (par, intervalo_de_tempo, limite)
binance_trade = binance_exchange.fetch_trades(symbol, None, 1)
timestamp = binance_trade[0]['timestamp']

# Retorna os X primeiros bidask em cada lado do livro de ofertas
limit = 100

binance_exchange_orders = binance_exchange.fetch_order_book(symbol, limit)
#pprint(binance_exchange_orders)

asks_amount = [0] * limit
asks_prices = [0] * limit
bids_amount = [0] * limit
bids_prices = [0] * limit

for i in range(0,limit):
    asks_prices[i] = binance_exchange_orders['asks'][i][0]
    for j in range(0,i+1):
        asks_amount[i] += binance_exchange_orders['asks'][j][1]


for i in range(0,limit):
    bids_prices[i] = binance_exchange_orders['bids'][i][0]
    for j in range(0,i+1):
        bids_amount[i] += binance_exchange_orders['bids'][j][1]

plt.plot(asks_prices, asks_amount, bids_prices, bids_amount, marker='.', color='black')
plt.xlabel('Price')
plt.ylabel('Amount')
red_patch = mpatches.Patch(color='red', label='bids')
green_patch = mpatches.Patch(color='green', label='asks')
plt.legend(handles=[red_patch, green_patch])
# grab a reference to the current axes
ax = plt.gca()
# set the xlimits to be the reverse of the current xlimits
ax.set_xlim(ax.get_xlim()[::-1])
# call `draw` to re-render the graph
plt.draw()
plt.fill_between(asks_prices, asks_amount, color='green')
plt.fill_between(bids_prices, bids_amount, color='red')
plt.show()

# Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
# Parametros (par, intervalo_de_tempo, limite)

binance_trade2 = binance_exchange.fetch_trades(symbol, timestamp, 10)
#pprint(binance_trade2)

exit()
# Poloniex - OrderBook com limite 1000

poloniex_exchange = ccxt.poloniex()

print("-> Exchange " + poloniex_exchange.id + " pronta!")

poloniex_exchange_markets = poloniex_exchange.load_markets()

print("-> " + poloniex_exchange.id + " carregou o mercado")

print("-> Buscando no livro de ofertas da " + poloniex_exchange.id + " ETH/BTC:\n")


# Retorna os 5 primeiros bidask em cada lado do livro de ofertas
# Parametros (par, intervalo_de_tempo, limite)
poloniex_trade = poloniex_exchange.fetch_trades(symbol, None, 1)
trade_id_poloniex = poloniex_trade[0]['id']

# Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
#pprint(poloniex_exchange.fetch_order_book(symbol, limit))

poloniex_trade2 = poloniex_exchange.fetch_trades(symbol, trade_id_poloniex, 10)
pprint(poloniex_trade2)

# Bittrex - OrderBook com limite 100

bittrex_exchange = ccxt.bittrex()

print("-> Exchange " + bittrex_exchange.id + " pronta!")

bittrex_exchange_markets = bittrex_exchange.load_markets()

print("-> " + bittrex_exchange.id + " carregou o mercado")

print("-> Buscando no livro de ofertas da " + bittrex_exchange.id + " ETH/BTC:\n")

# Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)

bittrex_trade = bittrex_exchange.fetch_trades(symbol, None, 1)
timestamp_bittrex = bittrex_trade[0]['timestamp']
# Comentado pq o limite nao esta funcionando
#pprint(bittrex_exchange.fetch_order_book(symbol, 1000))

# Retorna os 5 primeiros bidask em cada lado do livro de ofertas
# Parametros (par, intervalo_de_tempo, limite)
bittrex_trade2 = bittrex_exchange.fetch_trades(symbol, timestamp_bittrex, 5)
#pprint(bittrex_trade2)


# Bitfinex - OrderBook com limite 1000

bitfinex_exchange = ccxt.bitfinex()

print("-> Exchange " + bitfinex_exchange.id + " pronta!")

bitfinex_exchange_markets = bitfinex_exchange.load_markets()

print("-> " + bitfinex_exchange.id + " carregou o mercado")

print("-> Buscando no livro de ofertas da " + bitfinex_exchange.id + " ETH/BTC:\n")

# Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
#pprint(bitfinex_exchange.fetch_order_book(symbol, 1000))

# Retorna os 5 primeiros bidask em cada lado do livro de ofertas
# Parametros (par, intervalo_de_tempo, limite)
bitfinex_trade = bitfinex_exchange.fetch_trades(symbol, None, 1)
trade_id = bitfinex_trade[0]['id']
print(bitfinex_trade)

sleep(10)

bitfinex_trade2 = bitfinex_exchange.fetch_trades(symbol, trade_id, 5)
print(bitfinex_trade)

# Huobi - OrderBook com limite de 150

huobi_exchange = ccxt.huobipro()
print("-> Exchange " + huobi_exchange.id + " pronta!")

huobi_exchange_markets = huobi_exchange.load_markets()

print("-> " + huobi_exchange.id + " carregou o mercado")

print("-> Buscando no livro de ofertas da " + huobi_exchange.id + " ETH/BTC:\n")

# Retorna as trades efetudas em determinado par (ETH/BTC | BTC/USD)
# Parametro limit nao esta funcionando

#pprint(huobi_exchange.fetch_order_book(symbol, 1000))

# Retorna os 5 primeiros bidask em cada lado do livro de ofertas
# Parametros (par, intervalo_de_tempo, limite)
huobi_trade = huobi_exchange.fetch_trades(symbol, None, 1)