
import matplotlib.pyplot as plt
import numpy as np
from invgauss import ivpdf
import pylab as P


# Loading data
data = np.genfromtxt('testdata.csv', delimiter=',')
data[data<1] = 0
data = np.ma.masked_equal(data,0)
data = data.compressed()

N = data.__len__() - 1

# Compute mean and variance
k    = 0
l    = 0
mean = 0
var  = 0

while(k <= N):
	mean = mean + data[k]	
	k    = k + 1

mean = mean / N

while(l <= N):
	var  = var + (data[l] - mean)**2
	l    = l + 1

var = var / N

scale = mean**3 / var

print mean, var, scale

# CREATING HISTOGRAM

#Basic setting
fig = P.figure()
ax = fig.add_subplot(111)

#Plotting the pdf
x = np.linspace(0.01, 20, 100)
P.plot(x, ivpdf(x, mean, scale), 'r-', lw=2, label='Inverse Gaussian pdf')

#Drawing histogram
n, bins, patches = P.hist(data, 200, normed=True, histtype='bar', alpha=0.2, label='Exit angles')
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75, color='mediumslateblue')

#Adding legend
#P.legend(loc='best', frameon=False)

#Adding annotation
ax.annotate('D = 0.01', xy=(110, 0.045), xytext=(115, 0.045))
ax.annotate(u'\u03bc = 20.44', xy=(20, 0.04), xytext=(22, 0.04))
ax.annotate(u'\u03bb = 34.43', xy=(20, 0.037), xytext=(22, 0.037))

P.show()