A = [3 4; 5 6];
[m,n] = size(A);
disp(n);
for j=1:n
  v = A(:,j);
  for i=1:j-1
    R(i,j) = Q(:,i)'*A(:,j);
    v=v-R(i,j)*Q(:,i);
  end
  R(j,j) = norm(v);
  Q(:,j) = v/R(j,j);
end
