from oauth2client.file import Storage
from datetime import date
from urllib import urlencode
import httplib2
import json

storage = Storage('credentials.json')
credentials = storage.get()


http = httplib2.Http()
http = credentials.authorize(http)

print "\n\nRead our status - username and if we're authenticated:"
resp, content = http.request("https://prevoz.org/api/accounts/status/", "GET")
print content

print "\n\nCreate a new carshare:\n"
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

resp, content = http.request("https://prevoz.org/api/carshare/create/", "POST", urlencode(data))
print content
data = json.loads(content)
carshare_id = data["id"]

print "\n\nDelete this carshare (since it's a live site and we don't want to dirty it)\n"

resp, content = http.request("https://prevoz.org/api/carshare/delete/%s" % carshare_id, "POST")
print content