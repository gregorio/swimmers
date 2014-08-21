"""

"""

from fa import F
from numpy import array, zeros, hstack, savetxt, sqrt, power, pi, arccos, dot
from numpy.linalg import norm


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                # Dipole strength  
    D = 0               # Diffusion
    x0 = [0.0, 21.1, 0.0]  # Initial position
    e0 = [1.0, 0.0, 0.0]       # Initial direction

    # Integration Parameters
    T = 10     # Final time
    dt = 0.001   # Mesh 
    N = int(T / dt)  # Number of iterations
    filename = "angles.csv"

    delta = zeros((N, 6))
    t = zeros((N, 1))
    dist = zeros((N, 1))
    angle = zeros((N, 1))

    delta[0, :] = hstack((x0, e0))
    t[0] = 0
    
    for k in range(0, N - 1):

        xk = delta[k, :3]
        ek = delta[k, 3:]

        delta[k + 1, :] = delta[k, :] + dt * F(U, A, alpha, D, xk, ek)[:6] + sqrt(dt) * F(U, A, alpha, D, xk, ek)[6:]
        t[k + 1] = t[k] + dt
        # We need to renormalize the direction!
        vec = delta[k + 1, 3:]/norm(delta[k + 1, 3:])
        delta[k + 1, 3:] = vec

        pos = delta[k + 1, :3]
        dist[k+1] = norm(pos) - A - 1

        ray = pos / norm(pos)
        cosAngle = dot(ray, vec)
        ang = arccos(cosAngle)
        ang = pi / 2 - ang
        angle[k+1] = ang

    # Save the ...
    savetxt(filename, angle)