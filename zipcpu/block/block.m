fid = fopen('img.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('block.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
%fid = fopen('invblock.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);

figure
imagesc(im1)
colorbar
%colormap "gray"
title 'orig c2 subband'

figure
imagesc(im2)
colorbar
%colormap "gray"
title 'c2 subband pass 1 hi-pass lo-pass pass 2 hi-pass lo-pass '
%title 'c2 subband pass 1 hi-pass lo-pass'

%figure
%hist(im2)
%colorbar

%figure
%imagesc(im3)
%colorbar
%colormap "gray"
%title 'rebuilt c1 subband lo-pass hi pass'
