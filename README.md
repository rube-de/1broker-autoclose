# 1broker-autoclose

A little pyhton script to check 1broker with a timed intervall and close positions if they reached a trigger.

Requirements:

* Python 3.6
* ccxt library

Check what python you have installed with: 
python -V
=> if it is not Python3.6 => Install Python 3.6 from https://www.python.org/downloads/

After that install the ccxt library via pip:
pip3.6 install ccxt

usage:
python3.6 auto_sell.py




extra:
there is also a google script which will check gains.
you will need to edit the script to add your api-key as token and have a google sheet named like in the script (my sheet is called BTCBalance)
the first row on the sheet is:
date 	balance 	orders_worth 	positions_worth 	net_worth	Gain BTC	Gain %




