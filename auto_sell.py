
import logging

import ccxt
import time


def getExchange(exchange_id):
    try:
        exchange = getattr(ccxt, exchange_id)({
            'apiKey': api,
            'secret': secret,
            'verbose': False
        })
    except KeyError as e:
        print("error: " + str(e))
        print("return exchange without api")
        exchange = getattr(ccxt, exchange_id)()
    return exchange


# enter here your api key from 1broker
api = ""
secret = ""
exchange_id = "_1broker"
# interval to check the orders in secs
time_interval = 60*5

# triggers when to close an order
# close at +XX%
triggerPositive = 50 
# close at -XX%
triggerNegative = -10 

# logging file
logging.basicConfig(filename="1broker_sell.log", format="%(asctime)s %(levelname)s : %(message)s", level=logging.INFO)

exchange = getExchange(exchange_id)

while True:
    open_positions = exchange.privateGetPositionOpen()['response']
    for pos in open_positions:
        pos_id = pos['position_id']
        pos_profit = float(pos['profit_loss'])
        pos_profit_percent = float(pos['profit_loss_percent'])
        pos_stop_loss = float(pos['stop_loss'])
        pos_entry = float(pos['entry_price'])
        if pos_profit_percent > 0 and pos_profit_percent > triggerPositive:
            logging.info("Closing position: " + pos_id + " with profit: " + str(pos_profit_percent) + "%")
            # exchange.privateGetPositionClose({'position_id': pos_id})
        elif pos_profit_percent < 0 and pos_profit_percent < triggerNegative:
            logging.info("Closing position: " + pos_id + " with loss: " + str(pos_profit_percent) + "%")
            # exchange.privateGetPositionClose({'position_id': pos_id})
    time.sleep(time_interval)
