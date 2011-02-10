#!/usr/bin/ruby

require 'lib/finance/yahoo_finance_interface'
require 'lib/core/csv_helper'

p "Stock Agent"

yfi = YahooFinanceInterface.new

prices = yfi.fetch_historical_prices( "CRI.MC", 
                                      Date.civil(2007, 10, 10), 
                                      Date.today)


data = store_csv( prices, { :header => true})

