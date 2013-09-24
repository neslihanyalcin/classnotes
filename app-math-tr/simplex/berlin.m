% octave

A = [1, 1;
     16, 8;
     9000, 5000];
b = [44, 512, 300000]';
c = [30000, 20000]';
lb = [0, 0]';
ub = [];
ctype = "UUU";
vartype = "CC";
s = -1;
param.msglev = 1;
param.itlim = 100;
[xmin, fmin, status, extra] = glpk (c, A, b, lb, ub, ctype, vartype, s, param);
xmin
fmin
