
from numpy import loadtxt
from matplotlib import pylab, axes, pyplot


if __name__ == "__main__":

    filename = "angles.csv"
    data = loadtxt(filename)

    d = data[:]

    pylab.plot(d)
    pylab.show()