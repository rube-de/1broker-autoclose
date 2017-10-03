
import logging

import ccxt
import time


def get_exchange(exchange_id):
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


def get_trigger_positive():
    if username == 'snortex':
        return 100
    elif username == '333':
        return 50
    else:
        return trigger_positive


def get_trigger_negative():
        if username == 'snortex':
            return -80
        elif username == '333':
            return -10
        else:
            return trigger_negative


# enter here your api key from 1broker
api = ""
secret = ""
exchange_id = "_1broker"
# interval to check the orders in secs
time_interval = 60*5

# triggers when to close an order
# close at +XX%
trigger_positive = 50
# close at -XX%
trigger_negative = -10

# logging file
logging.basicConfig(filename="1broker_sell.log", format="%(asctime)s %(levelname)s : %(message)s", level=logging.INFO)

exchange = get_exchange(exchange_id)

while True:
    open_positions = exchange.privateGetPositionOpen()['response']
    for pos in open_positions:
        pos_id = pos['position_id']
        pos_profit = float(pos['profit_loss'])
        pos_profit_percent = float(pos['profit_loss_percent'])
        pos_stop_loss = float(pos['stop_loss'])
        pos_entry = float(pos['entry_price'])

        # for copied trades
        pos_copy = pos['copy_of']
        shared_position = exchange.privateGetPositionSharedGet({'position_id': pos_copy})['response']
        username = shared_position['username']

        '''
        # use this for different trader settings
        trigger_positive = get_trigger_positive()
        trigger_negative = get_trigger_negative()
        '''

        if pos_profit_percent > 0 and pos_profit_percent > trigger_positive:
            logging.info("Close position: " + pos_id + " (" + username + ") with profit: " + str(pos_profit_percent) + "%")
            # exchange.privateGetPositionClose({'position_id': pos_id})
        elif pos_profit_percent < 0 and pos_profit_percent < trigger_negative:
            logging.info("Close position: " + pos_id + " (" + username + ") with loss: " + str(pos_profit_percent) + "%")
            # exchange.privateGetPositionClose({'position_id': pos_id})
    time.sleep(time_interval)