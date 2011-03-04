#!/usr/bin/python

import sys

sys.path.append( 'lib/core' )
sys.path.append( 'lib/finance')
sys.path.append( 'lib/math' )

import math
import numpy as np
import matplotlib as mpl
import pylab as pl
import scipy
from scipy import optimize
import datetime


import yahoo_finance_interface as yfi
import csv_helper as ch

import list_extension as le
import dict_extension as de
import signal_processing as sp


def fit_fundamental_analysis( time, prices ):
    """ Fundamental analysis found at http://es.wikipedia.org/wiki/An%C3%A1lisis_fundamental """

    # Target function
    fitfunc = lambda p, x: p[0] + p[1]*np.cos( p[2]*x + p[3] ) 
    # Distance to the target function
    errfunc = lambda p, x, y: fitfunc(p, x) - y 

    ## Initial guess for the parameters
    p0 = [ prices[0], 1.0, 1.0, 0.0 ]

    t = np.array(time)
    p = np.array(prices)

    p1,success = optimize.leastsq(errfunc, p0, args=(t, p))

    print p1


    #pl.plot( time, prices)
    pl.plot( fitfunc( p1, t) )
    pl.show()

    return p1






start_date = datetime.date(2007, 10,10)
today      = datetime.date.today()

historical = yfi.fetch_historical_prices( "CRI.MC", start_date, today)
#historical = yfi.fetch_historical_prices( "TEF.MC", start_date, today)

historical = ch.store_csv( historical, True, ',')

historical['Close'] = le.convert_to_float_list( historical['Close'] )

price = le.reverse( historical['Close'] )
dates = le.reverse( historical['Date'] )

price_ema_slow = sp.compute_ema( price, 30 )
price_ema_fast = sp.compute_ema( price, 10 )


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
dt = []

start_date =  datetime.datetime.strptime( dates[1], "%Y-%m-%d" )

#pl.plot( price_ema_slow )
#pl.plot( price_ema_fast )
#pl.draw()
for i in xrange( n_sessions ):

    if i == 0.0: continue

    time_to_buy  = ( ( price_ema_fast[i]   >= price_ema_slow[i] ) and 
                     ( price_ema_fast[i-1] <  price_ema_slow[i-1] ) )
    time_to_sell = ( ( price_ema_fast[i]   <= price_ema_slow[i] ) and 
                     ( price_ema_fast[i-1] >  price_ema_slow[i-1] ) ) 
    
    date = datetime.datetime.strptime( dates[i], "%Y-%m-%d" )
    dt.append( (date-start_date).days )

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

print len(dt), len(price[1:])

print fit_fundamental_analysis( dt, price[1:] )
pl.plot( dt, price[1:] )
#pl.plot( operations_dates, operations,'k.-' )
pl.show()
