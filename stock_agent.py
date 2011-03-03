#!/usr/bin/python

import sys

sys.path.append( 'lib/core' )
sys.path.append( 'lib/finance')
sys.path.append( 'lib/math' )

import math

import yahoo_finance_interface as yfi
import datetime
import csv_helper as ch
import matplotlib as mpl
import pylab  as pl
import list_extension as le
import dict_extension as de
import signal_processing as sp

start_date = datetime.date(2007, 10,10)
today      = datetime.date.today()

#historical = yfi.fetch_historical_prices( "CRI.MC", start_date, today)
historical = yfi.fetch_historical_prices( "TEF.MC", start_date, today)

historical = ch.store_csv( historical, True, ',')

historical['Close'] = le.convert_to_float_list( historical['Close'] )

price = le.reverse( historical['Close'] )
dates = le.reverse( historical['Date'] )

price_ema_slow = sp.compute_ema( price, 30 )
price_ema_fast = sp.compute_ema( price, 10 )

#pl.plot( price )
#pl.plot( price_ema_slow )
#pl.plot( price_ema_fast )
#pl.draw()

# Simulation 
account   = 6000.0
n_stocks  = 0
value     = 0.0
stop_loss = 1.0 # Percentual

# Does not seem too optimistic. Possible ways to overcome the limitations:
# 1.- Add a "MOMENTUM" indicator based on the first derivative analysis
# 2.- Add Resistance and Support check
# 
# Other things to implement
# 1.- Sector based trading.
n_sessions = len( price )

operations_dates = []
operations = []

for i in xrange( n_sessions ):

    if i == 0.0: continue

    time_to_buy  = ( ( price_ema_fast[i]   >= price_ema_slow[i] ) and 
                     ( price_ema_fast[i-1] <  price_ema_slow[i-1] ) )
    time_to_sell = ( ( price_ema_fast[i]   <= price_ema_slow[i] ) and 
                     ( price_ema_fast[i-1] >  price_ema_slow[i-1] ) ) 
    
    date = datetime.datetime.strptime( dates[i], "%Y-%m-%d" )

    # Check stop loss condition
    if n_stocks > 0:
        stop_loss_price = (1.0-stop_loss/100.0) * purchase_price
        is_stop_loss =  ( price[i] < stop_loss_price )
        print date, price[i], purchase_price, stop_loss_price, is_stop_loss
        time_to_sell = time_to_sell or is_stop_loss
    
    if time_to_buy:
        n_stocks = math.floor( account / price[i] )
        value    = n_stocks * price[i]
        purchase_price = price[i]
        account        = account - value

    if time_to_sell and n_stocks > 0:
        account  = account + n_stocks*price[i]
        n_stocks = 0
        operations_dates.append(date)
        operations.append( account )

pl.plot( operations_dates, operations,'k.-' )
pl.show()
