#!/usr/bin/ruby

require 'lib/finance/yahoo_finance_interface'

p "Stock Agent"

yfi = YahooFinanceInterface.new

prices = yfi.fetch_historical_prices( "CRI.MC", 
                                      Date.civil(2007, 10, 10), 
                                      Date.today)

p prices
p prices.class.name

