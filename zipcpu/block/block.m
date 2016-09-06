fid = fopen('img.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('block.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('interleaveblk.bin','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('invblock.bin','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);

figure
imagesc(im1)
colorbar
%colormap "gray"
title 'orig c1 subband'
%title 'orig c2 subband'

figure
imagesc(im2)
colorbar
%colormap "gray"
%title 'c1 subband pass 1 hi-pass lo-pass w/de_interleave '
%title 'c1 subband pass 1 hi-pass lo-pass pass 2 hi-pass lo-pass '
title 'c1 subband 3 lvls pass 1 hi-pass lo-pass pass 2 hi-pass lo-pass '
%title 'c1 subband 3 lvls pass 1 lo-pass hi-pass pass 2 lo-pass hi-pass '

%figure
%hist(im2)
%colorbar

figure
imagesc(im3)
colorbar
%colormap "gray"
title 'c1 subband pass 1 hi-pass lo pass interleave'
%title 'c1 subband pass 1 lo-pass hi pass pass 2 lo-pass hi pass interleave'

figure
imagesc(im4)
colorbar
%colormap "gray"
title '       dwt c1 subband pass 1 hi-pass lo pass w/de_interleave and inv interleave pass 1 lo-pass hi pass'
%title 'inv dwt c1 subband pass 1 lo-pass hi pass pass 2 lo-pass hi pass'
