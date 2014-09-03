
from numpy import pi, exp, sqrt
from numpy.linalg import norm

def ivpdf(x, mu, lm):

        return lm / sqrt(2*pi*x**3) * exp(-lm*(x-mu)**2/(2*x*mu**2))



