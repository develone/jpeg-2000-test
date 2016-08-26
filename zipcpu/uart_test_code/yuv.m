fid = fopen('c0.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('c0_3.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('c1.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('c1_3.bin','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('c2.bin','r'); im5 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('c2_3.bin','r'); im6 = fread(fid, [256,inf], 'int32'); fclose(fid);
 
figure
imagesc(im1)
colorbar
%colormap "gray"
title 'Y subband'

figure
imagesc(im2)
colorbar
%colormap "gray"
title 'Y subband 3 lvls fwd dwt pass 1 and 2 RPi2B'

figure
imagesc(im3)
colorbar
%colormap "gray"
title 'U subband'

figure
imagesc(im4)
colorbar
%colormap "gray"
title 'U subband 3 lvls fwd dwt pass 1 and 2 RPi2B'
figure
imagesc(im5)
colorbar
%colormap "gray"
title 'V subband'

figure
imagesc(im6)
colorbar
%colormap "gray"
title 'V subband 3 lvls fwd dwt pass 1 and 2 RPi2B'
