"""Computes the position increment and angular variation using the full approximation 


"""

# Import relevant commands
from numpy import array, dot, cross, arctan2, sin, cos, power, hstack, random, sqrt
from numpy.linalg import norm


def F(U, A, alpha, D, x0, e0, dt=1):
    """


    """
    
    # Cast the position and angle to arrays
    x0 = array(x0)
    e0 = array(e0)

    # Write the initial conditions (in the lab frame) relative to the colloid
    r0 = norm(x0)
    rhat = x0 / r0

    # Handle possible zero division errors
    if(norm(e0 - dot(e0, rhat) * rhat) == 0):
        rhatp = cross(random.rand(3,1),rhat) 
        rhatp = rhatp / norm(rhatp)
        ep = cross(random.rand(3,1), e0)
        ep = ep / norm(ep)
    else:
        rhatp = (e0 - dot(e0, rhat) * rhat) / norm(e0 - dot(e0, rhat) * rhat)  
        ep = cross(rhat, e0) / norm(cross(rhat, e0))         

    phi = arctan2(dot(e0, rhat), dot(e0, rhatp))



 
    h = r0 - A  # We need to check if we are inside the colloid
    if(h <= 1.0):
        wall = 1
        h = 1.0
    else:
        wall=0


    # Compute the image velocity field (full approximation)
    utilde_rhat = -alpha * 3 * A * (A + h) * (1 - 3 * power(sin(phi), 2)) / (2 * power(h, 2) * power((2 * A + h), 2))
    utilde_rhatp = alpha * 3 * A**3 * (2 * A**2 + 6 * A * h + 3 * h**2) * sin(2 * phi) / (4 * h**2 * (A + h)**3 * (2 * A + h)**2)
    Omtilde = -alpha * 3 * A**3 * (2 * A**2 + 6 * A * h + 3 * h**2) * sin(2 * phi) / (4 * h**3 * (A + h)**2 * (2 * A + h)**3)

    # Compute the increment in position and angle variation
    if(wall==1):
        hdot = max(0, U*dot(e0, rhat) + utilde_rhat)
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
    deltaD = hstack((x, edot))

    #Runs if we set a positive diffusion coefficient
    if(D):
        Dr = (2/sqrt(3))*D

        #Spatial diffusion

        # r-contribution
        if(wall):
            fBrhat = max(0, 2*D*random.randn())
        else:
            fBrhat = 2*D*random.randn()

        # rhat-contribution
        fBrhatp  = 2*D*random.randn()

        # Contribution in the remaining direction
        fBrhatp2 = 2*D*random.randn()

        rhatp2 = cross(rhat, rhatp)
        ep2    = cross(e0, ep)

        deltaBspace = fBrhat * rhat + fBrhatp * rhatp + fBrhatp2 * rhatp2

        #Rotational diffusion

        rand1 = random.rand()
        rand2 = random.randn()

        randvec = rand2 * (cos(rand1) * ep + sin(rand1) * ep2)

        deltaBrot = sqrt(2 * Dr) * randvec
        #I feel I am missing a cross product

        deltaB = hstack((deltaBspace, deltaBrot))

    else:
        deltaB = [0,0,0,0,0,0]

    #Modify later
    delta = hstack((deltaD, deltaB))

    
    return delta


if __name__ == "__main__":

    # Parameters
    U = 1                       # Velocity
    A = 20                      # Colloid size  
    alpha = 0.8                 # Dipole strength  
    D = 0.1                    # Diffusion
    x0 = [-50.0, -15.0, 0.0]  # Initial position
    e0 = [1.0, 0.0, 0.0]        # Initial direction

    print F(U, A, alpha, D, x0, e0)

    #F(U, A, alpha, D, x0, e0)

#rhat component of Brownian motion. sigma=k_b*T/6*pi*mu*a
#Remember, we made the problem dimensionless by scaling on a
    
    # if (wall)
    #     fBrhat=max([0 (2*D_s)*randn]);
    # else
    #     fBrhat=(2*D_s)*randn;
    # end
    
    # % For a spherical swimmer:    
    
    # rhatperp2 = cross(rhat,rhatperp);
    # eeperp2 = cross(ee,eeperp);
    
    # fBrhatperp=(2*D_s)*randn;
    # fBrhatperp2=(2*D_s)*randn;    
    
    # fout_B(1,1)=fBrhat*rhat(1)+fBrhatperp*rhatperp(1)+fBrhatperp2*rhatperp2(1); 
    # fout_B(2,1)=fBrhat*rhat(2)+fBrhatperp*rhatperp(2)+fBrhatperp2*rhatperp2(2);
    # fout_B(3,1)=fBrhat*rhat(3)+fBrhatperp*rhatperp(3)+fBrhatperp2*rhatperp2(3);
        
    # rand1=2*pi*rand; rand2=randn;    
    # randvec=rand2*(cos(rand1)*eeperp+sin(rand1)*eeperp2);
    
    # D_r=(2/sqrt(3))*D_s;
    # fout_B(4:6,1)=sqrt(2*D_r)*randvec; % (3/4a^2) but scaling on a so a->1

    
