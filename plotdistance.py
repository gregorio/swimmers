
from numpy import loadtxt
from matplotlib import pylab, axes, pyplot


if __name__ == "__main__":

    filename = "distance.csv"
    data = loadtxt(filename)

    #filename2 = "results2.csv"
    #data2 = loadtxt(filename2)

    #cir = pylab.Circle((0.0,0.0), radius=20.0,  fc='y')
    #pylab.gca().add_patch(cir)
    #cir = pylab.Circle((0.0,21.0), radius=1.0, alpha =.2, fc='b')
    #cir = pylab.Circle((0.0,21.1), radius=1.0, alpha =.2, fc='b')
    #pylab.gca().add_patch(cir)
    #pylab.axis('scaled')

    t = data[1:, 0]
    d = data[1:, 1]

    #t2 = data2[:, 0]
    #x2 = data2[:, 1:4]
    #e2 = data2[:, 4:6]

    #pylab.axes(xscale=None, yscale=None)


    pylab.plot(t, d)
    #pylab.plot(x2[:, 0], x2[:, 1])
    #pyplot.xlim([-100,100])
    #pyplot.ylim([-66,66])
    pylab.show()

   
