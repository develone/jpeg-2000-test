fid = fopen('red','r'); im1 = fread(fid, [2048,inf], 'char'); fclose(fid);
figure; imagesc(im1);colorbar;
title 'RED DECOMPRESSED 2048 x 2048';
fid = fopen('green','r'); im2 = fread(fid, [2048,inf], 'char'); fclose(fid);
figure; imagesc(im2);colorbar
title 'GREEN DECOMPRESSED 2048 x 2048';
fid = fopen('blue','r'); im3 = fread(fid, [2048,inf], 'char'); fclose(fid);
figure; imagesc(im3);colorbar
title 'BLUE DECOMPRESSED 2048 x 2048';
