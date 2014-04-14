"""

"""

from fa import F
from numpy import array, zeros, hstack, savetxt


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                 # Dipole strength  
    D = 0.01                    # Diffusion
    x0 = [30.0, 30.0, 0.0]      # Initial position
    e0 = [0, -1.0, 0.0]       # Initial direction

    # Integration Parameters
    T = 100     # Final time
    dt = 0.01   # Mesh 
    N = int(T / dt)  # Number of iterations
    filename = "results.csv"

    delta = zeros((N, 6))
    t = zeros((N,1))

    delta[0, :] = hstack((x0, e0))
    t[0] = 0
    
    for k in range(0, N - 1):

        xk = delta[k, :3]
        ek = delta[k, 3:]

        delta[k + 1, :] = delta[k, :] + dt * F(U, A, alpha, D, xk, ek)
        t[k + 1] = t[k] + dt

    # Save the ...
    savetxt(filename, hstack((t, delta)))
    

