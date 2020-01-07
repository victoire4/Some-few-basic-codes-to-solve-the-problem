import numpy as np								# import all the function that we are going to use and give the small name.
import pylab as pl
import math as m

x=np.arange(-2,2.1,0.1)							# Intervalle of x to -2 from 2 with a small step value 0.1

name=['Kmax=6','Kmax=26']							# The list of the names of the two plots

def y1(x):								# We define the function where Kmax=6
	y=np.zeros(len(x))
	for i in range(len(x)):
		for k in range(1,6,2):					# k is odd number. So, we remove all the even number between 0 and 26
			y[i]+=(4/(k*m.pi))*(m.sin((k*m.pi*x[i])/2))		# We apply the summation for  all k
	return y

def y2(x):								# We define the function where Kmax=26
	y=np.zeros(len(x))							# y is a not vector which have a same lenght that x 
	for i in range(len(x)):
		for k in range(1,26,2):					# k is odd number. So, we remove all the even number between 0 and 26
			y[i]+=(4/(k*m.pi))*(m.sin((k*m.pi*x[i])/2))
	return y

pl.plot(x,y1(x),label=name[0])						# Plot the figure that Kmax=6 (k is a odd numbers)
pl.plot(x,y2(x),label=name[1])						# Plot the figure that Kmax=26 (k is a odd numbers)
pl.legend(loc='best') 										# Put the legend at the best position
pl.title("figure of $f(x)$")							# The title of the figure

pl.show()													# display the figure

# When we change Kmax, we observe that plus the Kmax is bigger, the plot of f(x) is exact
