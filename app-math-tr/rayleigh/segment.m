#dim = 16;
I = double(imread("twoObj.jpg"));
dim = 30
#I = rand( dim, dim );
% generate a random image
I( 1:dim/2,:) = I( 1:dim/2,:) + 1; % brighten the top half
[X,Y] = meshgrid( [1:dim]/dim-0.5, [1:dim]/dim-0.5 );
I = I(:); X = X(:);Y = Y(:);
N = length(I); % number of pixels
W = zeros( N );
sigD = 0.1; % variance for distance
sigI = 0.1; % variance for intensity
for k = 1 : N
dist = sqrt( (X(k)-X).^2 + (Y(k)-Y).^2 );
W(:,k) = exp( -((I(k)-I).^2)/sigI ) .* exp( -(dist.^2)/sigD );
end
subplot(121); imagesc( reshape(I,dim,dim) ); axis image; % original image

%%% CLUSTER
d = sum(W);D1 = diag(d);D2 = diag(1./sqrt(d));
[vv, dd] = eig(D2 * (D1-W) * D2);
v2 = vv(:,2) > 0;
cc = sum(vect(W(v2==0,v2==1)))/sum(d(v2==0)) +sum(vect(W(v2==1,v2==0)))/sum(d(v2==1));
v2 = reshape( v2, dim, dim ); % 2 clusters by a 6 binary matrix
subplot(122); imagesc( v2 ); axis image; title( cc ); % segmentation result
colormap gray;
