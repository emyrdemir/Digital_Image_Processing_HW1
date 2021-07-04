%pkg load image
I = imread('sherlock.jpg');
subplot(221);
imshow(I);
title('RGB');

subplot(222);
I2=rgb2gray(I);
imshow(I2);
title('Grayscale');

subplot(223);
I3 = imbinarize(I2);
%I3 = im2bw(I2);
imshow(I3);
title('Binary');
 
subplot(224);
imhist(I2);
title('Histogram');