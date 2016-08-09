fid = fopen("inpimg.bin","r"); im1 = fread(fid, [32,inf], 'int32'); fclose(fid);
fid = fopen("lnterleave.bin","r"); im2 = fread(fid, [64,inf], 'int32'); fclose(fid);
  
figure
imagesc(im1)
colorbar
figure
imagesc(im2)
colorbar
