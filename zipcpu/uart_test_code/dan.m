fid = fopen('red-out.32t','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('grn-out.32t','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
fid = fopen('blu-out.32t','r'); im3 = fread(fid, [256,inf], 'int32'); fclose(fid);

figure
imagesc(im1)

figure
imagesc(im2)

figure
imagesc(im3)
