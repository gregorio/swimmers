function [fout_D fout_B h phi] = xytdot(t,xin,A,U,alpha,D_s)

%Output: 
% fout_D: deterministic contribution to the translational velocities
% fout_R: Rotation matrix
% fout_B: Brownian contribution
% h: distance between the swimmer centroid and the sphere surface
% phi: the angle in the rhat, rhatperp frame (see Fig. 2 in the paper)


% Input state: 
    x0(1:3,1)=xin(1:3);
    ee(1:3,1)=xin(4:6); % (theta,eta) are the body angles in the lab frame
    
% Convert coordinate system to (rhat,rhatperp,phi) as in paper:
    r=norm(x0);  
    rhat = x0/r;
    if (norm(ee-dot(rhat,ee)*rhat)==0)
        rhatperp=cross(rand(3,1),rhat);rhatperp=rhatperp/norm(rhatperp); % just get one
        eeperp=cross(rand(3,1),ee);eeperp=eeperp/norm(eeperp); % just get one
    else
        rhatperp=(ee-dot(rhat,ee)*rhat)/norm(ee-dot(rhat,ee)*rhat);        
        eeperp=cross(rhat,ee)/norm(cross(rhat,ee));
    end
    phi = atan2(dot(ee,rhat),dot(ee,rhatperp)); % body angle relative to the colloid frame ("theta" in the paper)     
         
    
% Are we "on" the wall?
 
    h=r-A;
    if (h<=1) 
        h=1; 
        wall=1;
    else
        wall=0;  
    end 
    
% Far-field hydrodynamic effect of the no-slip boundary condition:

%"Full approximation"

    utilde_rhat = -alpha*3*A*(A+h)*(1-3*sin(phi)^2)/(2*h^2*(2*A+h)^2); 
    utilde_rhatperp = alpha*3*A^3*(2*A^2+6*A*h+3*h^2)*sin(2*phi)/(4*h^2*(A+h)^3*(2*A+h)^2);
    Omtilde=-alpha*3*A^3*(2*A^2+6*A*h+3*h^2)*sin(2*phi)/(4*h^3*(A+h)^2*(2*A+h)^3);

% Simple approximation
%     utilde_rhat = -3*alpha*(1-h^2/(4*A^2))*(1-3*sin(phi)^2)/(8*h^2); 
%     utilde_rhatperp = 3*alpha*(1-h/A-3*h^2/(4*A^2))*sin(2*phi)/(8*h^2);
%     Omtilde=-3*alpha*sin(2*phi)/(16*h^3)*(1-h/(2*A)-3*h^2/(2*A^2));

    
% If there is a wall, don't allow for motion through the boundary:    
    if (wall) 
        hdot=max([0 U*dot(ee,rhat)+utilde_rhat]);
    else
        hdot=U*dot(ee,rhat)+utilde_rhat;
    end
    
% Perpendicular component of velocity (no such constraints)
    gdot=U*dot(ee,rhatperp)+utilde_rhatperp;
    
% Converted back to (x,y,z,theta,eta) coordinate system:    
    xdot = hdot*rhat(1)+gdot*rhatperp(1);
    ydot = hdot*rhat(2)+gdot*rhatperp(2);
    zdot = hdot*rhat(3)+gdot*rhatperp(3);
    eedot = cross(ee,Omtilde*eeperp);
     
% Deterministic contribution    
    fout_D(1,1)=xdot; 
    fout_D(2,1)=ydot;
    fout_D(3,1)=zdot; 
    fout_D(4:6,1)=eedot;

% Brownian contribution    
    
% rhat component of Brownian motion. sigma=k_b*T/6*pi*mu*a
% Remember, we made the problem dimensionless by scaling on a
    
    if (wall)
        fBrhat=max([0 (2*D_s)*randn]);
    else
        fBrhat=(2*D_s)*randn;
    end
    
    % For a spherical swimmer:    
    
    rhatperp2 = cross(rhat,rhatperp);
    eeperp2 = cross(ee,eeperp);
    
    fBrhatperp=(2*D_s)*randn;
    fBrhatperp2=(2*D_s)*randn;    
    
    fout_B(1,1)=fBrhat*rhat(1)+fBrhatperp*rhatperp(1)+fBrhatperp2*rhatperp2(1); 
    fout_B(2,1)=fBrhat*rhat(2)+fBrhatperp*rhatperp(2)+fBrhatperp2*rhatperp2(2);
    fout_B(3,1)=fBrhat*rhat(3)+fBrhatperp*rhatperp(3)+fBrhatperp2*rhatperp2(3);
        
    rand1=2*pi*rand; rand2=randn;    
    randvec=rand2*(cos(rand1)*eeperp+sin(rand1)*eeperp2);
    
    D_r=(2/sqrt(3))*D_s;
    fout_B(4:6,1)=sqrt(2*D_r)*randvec; % (3/4a^2) but scaling on a so a->1
        
     
return
