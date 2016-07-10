%to load load "disp.m"
%to run disp
fid = fopen('r_dwt_zip.bin','r'); im = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('g_dwt_zip.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('b_dwt_zip.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('outimg.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('img.bin','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);
figure
imagesc(im)
title("Red subband 3 levels dwt ZipCpu")
colorbar
figure
imagesc(im1)
title("Green subband 3 levels dwt ZipCpu")
colorbar
figure
imagesc(im2)
title("Blue subband 3 levels dwt ZipCpu")
colorbar
figure
imagesc(im3)
title("Red subband 3 levels dwt RPi2B")
colorbar
figure
imagesc(im4)
title("Red subband")
colorbar
