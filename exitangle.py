"""

"""

from fa import F
from numpy import array, zeros, hstack, savetxt, sqrt, power, pi, arccos, dot
from numpy.linalg import norm
import pylab as P


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                 # Dipole strength  
    D = 0.05                     # Diffusion
    x0 = [0.0, 21.15, 0.0]       # Initial position
    e0 = [1.0, 0.0, 0.0]        # Initial direction

    trials = 10000


    dt = 0.001

    # Parameters to change the variance
    # deltaD = 0.01
    # maxD   = 0.8
    # numD   = maxD / deltaD
    # iD     = 0

    filename = "exittimes.csv"
    

    sum = 0
    Ts = zeros(trials+1)
    N=0

    print D, trials

    while (N <= trials):

        t=0
        dist = 21.1
        delta = hstack((x0, e0))
        lastAngle = 0

        #print Ts

        while (lastAngle <= pi/9):

            xk = delta[:3]
            ek = delta[3:]

            delta = delta + dt * F(U, A, alpha, D, xk, ek)[:6] + sqrt(dt) * F(U, A, alpha, D, xk, ek)[6:]
            # We need to renormalize the direction!
            vec = delta[3:]/norm(delta[3:])
            delta[3:] = vec

            position = delta[:3]
            dist = norm(position)

            #pos = delta[k + 1, :3]
            #dist[k+1] = norm(pos) - A - 1

            ray = position / dist
            cosAngle = dot(ray, vec)
            ang = arccos(cosAngle)
            ang = pi / 2 - ang
            lastAngle = ang

            # Last t is the exit time
            t = t + dt

        # Saving this particular exit time in order to compute the variance later
        Ts[N] = t

        #Computing the average exit time (must renormalize later)
        sum = sum + t

        #Computing the average exit time (must renormalize later)
        #sum = sum + t
        

        N = N + 1

        if(N%100 == 0):
            print N

    # Recording the empirical mean

    #average = sum / (trials + 1)
    #print average

    # Computing the empirical variance

    # variance = 0

    # for i in range(0,trials+1):
    #     variance = variance + (Ts[i] - average)**2

    # variance = variance / (trials + 1)
    # print variance

    print D, trials
    

    # the histogram of the data with histtype='step'
    n, bins, patches = P.hist(Ts, 50, normed=1, histtype='bar')
    P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

    P.show()