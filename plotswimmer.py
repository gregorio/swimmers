
from numpy import loadtxt
from matplotlib import pylab


if __name__ == "__main__":

    filename = "results.csv"
    data = loadtxt(filename)

    t = data[:, 0]
    x = data[:, 1:4]
    e = data[:, 4:]

    pylab.plot(x[:, 0], x[:, 1])
    pylab.show()

   
