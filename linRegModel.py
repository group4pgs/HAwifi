from scipy import stats
import numpy as np
import pandas as pd


def calcDelta():
	df = pd.read_csv('value_file.csv')
	x = np.arange(len(df['value']))
	y = np.asarray(df['value'])
	
	slope, intercept,a,b,c = stats.linregress(x,y)
	last = x[-1]
	deltaON = (slope*(last+1))+intercept
	return deltaON

