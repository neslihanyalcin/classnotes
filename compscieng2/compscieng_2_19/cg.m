A = [6 1 1; 1 7 1; 1 1 8];
b = [1;1;1]           
disp(A\b);

d = b;                             % initial search direction
r = b;                             % initial residual
x = b*0;                           % initial solution
r2 = r'*r;
disp('CG solution');
for i = 1:10
   Ad = A*d;                       % apply the matrix A
   alpha = r2/(d'*Ad);             % a first scalar product
   x = x+alpha*d;                  % update solution
   r = r-alpha*Ad;                 % update residual
   r2old = r2;
   r2 = r'*r;                      % a second scalar product
   beta = r2/r2old;               
   d = r+beta*d;                   % new search direction
   disp(x);
   disp("\n");
end

