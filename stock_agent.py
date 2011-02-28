#!/usr/bin/python

import sys

sys.path.append( 'lib/finance')
sys.path.append( 'lib/core' )

import yahoo_finance_interface as yfi
import datetime
import csv_helper as ch
import matplotlib as mpl
import pylab  as pl

start_date = datetime.date(2007, 10,10)
today      = datetime.date.today()

historical = yfi.fetch_historical_prices( "CRI.MC", start_date, today)

historical = ch.store_csv( historical, True, ',')
print historical

pl.plot( historical['Close'])
pl.show()

