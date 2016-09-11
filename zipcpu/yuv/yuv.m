clear
fid = fopen('green.bin','r'); im = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('yy.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('blue.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('red.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid); 
fid = fopen('u.bin','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid); 
fid = fopen('v.bin','r'); im5 = fread(fid, [256,inf], 'int32'); fclose(fid); 
fid = fopen('c1.bin','r'); im6 = fread(fid, [256,inf], 'int32'); fclose(fid); 
fid = fopen('c2.bin','r'); im7 = fread(fid, [256,inf], 'int32'); fclose(fid); 

fid = fopen('udwt.bin','r'); im8 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('bdwt.bin','r'); im9 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('vdwt.bin','r'); im10 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('ydwt.bin','r'); im11 = fread(fid, [256,inf], 'int32'); fclose(fid);

fid = fopen('rr.bin','r'); im12 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('gg.bin','r'); im13 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('bb.bin','r'); im14 = fread(fid, [256,inf], 'int32'); fclose(fid);
figure
imagesc(im)
colorbar
%colormap "gray"
title 'green subband'
figure
imagesc(im1)
colorbar
%colormap "gray"
title 'Y subband'

figure
imagesc(im2)
colorbar
%colormap "gray"
title 'blue subband'

figure
imagesc(im3)
colorbar
%colormap "gray"
title 'red subband'

figure
imagesc(im4)
colorbar
%colormap "gray"
title 'U subband'

figure
imagesc(im5)
colorbar
%colormap "gray"
title 'V subband'

figure
imagesc(im6)
colorbar
%colormap "gray"
title 'u subband'

figure
imagesc(im7)
colorbar
%colormap "gray"
title 'V subband'

figure
imagesc(im8)
colorbar
%colormap "gray"
title 'u dwt'

figure
imagesc(im9)
colorbar
%colormap "gray"
title 'bl dwt'

figure
imagesc(im10)
colorbar
%colormap "gray"
title 'v dwt'

figure
imagesc(im11)
colorbar
%colormap "gray"
title 'Y dwt'

figure
imagesc(im12)
colorbar
%colormap "gray"
title 'rr'

figure
imagesc(im13)
colorbar
%colormap "gray"
title 'gg'

figure
imagesc(im14)
colorbar
%colormap "gray"
title 'bb'
