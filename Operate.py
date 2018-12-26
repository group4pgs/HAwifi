import RPi.GPIO as gpio
import timeDifference as td
import pandasWriter as pw
import datetime
import linRegModel as lrm
import json
import time
import urllib.request


def ledON(ledPin,flag):
	try:
		gpio.output(pinList[ledPin-1],gpio.HIGH)
		if datetime.datetime.now().hour >= 16 and flag==True:
			diff = td.calculateDifference()
			pw.write_to_csv(diff)
		
	except:
		print("FAILED TO ON")

def ledOFF(ledPin,flag):
	try:
		gpio.output(pinList[ledPin-1],gpio.LOW)
	except:
		print("FAILED TO OFF")



gpio.setmode(gpio.BCM)
str_temp = open("PinNum.txt").read()
pinListStr = str_temp.split()
pinList = []
for k in pinListStr:
	pinList.append(int(k))
gpio.setup(pinList,gpio.OUT)

