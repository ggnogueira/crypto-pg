#!/usr/bin/env bash

SYMBOLS='BCH/USDT BTC/USDT DASH/BTC ETC/BTC ETH/BTC ETH/USDT LTC/BTC LTC/USDT OMG/BTC OMG/ETH XRP/BTC ZEC/BTC ZRX/BTC ZRX/ETH'
INTERVAL=60
LIMIT=1000

python ./src/fetch.py --symbol $SYMBOLS --exchange Binance --limit $LIMIT --interval $INTERVAL &
python ./src/fetch.py --symbol $SYMBOLS --exchange Bitfinex --limit $LIMIT --interval $INTERVAL &
python ./src/fetch.py --symbol $SYMBOLS --exchange Bittrex --limit $LIMIT --interval $INTERVAL &
python ./src/fetch.py --symbol $SYMBOLS --exchange Poloniex --limit $LIMIT --interval $INTERVAL &
python ./src/fetch.py --symbol $SYMBOLS --exchange Huobi --limit $LIMIT --interval $INTERVAL &