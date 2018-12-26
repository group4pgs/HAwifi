import datetime
import urllib.request
import json

def timeDifference(now, sunsetTime):
	nhour, nminute = now.hour, now.minute
	shour, sminute = sunsetTime.hour, sunsetTime.minute
	nsminute, nshour, flag=0,0, False
	if nminute>sminute:
	    nsminute = nminute-sminute
	else:
	    nsminute = nminute+60 - sminute
	    flag = True
	
	if nhour-1 == shour:
	    nshour = 0
	else:
	    if flag == False:
	        nshour = nhour - shour
	    else:
	        nshour = nhour - 1 - shour
	        
	if nshour>=0:
	    nsminute = nsminute+nshour*60
	else:
	    nsminute = -1*(nsminute+nshour*60)
	return nsminute

def calculateDifference():
	now = datetime.datetime.now()
	sunset = json.loads(urllib.request.urlopen("https://api.sunrise-sunset.org/json?lat=12.9716600&lng=77.5946400&date=today&formatted=0").read().decode('utf-8'))
	sunsetTime = sunset['results']['sunset']
	sunsetTime = sunsetTime.replace('-',' ').replace('T',' ')
	sunsetTime = sunsetTime[0:-6]
	sunsetTime = datetime.datetime.strptime(sunsetTime,"%Y %m %d %H:%M:%S")
	sunsetTime=sunsetTime.replace(tzinfo=datetime.timezone.utc) #Convert it to datetime object in UTC
	sunsetTime=sunsetTime.astimezone()
	delta = timeDifference(now, sunsetTime)
	return delta
