 

fid = fopen('ydwt.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('udwt.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('vdwt.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);

fid = fopen('iy','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('iu','r'); im5 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('iv','r'); im6 = fread(fid, [256,inf], 'int32'); fclose(fid);

figure
imagesc(im1)
colorbar
%colormap "gray"
title 'Y subband'

figure
imagesc(im4)
colorbar
%colormap "gray"
title 'ar Y subband'

figure
imagesc(im2)
colorbar
%colormap "gray"
title 'U subband'

figure
imagesc(im5)
colorbar
%colormap "gray"
title 'ar U subband'

figure
imagesc(im3)
colorbar
%colormap "gray"
title 'V subband'

figure
imagesc(im6)
colorbar
%colormap "gray"
title 'ar V subband'

y = im4 - im1;
u = im5 - im2;
v = im6 - im3;
