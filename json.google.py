import urllib, json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    data = urllib.urlopen(url).read()

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '=== Failure to Retrieve ==='
        print data
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    print 'Location:', location
    print 'lat',lat,'lng',lng

