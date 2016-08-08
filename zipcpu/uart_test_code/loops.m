fid = fopen("32x32dwt.bin","r"); im1 = fread(fid, [32,inf], 'int32'); fclose(fid);
fid = fopen("64x64inter.bin","r"); im2 = fread(fid, [64,inf], 'int32'); fclose(fid);
fid = fopen("64x64idwt.bin","r"); im3 = fread(fid, [64,inf], 'int32'); fclose(fid);  
figure
imagesc(im1)
colorbar
figure
imagesc(im2)
colorbar
figure
imagesc(im3)
colorbar
