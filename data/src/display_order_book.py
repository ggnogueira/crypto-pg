import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
