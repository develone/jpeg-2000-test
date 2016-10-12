 

 

fid = fopen('uydwt.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('uudwt.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('uvdwt.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);

 

figure
imagesc(im1)
colorbar
%colormap "gray"
title 'Y subband'

 

figure
imagesc(im2)
colorbar
%colormap "gray"
title 'U subband'

 

figure
imagesc(im3)
colorbar
%colormap "gray"
title 'V subband'

ymin = min(im1);
ymax = max(im1);
yymin = min(ymin)
yymax = max(ymax)

umin = min(im2);
umax = max(im2);
uumin = min(umin)
uumax = max(umax)

vmin = min(im3);
vmax = max(im3);
vvmin = min(vmin)
vvmax = max(vmax)
