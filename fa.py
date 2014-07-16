"""Computes the position increment and angular variation using the full approximation 


"""

# Import relevant commands
from numpy import array, dot, cross, arctan2, sin, cos, power, hstack
from numpy.linalg import norm


def F(U, A, alpha, D, x0, e0, dt=1):
    """


    """
    
    # Cast the position and angle to arrays
    x0 = array(x0)
    e0 = array(e0)

    # Write the initial conditions (in the lab frame) relative to the colloid
    r0 = norm(x0, 2)
    rhat = x0 / r0
    rhatp = (e0 - dot(e0, rhat) * rhat) / norm(e0 - dot(e0, rhat) * rhat)  # ZeroDivisionError
    ep = cross(rhat, e0) / norm(cross(rhat, e0))
    phi = arctan2(dot(e0, rhat), dot(e0, rhatp))
 
    h = r0 - A  # We need to check if we are inside the colloid
    if(h <= 2.0):
        wall=1
    else:
        wall=0


    # Compute the image velocity field (full approximation)
    utilde_rhat = -alpha * 3 * A * (A + h) * (1 - 3 * power(sin(phi), 2)) / (2 * power(h, 2) * power((2 * A + h), 2))
    utilde_rhatp = alpha * 3 * A**3 * (2 * A**2 + 6 * A * h + 3 * h**2) * sin(2 * phi) / (4 * h**2 * (A + h)**3 * (2 * A + h)**2)
    Omtilde = -alpha * 3 * A**3 * (2 * A**2 + 6 * A * h + 3 * h**2) * sin(2 * phi) / (4 * h**3 * (A + h)**2 * (2 * A + h)**3)

    # Compute the increment in position and angle variation
    if(wall==1):
        hdot = 0
    else:
        hdot = U * dot(e0, rhat) + utilde_rhat
   
    gdot = U * dot(e0, rhatp) + utilde_rhatp

    # Lab framework
    # xdot = hdot * rhat[0] + gdot * rhatp[0]
    # ydot = hdot * rhat[1] + gdot * rhatp[1]
    # zdot = hdot * rhat[2] + gdot * rhatp[2]

    # Go back to the lab framework
    x = hdot * rhat + gdot * rhatp
    edot = cross(e0, Omtilde * ep)
    delta = hstack((x, edot))
    
    return delta


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                 # Dipole strength  
    D = 0.01                    # Diffusion
    x0 = [-30.0, -40.0, -40.0]  # Initial position
    e0 = [1.0, 0.0, 0.0]        # Initial direction

    print F(U, A, alpha, D, x0, e0)

    F(U, A, alpha, D, x0, e0)
