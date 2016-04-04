import urllib.request
import json

# returns the local tims for a place provided.
#e.g Input = Montgomery,Alabama
#output = Monday 28th December 2015 11:20 am/pm 
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl2 = 'https://maps.googleapis.com/maps/api/timezone/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    uh = urllib.request.urlopen(url)
    data = uh.read() 

    js = json.loads(data.decode())
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    print('address: ',location)
    myList = [lat,lng] 
    lahy=",".join(str(bit) for bit in myList)    #it will join the lat and lng according to the url format.

    if len(address) < 1 : break
    import time
    sat=time.time()     #returns the gmt time in seconds
    urls = serviceurl2 + urllib.parse.urlencode({'timestamp':int(sat),'location':lahy},'utf-8')
    uhb = urllib.request.urlopen(urls)
    data1 = uhb.read()
    jsm = json.loads(data1.decode()) 
    
    location = jsm["timeZoneId"]
    zone = jsm["timeZoneName"]
    off=jsm["rawOffset"]
    dst=jsm['dstOffset']
    print ('Regeion: ',location,'    Time zone: ',zone,  off,  dst)
    from time import gmtime, strftime
    time=strftime("%A, %d %B %Y %I:%M %p", gmtime(int(sat)+off+3600))
    print('Local time : ',time)
    
   
    
