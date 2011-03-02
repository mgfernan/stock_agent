#!/usr/bin/python

import sys

sys.path.append( 'lib/core' )
sys.path.append( 'lib/finance')
sys.path.append( 'lib/math' )

import yahoo_finance_interface as yfi
import datetime
import csv_helper as ch
import matplotlib as mpl
import pylab  as pl
import list_extension as le
import signal_processing as sp

start_date = datetime.date(2007, 10,10)
today      = datetime.date.today()

historical = yfi.fetch_historical_prices( "CRI.MC", start_date, today)

historical = ch.store_csv( historical, True, ',')

historical['Close'] = le.convert_to_float_list( historical['Close'] )

price = le.reverse( historical['Close'] )

price_ema = sp.compute_ema( price, 10 )
price_ema_slow = sp.compute_ema( price, 5)

pl.plot( price )
pl.plot( price_ema )
pl.plot( price_ema_slow )
pl.show()

