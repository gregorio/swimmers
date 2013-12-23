% Program: MAIN.m
%
% Computes the trajectory of a swimming 'dipole' near a no-slip sphere.
%
% Written by S.E. Spagnolie, 2012
%

% Physical parameters:

U=1; % Free-space swimming speed
alpha=.8; % Dipole strength
A=20; % Sphere size; sphere is centered at the origin
D_s=0.01; % Spatial diffusivity constant; (sigma_s^2=2*D_s)

j1=0;
for theta0=0;
    j1=j1+1
    j2=0;
    for h0=2*A;
        j2=j2+1;

        % Initial conditions
        %theta0=0; %theta\in[0,pi]
        eta0=0*rand*2*pi; %eta\in[0,2*pi]

        X0=[0 0 21.2]; % Initial swimmer centroid position (x0,y0,z0)
        ee0=[cos(theta0) sin(theta0)*sin(eta0) sin(theta0)*cos(eta0)]; % and orientation in the lab frame

        % Time stepping parameters
        T_final=1000; % Final time (body lengths ~= U*T_final)
        T=T_final*100; % Number of timesteps
        dt=T_final/T;

        Trials=1000;


    for trial=1:Trials
trial
        clear ee x theta eta
        vars=[X0 ee0]'; % Initial state vector

        x=zeros(3,T); ee=zeros(3,T); t=zeros(1,T); h_body=zeros(1,T); phi_body=zeros(1,T);
        x(1:3,1)=X0; ee(1:3,1)=ee0; t(1)=0;
        [varsdot_D varsdot_B h phi]=xytdot(0,vars,A,U,alpha,D_s);
        phi_body(1)=phi; 
        h_body(1)=h;
  
        for timestep=1:T-1

            % Get velocity components:
            [varsdot_D varsdot_B h phi]=xytdot(0,vars,A,U,alpha,D_s);

            % Update position:
            vars=vars+dt*varsdot_D+sqrt(dt)*varsdot_B;

            t(1,timestep+1)=timestep*dt;
            x(1,timestep+1)=vars(1);
            x(2,timestep+1)=vars(2);
            x(3,timestep+1)=vars(3);

            ee(1:3,timestep+1)=vars(4:6)/norm(vars(4:6));

            h_body(timestep+1)=h; 
            phi_body(timestep+1)=phi; 

            if (1==0) % Movie!
                if (mod((timestep+1)/1000,1)==0)
                    figure(1)
                    eta=linspace(0,2*pi,50);
                    xi=linspace(0,pi,50);
                    [Eta,Xi]=meshgrid(eta,xi);
                    surf1=surf(A*cos(Eta).*sin(Xi),A*sin(Eta).*sin(Xi),A*cos(Xi));,hold on
                    plot3(x(1,1:timestep),x(2,1:timestep),x(3,1:timestep),'Color',[.8 .2 0])
                    surf2=surf(x(1,timestep+1)+1*cos(Eta).*sin(Xi),x(2,timestep+1)+1*sin(Eta).*sin(Xi),x(3,timestep+1)+1*cos(Xi));, axis equal,shading interp, grid off
                    set(surf1, 'FaceColor',[.5 .7 .7])
                    set(surf2, 'FaceColor',[.8 .2 0])      
                    xlabel('x'),ylabel('y'),zlabel('z'),title(['t = ' num2str((timestep+1)*dt)])
                    drawnow,pause(.01),hold off           
                end
            end        
 
        end %end timestepping
 
    if (1==0)
        figure(100)
        eta=linspace(0,2*pi,50);
        xi=linspace(0,pi,50);
        [Eta,Xi]=meshgrid(eta,xi);
        surf1=surf(A*cos(Eta).*sin(Xi),A*sin(Eta).*sin(Xi),A*cos(Xi));,hold on
        plot3(x(1,1:timestep),x(2,1:timestep),x(3,1:timestep),'Color',[.8 .2 0])
        surf2=surf(x(1,timestep+1)+1*cos(Eta).*sin(Xi),x(2,timestep+1)+1*sin(Eta).*sin(Xi),x(3,timestep+1)+1*cos(Xi));, axis equal,shading interp, grid off
        set(surf1, 'FaceColor',[.5 .7 .7])
        set(surf2, 'FaceColor',[.8 .2 0])      
        xlabel('x'),ylabel('y'),zlabel('z')
        drawnow
        hold on
        
        figure(101)
        plot(t,phi_body),hold on
        figure(102)
        plot(t,acos(ee(1,:))),hold on
    end

        trapped_time(trial)=dt*length(find(h_body<=1.1));
% 
%         figure(101)
%         plot(t,h_body),hold on
%         figure(102)
%         plot(t,phi_body),hold on
%         
    end % end trials

    phistar(j1,j2)=phi_body(end);
    hstar(j1,j2)=h_body(end);

    end %j2
end %j1


% Inverse Gaussian distribution:
mu=mean(trapped_time)
lambda=mu^3/var(trapped_time)
tt=linspace(1e-6,T_final,400);
invG=sqrt(lambda./(2*pi*tt.^3)).*exp(-lambda*(tt-mu).^2./(2*mu^2*tt));
