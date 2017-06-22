import urllib2, base64, json, re
username = 'mediaplanet_api@moat.com'
password = 'm3D!a+p&1'

url = 'https://api2.moat.com/1/stats.json?start=20151201&end=20151231&level1=US&columns=level1,level4,impressions_analyzed,session_time,page_dwell_time,time_to_scroll_percent,scroll_depth_percent,page_dwell_time_lt_30s_percent'
req = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header('Authorization', 'Basic %s' % base64string)

try: data = urllib2.urlopen(req).read()
except urllib2.URLError: print '=== Authorization Failed ==='

try: api = json.loads(str(data))
except: api = None

#delete
print json.dumps(api, indent=4)

top = dict()
bot = dict()

for article in api['results']['details']:
    url = article['level1_id'] + ' ' + article['level4_id']
    pv = int(article['impressions_analyzed'])
    apdt = int(article['page_dwell_time'])
    adr = int(article['page_dwell_time_lt_30s_percent'])
    if pv >= 200:
        if adr <= 25:
            if apdt >= 60:
                top[url] = top.get(url,adr)
                print url, 'ADR:', adr, '%'
#        elif adr >= 50:

sorted(top.items(), key=lambda x:x[1])
