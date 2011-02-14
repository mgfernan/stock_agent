import urllib
import datetime

class YahooFinanceInterface:
    """ YahooFinanceInterface is a class to interface with the Yahoo Financial web site """

    def __init__( self ):
        """ Initialization method """
        self.host = "ichart.finance.yahoo.com"
        self.port = 80


    def fetch_historical_prices( self, ticker, start_date, end_date ):
        """ Fetch historical prices for a given ticker 
            Typical address is
             http://ichart.finance.yahoo.com/table.csv?
                            s=CRI.MC&a=09&b=10&c=2007&d=01&e=3&f=2011&g=d&ignore=.csv
            ticker string identifying the ticker to fetch
            start_date date identifying the start date of the price
            end_date date identifying the end date of the price """

        start_year  = start_date.year
        start_month = start_date.month
        start_day   = start_date.day

        end_year    = end_date.year
        end_month   = end_date.month
        end_day     = end_date.day

        # Build the path 
        path = "/table.csv?s=%s&a=%02d&b=%02d&c=%4d&d=%02d&e=%02d&f=%04d&g=d&ignore=.csv" % ( ticker, start_month-1, start_day, start_year, end_month-1, end_day, end_year )

        url_request = urllib.urlopen( "http://" + self.host + path )

        # Return the string with the CSV format
        return url_request.read()

