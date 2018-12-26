import pandas

def write_to_csv(value):
	df = pandas.read_csv('value_file.csv')
	df = df.append({'value': value},ignore_index=True)
	try:
		df.pop('Unnamed: 0')
	except:
		pass

	df.to_csv('value_file.csv')


