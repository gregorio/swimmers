#!/usr/bin/env python
import numpy as np
import pylab as P

#
# The hist() function now has a lot more options
#

#
# first create a single histogram
#
mu, sigma = 200, 25
x = mu + sigma*P.randn(10000)

# the histogram of the data with histtype='step'
n, bins, patches = P.hist(x, 50, normed=1, histtype='bar')
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)




#
# create a histogram by providing the bin edges (unequally spaced)
#
P.show()
