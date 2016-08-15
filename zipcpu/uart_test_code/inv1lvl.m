fid = fopen('outimg.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('interimg.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
figure
imagesc(im1)
colorbar
title "red subband 1 lvl fwd dwt "
%figure
%hist(im1)
%title "red subband 1 lvl fwd dwt"
figure
imagesc(im2)
colorbar
title "1 lvl inv de-interleave"
%figure
%hist(im2)
