import urllib
import datetime
import lxml.etree as le

HOST = "www.invertia.com"
PORT = 80

def parse_float( string, thousand='.', decimal=',' ):
    """ Parses a float string with a given thousands and decimal separator """

    try:
        f_string = string.replace( thousand,"").replace(decimal,".")
        return float(f_string)
    except Exception: return None

def parse_epoch_string_list( array ):
    """ """

    p_array = []

    for epoch in array:
        p_array.append( datetime.datetime.strptime( epoch, "%d/%m/%Y") )

    return p_array


def fetch_results( ticker ):
    """ Fetch results from the invertia page """

    path = "/mercados/bolsa/empresas/resultados.asp?idtel=%s" % ticker

    url_request = urllib.urlopen( "http://" + HOST + path )

    page_string = url_request.read()

    xpath = "//div[@id='result_hist']/table/tbody//tr" 

    doc = le.fromstring( page_string, parser=le.XMLParser(recover=True) )

    elements = doc.xpath( xpath )

    data = []
    headers = []
    
    for element in elements:
        for tag in element:
            if tag.tag == "th": headers.append( tag.text )
            if tag.tag != "td": continue

            data.append( tag.text )

    n_elements = len( data )

    print n_elements, len(headers), n_elements / len( headers)

    print data[0::9]
    print data[1::9]
    print data[2::9]
    print data[3::9]
    print data[4::9]
    print data[5::9]
    print data[6::9]
    print data[7::9]
    print data[8::9]

    return data
