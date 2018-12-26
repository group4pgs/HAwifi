import urllib.request
import json
import datetime
import time
import linRegModel as lrm

def onTimeCalc():
	sunset = json.loads(urllib.request.urlopen("https://api.sunrise-sunset.org/json?lat=12.9716600&lng=77.5946400&date=today&formatted=0").read().decode('utf-8'))
	sunsetTime=sunset['results']['sunset']
	sunsetTime = sunsetTime.replace('-',' ').replace('T',' ')
	sunsetTime = sunsetTime[0:-6]
	sunsetTime = datetime.datetime.strptime(sunsetTime,"%Y %m %d %H:%M:%S")
	sunsetTime=sunsetTime.replace(tzinfo=datetime.timezone.utc) #Convert it to datetime object in UTC
	sunsetTime=sunsetTime.astimezone()
	delta = lrm.calcDelta()
	ontime = sunsetTime-datetime.timedelta(minutes=delta)
	return ontime

