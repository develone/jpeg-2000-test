fid = fopen('img.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('outimg.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('interimg.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('testimg.bin','r'); im4 = fread(fid, [128,inf], 'int32'); fclose(fid);
fid = fopen('invdwt.bin','r'); im5 = fread(fid, [256,inf], 'int32'); fclose(fid);

figure
imagesc(im1)
colorbar
%colormap "gray"
title 'red subband'

figure
imagesc(im2)
colorbar
%colormap "gray"
%title 'red subband 1 lvl de-interleave RPi2B'

figure
imagesc(im3)
colorbar
%colormap "gray"
title 'red subband 3 lvls fwd dwt pass 2 img RPi2B'

figure
imagesc(im4)
colorbar
%colormap "gray"
title 'testing extracting 128 x 128'
figure
imagesc(im5)
colorbar
%colormap "gray"
title 'red subband 1 lvls inv dwt pass 1 img RPi2B'

