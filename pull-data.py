import ast #for converting bytes to dict
import urllib.request
#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

config = {
    'key': 'LN4YK5M0BH5052U7'
}

def get_data(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=5min&apikey=' + config['key']
    #req = urllib.request.urlopen(url)
    with urllib.request.urlopen(url) as req:
        #data = req.read()
        #data_dict =
        return req.read()
#
#    return url
    
yolo_symbols = ['AMC','GME']

test_data = get_data('AMC')
test_data = test_data.decode('UTF-8')
test_data_dict = ast.literal_eval(test_data)
print(test_data_dict['Meta Data'])

#daily
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo
#alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo



#weekly
#https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo


#API DOCUMENTATION:
#https://www.alphavantage.co/documentation/
#SAMPLE RESPONSES
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo
