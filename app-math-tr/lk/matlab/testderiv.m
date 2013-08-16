im1 = imread('flow1-bw-0.png');
im2 = imread('flow2-bw-0.png');
[fx, fy, ft] = deriv(im1, im2);
