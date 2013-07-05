from oauth2client.file import Storage
from datetime import date
from urllib import urlencode
import httplib2

storage = Storage('credentials.json')
credentials = storage.get()


http = httplib2.Http()
http = credentials.authorize(http)

resp, content = http.request("https://prevoz.org/api/accounts/status/", 'GET')
print content


data = {'transptype': 0,
        'transpfrom': 'Ljubljana',
        'transpfromcountry': 'SI',
        'transpto': 'Maribor',
        'transptocountry': 'SI',
        'transpdate': date.today().strftime('%Y-%m-%d'),
        'transptime': '16:35',
        'transpppl': 2,
        'transpprice': 5,
        'transpphone': '040 404 404',
        'transpdescr': 'testni prevoz'
    	}

resp, content = http.request("https://prevoz.org/api/carshare/create/", 'POST', urlencode(data))
print content