from numpy import genfromtxt
import numpy as np
import pylab as P
from scipy.stats import invgauss

import numpy.random as nr

from scipy.stats import invgauss
import matplotlib.pyplot as plt
import numpy as np


data = genfromtxt('testdata.csv', delimiter=',')

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

#a = nr.wald(2,2)

#fig, ax = plt.subplots(1, 1)

#x = np.linspace(invgauss.ppf(0.01, mean, scale), invgauss.ppf(0.7, mean, scale), 100)

#vals = invgauss.ppf([0.001, 0.5, 0.7], mean)

#ax.plot(vals, invgauss.pdf(vals, mean), 'r-', lw=5, alpha=0.6, label='invgauss pdf')

#r = invgauss.rvs(mean, scale, size=1000)
#ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)

#plt.show()


# (mu, sigma) = norm.fit(data)

n, bins, patches = P.hist(data, 50, normed=1, histtype='bar')
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

# y = mlab.normpdf( bins, mu, sigma)
# l = P.plot(bins, y, 'r--', linewidth=2)

P.show()

# fig, ax = plt.subplots(1, 1)

# mean = 0.145462645553

# x = np.linspace(invgauss.ppf(0.01, mean),invgauss.ppf(0.7, mean), 100)

# rv = invgauss(mean)
# ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# ax.plot(x, invgauss.pdf(x, mean), 'r-', lw=5, alpha=0.6, label='invgauss pdf')

# r = invgauss.rvs(mean, size=1000)

# ax.hist(r, normed=True, histtype='bar', alpha=0.2)
# ax.legend(loc='best', frameon=False)
# plt.show()	