x=165
y=95
win=50

im1 = imread('flow1-bw-0.png');
im2 = imread('dleft.png');
%im2 = imread('upright.png');
%im2 = imread('flow2-bw-0.png');
[u, v] = lk(im1, im2, x, y, win);
imshow(im1) ;
hold on;
plot(x,y,'+r');
plot(x+u*3,y+v*3,'og');
