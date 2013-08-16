n = 4;
e = ones(n,1);
K = spdiags([-e, 2*e, -e], -1:1, n, n);
disp(full(K))
