A = [1, 1;
     16, 8;
     9000, 5000];
b = [44, 512, 300000]';
basis = [1];
c = [-30000, -20000]';
[x,y,cost] = simplex(A,b,c,basis);
x
y
cost
