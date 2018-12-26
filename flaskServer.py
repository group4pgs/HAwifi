#py_file
from flask import Flask, request, render_template
import Operate as operate	#my GPIO python file
import multiprocessing
import onTimeCalculator as otc
import datetime
import time
import sys

app = Flask(__name__)

@app.route('/')
def input_f():
    return render_template('multipleRoom.html')


@app.route('/',methods=['POST'])
def contact():
	if request.method == 'POST':
		if request.form['options1'] == 'ON':
			operate.ledON(1,True)            
			print("ON")
		elif request.form['options1'] == 'OFF':
			operate.ledOFF(1,False)
			print("OFF")
		else:
			pass
		if request.form['options2'] == 'ON':
			operate.ledON(2,False)            
			print("ON")
		elif request.form['options2'] == 'OFF':
			operate.ledOFF(2,False)
			print("OFF")
		else:
			pass
		if request.form['options3'] == 'ON':
			operate.ledON(3,False)            
			print("ON")
		elif request.form['options3'] == 'OFF':
			operate.ledOFF(3,False)
			print("OFF")
		else:
			print("Invalid")
		return ""
	elif request.method == 'GET':
		return render_template('contact.html', form=form)


def autoOn():
	onTime = otc.onTimeCalc()
	while True:
		time.sleep(10)
		if datetime.datetime.now().hour == onTime.hour and datetime.datetime.now().minute == onTime.minute:
			operate.ledON(1,True)
			print("ON")
			return ""

def hosting():
	app.debug=True
	app.run(host=sys.argv[1],port=sys.argv[2])


if __name__ == '__main__':
	app.debug=True
	p1 = multiprocessing.Process(name = 'p1', target = hosting)
	p2 = multiprocessing.Process(name = 'p2', target = autoOn)
	p1.start()
	p2.start()
