fid = fopen('img.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('outimg.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
%fid = fopen('imgdwt.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('imgdwt1.bin','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('imgdwt2.bin','r'); im5 = fread(fid, [256,inf], 'int32'); fclose(fid);

figure
imagesc(im1)
colorbar
%colormap "gray"
title 'red subband'

%figure
%imagesc(im3)
%colorbar
%colormap "gray"
%title 'red subband 1 lvl fwd dwt pass 1 alt RPi2B'

figure
imagesc(im2)
colorbar
%colormap "gray"
title 'red subband 3 lvls fwd dwt pass 2 img RPi2B'

figure
imagesc(im4)
colorbar
%colormap "gray"
title 'red subband 3 lvls inv dwt pass 1 alt RPi2B'
figure
imagesc(im5)
colorbar
%colormap "gray"
title 'red subband 3 lvls inv dwt pass 2 img RPi2B'

