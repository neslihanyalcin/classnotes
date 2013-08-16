function [u, v] = lk(im1, im2, i, j, windowSize);

  [fx, fy, ft] = deriv(im1, im2);
  
  halfWindow = floor(windowSize/2);
  curFx = fx(i-halfWindow:i+halfWindow, j-halfWindow:j+halfWindow);
  curFy = fy(i-halfWindow:i+halfWindow, j-halfWindow:j+halfWindow);
  curFt = ft(i-halfWindow:i+halfWindow, j-halfWindow:j+halfWindow);

  curFx = curFx';
  curFy = curFy';
  curFt = curFt';

  curFx = curFx(:);
  curFy = curFy(:);
  curFt = -curFt(:);

  A = [curFx curFy];

  U = pinv(A'*A)*A'*curFt;
  disp(U)
    
  u = U(1)
  v = U(2)

