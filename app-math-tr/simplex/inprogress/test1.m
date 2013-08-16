A = [1 1 2];
b = [4];
basis = [3];
c = [5 3 8]';
[x,y,cost] = simplex(A,b,c,basis)
