"""

"""

from fa import F
from numpy import array, zeros, hstack, savetxt, sqrt, power
from numpy.linalg import norm


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                # Dipole strength  
    D = 0.4                  # Diffusion
    x0 = [0.0, 21.2, 0.0]  # Initial position
    e0 = [1.0, 0.0, 0.0]       # Initial direction
    trials = 1000

    dt = 0.1

    filename = "exittimes.csv"

    delta = hstack((x0, e0))
    dist = 20
    t = 0
    N = 0
    sum = 0

    records = zeros((N,1))
    
    while (N <= trials):
        while (norm(delta) <= 20 + 1.4):

            xk = delta[:3]
            ek = delta[3:]

            delta = delta + dt * F(U, A, alpha, D, xk, ek)[:6] + sqrt(dt) * F(U, A, alpha, D, xk, ek)[6:]
            t = t + dt
            # We need to renormalize the direction!
            vec = delta[3:]/norm(delta[3:])
            delta[3:] = vec

            position = delta[:3]
            dist = norm(position)

        #print N
        #print t

        sum = sum + t
        #print sum

        delta = hstack((x0, e0))
        dist = 20
        N = N + 1
        t = 0

    # Save the ...
    #savetxt(filename, t)