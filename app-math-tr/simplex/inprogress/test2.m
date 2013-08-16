A = [1 1 2;
     1 1 4];
b = [4;4];
basis = [3];
c = [5 1 8]';
[x,y,cost] = simplex(A,b,c,basis);
x
y
cost
