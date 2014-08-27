"""

"""

from fa import F
from numpy import array, zeros, hstack, savetxt, sqrt, power
from numpy.linalg import norm


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                 # Dipole strength  
    D = 0.005                     # Diffusion
    x0 = [0.0, 21.05, 0.0]       # Initial position
    e0 = [1.0, 0.0, 0.0]        # Initial direction
    trials = 2000

    dt = 0.001

    # Parameters to change the variance
    deltaD = 0.002
    maxD   = 0.1
    numD   = maxD / deltaD
    iD     = 0

    filename = "exittimes.csv"

    delta = hstack((x0, e0))
    dist = 20
    t = 0
    N = 0
    sum = 0

    #records = zeros((numD+1, 3))
    records2 = zeros((numD+1, 1))
    
    while (iD <= numD):

        sum = 0
        Ts = zeros(trials+1)

        while (N <= trials):

            t=0
            dist = 21.1
            delta = hstack((x0, e0))

            #print Ts

            while (dist <= 20 + 1.2):

                xk = delta[:3]
                ek = delta[3:]

                delta = delta + dt * F(U, A, alpha, D, xk, ek)[:6] + sqrt(dt) * F(U, A, alpha, D, xk, ek)[6:]
                # We need to renormalize the direction!
                vec = delta[3:]/norm(delta[3:])
                delta[3:] = vec

                position = delta[:3]
                dist = norm(position)

                # Last t is the exit time
                t = t + dt

            # Saving this particular exit time in order to compute the variance later
            Ts[N] = t

            #Computing the average exit time (must renormalize later)
            sum = sum + t
            

            N = N + 1

        N = 0

        print iD

        # Recording the empirical mean

        average = sum / (trials + 1)

        # Computing the empirical variance

        # variance = 0

        # for i in range(0,trials+1):
        #     variance = variance + (Ts[i] - average)**2

        # records[iD] = hstack((iD, average, variance / trials))
        records2[iD] = average
        iD = iD + 1
        D = D + iD * deltaD

    # print records

    # Save the ...
    savetxt(filename, records2)