# 1broker-autoclose

A little pyhton script to check 1broker with a timed intervall and close positions if they reached a trigger.

## Requirements:
* Python 3.6
* ccxt library

Check what python you have installed with: 

`python -V`

=> if it is not Python3.6 => Install Python 3.6 from https://www.python.org/downloads/

After that install the ccxt library via pip:

`pip install ccxt` (if you only have one python version installed)
`pip3.6 install ccxt` (if you have multiple python version installed)

## usage:
Open auto_sell.py with an editor/notepad and add your api-key, the timeinterval you want to run the script and the positive and negative triggers. After that you can run the script with
`python3.6 auto_sell.py`

(the real execution is commented out, if you are satisfied with the actions in the log you have to remove the `#` in the while loop)




## extra:
There is also a google script which will check gains.
You will need to edit the script to add your api-key as token and have a google sheet named like in the script (my sheet is called BTCBalance)

Hint: use triggers in the google script: edit>current project triggers to run the e.g. every working day at 2pm

The first row on the sheet is:

date 	balance 	orders_worth 	positions_worth 	net_worth	Gain BTC	Gain %



### if you want to pay me a beer you are free to send some tip here
* bitcoin: 3NRdkqjeq4DCLeK1B5phfDc996BwHgsAvo
* dash: Xhheppe83wqdy3fFkMidUXa1CUNp2mEou5


