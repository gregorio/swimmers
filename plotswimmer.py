
from numpy import loadtxt
from matplotlib import pylab, axes, pyplot


if __name__ == "__main__":

    filename = "results.csv"
    data = loadtxt(filename)

    cir = pylab.Circle((0.0,0.0), radius=20.0,  fc='y')
    pylab.gca().add_patch(cir)
    cir = pylab.Circle((0.0,21.1), radius=1.0, alpha =.2, fc='b')
    pylab.gca().add_patch(cir)
    pylab.axis('scaled')

    t = data[:, 0]
    x = data[:, 1:4]
    e = data[:, 4:6]
    d = data[:, 6]

    #pylab.axes(xscale=None, yscale=None)


    pylab.plot(x[:, 0], x[:, 1])
    pyplot.xlim([-100,100])
    pyplot.ylim([-50,50])
    pylab.show()

   
