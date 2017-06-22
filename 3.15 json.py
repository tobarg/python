#JSON > serialization format
#JSON presents data as nested "lists" (called arrays) and "dictionaries" - key/value
#values could be strings or objects

#service oriented approach example: hotel website
#APIs application program integration (web services)

#SOAP: simple object access protocol (software)
#REST: representational state transfer (resources)

import urllib
import json

#access token key > for APIs that require authentication (like Twitter)
#OAuth is technique for sending/verifying signatures (not secrets)
#>>> import oauth

#"augment" function adds parameters to URL
#"info()" prints a URL header > add .dict and to convert to dictionary

#deserialize JSON
#>>> js = json.loads(variable_name)

#"pretty" json > indent function
#>>> json.dumps(js, indent=4)

#assignment
import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_281769.json'
www = urllib.urlopen(url).read()

info = json.loads(www)
total = 0

for item in info['comments']:
    total = total + item['count']
print total

#assignment
import urllib
import json

#Google Maps: serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    data = urllib.urlopen(url).read()

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '=== Failure To Retrieve ==='
        continue

    place_id = js['results'][0]['place_id']
    print place_id
    print js['status']

#    lat = js["results"][0]["geometry"]["location"]["lat"]
#    lng = js["results"][0]["geometry"]["location"]["lng"]
#    print 'lat',lat,'lng',lng
