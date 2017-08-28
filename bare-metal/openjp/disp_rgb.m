fid = fopen('red-out.32t','r'); im1 = fread(fid, [256,inf], 'char'); fclose(fid);
figure; imagesc(im1); colorbar; colormap 'gray';
 
title"RED SUB BAND INPUT 256 x 256 RPi BARE-METAL ULTIBO"
fid = fopen('grn-out.32t','r'); im2 = fread(fid, [256,inf], 'char'); fclose(fid);
figure; imagesc(im2); colorbar; colormap 'gray';
 
title"GREEN SUB BAND INPUT 256 x 256 RPi BARE-METAL ULTIBO"
fid = fopen('blu-out.32t','r'); im3 = fread(fid, [256,inf], 'char'); fclose(fid);
figure; imagesc(im3); colorbar; colormap 'gray';
 
title"BLUE SUB BAND INPUT 256 x 256 RPi BARE-METAL ULTIBO"
%fid = fopen('dwt-out.32t','r'); im4 = fread(fid, [256,inf], 'int32'); fclose(fid);
%figure; imagesc(im4); colorbar; colormap 'gray';title" 256 x 256 n = 5 lvls numresolution 4 RPi bare-metal ultibo "
