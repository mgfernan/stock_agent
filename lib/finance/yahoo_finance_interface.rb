require 'net/http'
require 'uri'
require 'date'

# YahooFinanceInterface is a class to interface with the Yahoo Financial web site
class YahooFinanceInterface

    def initialize
        @host = "ichart.finance.yahoo.com"
        @port = 80
    end

    # Fetch historical prices for a given ticker
    # Typical address is
    #  http://ichart.finance.yahoo.com/table.csv?s=CRI.MC&a=09&b=10&c=2007&d=01&e=3&f=2011&g=d&ignore=.csv
    def fetch_historical_prices( ticker, start_date, end_date )

        # Retrieve the date paramters
        start_year  = start_date.year
        start_month = start_date.month
        start_day   = start_date.day

        end_year    = end_date.year
        end_month   = end_date.month
        end_day     = end_date.day

        # Build the path
        path = "/table.csv?s=#{ticker}&a=%02d&b=%02d&c=%4d&d=%02d&e=%02d&f=%04d&g=d&ignore=.csv" % [ start_month-1, start_day, start_year, end_month-1, end_day, end_year ]

        req = Net::HTTP::Get.new( path )
        
        res = Net::HTTP.start( @host , @port) {|http|
            http.request(req)
        }

        # The body of the request contains the CSV formatted data
        return res.body

    end

end
