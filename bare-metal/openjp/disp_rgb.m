fid = fopen('red-out.32t','r'); im1 = fread(fid, [1024,inf], 'char'); fclose(fid);
figure; imagesc(im1); colorbar; colormap 'gray';title"red sub band 1024 x 1924 RPi bare-metal ultibo "

fid = fopen('grn-out.32t','r'); im2 = fread(fid, [1024,inf], 'char'); fclose(fid);
figure; imagesc(im2); colorbar; colormap 'gray';title"green sub band 1024 x 1924 RPi bare-metal ultibo "

fid = fopen('blu-out.32t','r'); im3 = fread(fid, [1024,inf], 'char'); fclose(fid);
figure; imagesc(im3); colorbar; colormap 'gray';title"blue sub band 1024 x 1924 RPi bare-metal ultibo "

fid = fopen('dwt-out.32t','r'); im4 = fread(fid, [1024,inf], 'int32'); fclose(fid);
figure; imagesc(im4); colorbar; colormap 'gray';title" 1024 x 1924 n = 5 lvls numresolution 4 RPi bare-metal ultibo "
