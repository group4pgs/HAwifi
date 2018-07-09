#py_file
from flask import Flask, request, render_template
import Operate as operate	#my Arduino handling python file

app = Flask(__name__)

@app.route('/')
def input_f():
    return render_template('multipleRoom.html')


@app.route('/',methods=['POST'])
def contact():
	if request.method == 'POST':
		if request.form['options1'] == 'ON':
			operate.ledON(1)            
			print("ON")
		elif request.form['options1'] == 'OFF':
			operate.ledOFF(1)
			print("OFF")
		else:
			pass
		if request.form['options2'] == 'ON':
			operate.ledON(2)            
			print("ON")
		elif request.form['options2'] == 'OFF':
			operate.ledOFF(2)
			print("OFF")
		else:
			pass
		if request.form['options3'] == 'ON':
			operate.ledON(3)            
			print("ON")
		elif request.form['options3'] == 'OFF':
			operate.ledOFF(3)
			print("OFF")
		else:
			print("Invalid")
		return ""
	elif request.method == 'GET':
		return render_template('contact.html', form=form)



if __name__ == '__main__':
	app.debug=True
	app.run(host="0.0.0.0",port=8000)
