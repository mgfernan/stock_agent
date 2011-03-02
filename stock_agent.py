#!/usr/bin/python

import sys

sys.path.append( 'lib/finance')
sys.path.append( 'lib/core' )

import yahoo_finance_interface as yfi
import datetime
import csv_helper as ch
import matplotlib as mpl
import pylab  as pl
import list_extension as le

start_date = datetime.date(2007, 10,10)
today      = datetime.date.today()

historical = yfi.fetch_historical_prices( "CRI.MC", start_date, today)

historical = ch.store_csv( historical, True, ',')

historical['Close'] = le.convert_to_float_list( historical['Close'] )
print historical
print historical['Close']

pl.plot( historical['Close'])
pl.show()

