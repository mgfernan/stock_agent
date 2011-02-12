#!/usr/bin/ruby

require 'lib/finance/yahoo_finance_interface'
require 'lib/core/csv_helper'
require 'lib/core/array_extension'

p "Stock Agent"

yfi = YahooFinanceInterface.new

prices = yfi.fetch_historical_prices( "CRI.MC", 
                                      Date.civil(2007, 10, 10), 
                                      Date.today)
prices = yfi.fetch_historical_prices( "TEF.MC", 
                                      Date.civil(2007, 10, 10), 
                                      Date.today)



data = store_csv( prices, { :header => true})

data.each_key { |key| p key }

p data["Date"][0]

dates = data["Date"].reverse
prices = data["Adj Close"].reverse

prices.each_with_index { |value, i_value| prices[i_value] = value.to_f }

prices_sma_fast = prices.compute_sliding_window( { :n_samples => 10, :delay => 'front', :missing_nil => false } )
prices_sma_slow = prices.compute_sliding_window( { :n_samples => 20, :delay => 'front', :missing_nil => false } )

(0...prices.size).each do |i|
    print "#{dates[i]} #{prices[i]} #{prices_sma_fast[i]} #{prices_sma_slow[i]}\n"
end

# Simulation 
account  = 6000.0
n_stocks = 0
value    = 0.0
stop_loss = 20.0

# Does not seem too optimistic. Possible ways to overcome the limitations:
# 1.- Add a "MOMENTUM" indicator based on the first derivative analysis
# 2.- Add Resistance and Support check
# 
# Other things to implement
# 1.- Sector based trading.
purchase_price = prices[0]
(1...prices.size).each do |i|

    time_to_buy  = ( ( prices_sma_fast[i]   >= prices_sma_slow[i] ) && 
                     ( prices_sma_fast[i-1] <  prices_sma_slow[i-1] ) )
    time_to_sell = ( ( prices_sma_fast[i]   <= prices_sma_slow[i] ) && 
                     ( prices_sma_fast[i-1] >  prices_sma_slow[i-1] ) ) ||
                     ( prices[i] - purchase_price)/purchase_price*100.0 > stop_loss 

    if time_to_buy then
        n_stocks = ( account / prices[i] ).to_i
        value    = n_stocks * prices[i]
        purchase_price = prices[i]
        account  = account - value
    end

    if time_to_sell && n_stocks > 0 then
        account  = account + n_stocks*prices[i]
        n_stocks = 0
        print "OPERATION #{dates[i]} #{account} \n"
    end


end

