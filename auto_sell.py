
import sys
import logging

import ccxt
import time
import datetime


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


def get_trigger_positive(username):
    if username == 'snortex':
        return 200
    elif username == '333':
        return 50
    else:
        return trigger_positive_def


def get_trigger_negative(username):
        if username == 'snortex':
            return -50
        elif username == '333':
            return -10
        else:
            return trigger_negative_def


# enter here your api key from 1broker
api = ""
secret = ""
exchange_id = "_1broker"
# interval to check the orders in secs
time_interval = 60*5

# triggers when to close an order
# close at +XX%
trigger_positive_def = 50
# close at -XX%
trigger_negative_def = -10

# logging file
logging.basicConfig(filename="1broker_sell.log", format="%(asctime)s %(levelname)s : %(message)s", level=logging.INFO)

exchange = get_exchange(exchange_id)

while True:
    try:        
        open_positions = exchange.privateGetPositionOpen()['response']  
       
        curTime = time.time()    
        mydate = datetime.datetime.fromtimestamp(curTime)    
        mydate = mydate.strftime('%Y%m%d_%H:%M:%S')    
        print("--- {0:s} ----------------------------------------".format(mydate))    
        print("{1:d} open positions found".format(mydate, len(open_positions)))

        for pos in open_positions:
            pos_id = pos['position_id']
            pos_profit = float(pos['profit_loss'])
            pos_profit_percent = float(pos['profit_loss_percent'])
            pos_stop_loss = float(pos['stop_loss'])
            pos_entry = float(pos['entry_price'])

            # for copied trades
            pos_copy = pos['copy_of'] 
            if (pos_copy != None) and (int(pos_copy) > 0):          
                shared_position = exchange.privateGetPositionSharedGet({'position_id': pos_copy})['response']                
                username = shared_position['username']
            else:
                username = '-- own --'
                pos_copy = str(-1)

            # use this for different trader settings        
            trigger_positive = get_trigger_positive(username)
            trigger_negative = get_trigger_negative(username)

            if pos_profit_percent > 0 and pos_profit_percent > trigger_positive:
                print("  profit trigger {0:d}% reached, trade closed".format(trigger_positive))
                logging.info("Close position: " + pos_id + " (" + username + ") with profit: " + str(pos_profit_percent) + "%")
                # exchange.privateGetPositionClose({'position_id': pos_id})
            elif pos_profit_percent < 0 and pos_profit_percent < trigger_negative:
                print("  loss trigger {0:d}% reached, trade closed".format(trigger_negative))
                logging.info("Close position: " + pos_id + " (" + username + ") with loss: " + str(pos_profit_percent) + "%")
                # exchange.privateGetPositionClose({'position_id': pos_id})
    except:        
        (type, value, traceback) = sys.exc_info()
        print("Exception:")
        print(type)
        print(value)
        print(traceback)
    print()
    time.sleep(time_interval)
