fid = fopen('img.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('outimg.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('imgdwt.bin','r'); im3 = fread(fid, [128,inf], 'int32'); fclose(fid);
fid = fopen('imgdwt1.bin','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);
figure
imagesc(im1)
colorbar
title 'red subband'
figure
imagesc(im2)
colorbar
title 'red subband 1 lvl dwt RPi2B'
figure
imagesc(im3)
colorbar
title 'red subband 1 lvl dwt RPi2B'

figure
imagesc(im4)
colorbar
title 'red subband inv dwt RPi2B'

