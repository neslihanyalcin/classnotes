close all
clear all
clc

% read the input image
inpImage =imread('twoObj.bmp');
% size of image
[rows cols dims] = size(inpImage);

if dims==3
    inpImage=double(rgb2gray(inpImage));
else
    inpImage=double(inpImage);
end

% Gaussian filter parameter
sigma=1.2;
% Gaussian filter
G=fspecial('gaussian',15,sigma);
% Gaussian smoothed image
inpImage=conv2(inpImage,G,'same');

% gradient of image
[gradIX,gradIY]=gradient(inpImage);
absGradI=sqrt(gradIX.^2+gradIY.^2);

% higher dimensional embedding function phi whose zero level set is our
% contour
% radius of circle - initial embedding function
% radius=min(floor(0.45*rows),floor(0.45*cols));
[u,v] = meshgrid(1:cols, 1:rows);
phi = ((u-cols/2)/(floor(0.45*cols))).^2+((v-rows/2)/(floor(0.45*rows))).^2-1;

% edge-stopping function
g = 1./(1+absGradI.^2);
% gradient of edge-stopping function
[gx,gy]=gradient(g);

% gradient descent step size
dt=.4;

% number of iterations after which we reinitialize the surface
num_reinit=10;

phiOld=zeros(rows,cols);

% number of iterations
iter=0;

while(sum(sum(abs(phi-phiOld)))~=0)
    % gradient of phi
    [gradPhiX gradPhiY]=gradient(phi);
    % magnitude of gradient of phi
    absGradPhi=sqrt(gradPhiX.^2+gradPhiY.^2);
    % normalized gradient of phi - eliminating singularities
    normGradPhiX=gradPhiX./(absGradPhi+(absGradPhi==0));
    normGradPhiY=gradPhiY./(absGradPhi+(absGradPhi==0));

    [divXnormGradPhiX divYnormGradPhiX]=gradient(normGradPhiX);
    [divXnormGradPhiY divYnormGradPhiY]=gradient(normGradPhiY);
    % curvature is the divergence of normalized gradient of phi
    K = divXnormGradPhiX + divYnormGradPhiY;
    % dPhiBydT
    dPhiBydT =( g.*K.*absGradPhi + g.*absGradPhi + (gx.*gradPhiX+gy.*gradPhiY) );
    phiOld=phi;
    % level set evolution equation
    phi = phi + ( dt * dPhiBydT );
    iter=iter+1;
    if mod(iter,num_reinit)==0
        % reinitialize the embedding function after num_reinit iterations
        phi=sign(phi);
        phi = double((phi > 0).*(bwdist(phi < 0)) - (phi < 0).*(bwdist(phi > 0)));
    end
    if mod(iter,10)==0
        pause(0.05)
        iter
        imagesc(inpImage)
        colormap(gray)
        hold on
        contour(phi,[0 0],'r')
        %         close all
        %         surf(phi)
        %         pause
    end
end