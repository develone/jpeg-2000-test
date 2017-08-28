fid = fopen('red','r'); im4 = fread(fid, [256,inf], 'char'); fclose(fid);
figure; imagesc(im4);colorbar; colormap 'gray';
title 'RED DECOMPRESSED 256 x 256 bare metal';
fid = fopen('green','r'); im5 = fread(fid, [256,inf], 'char'); fclose(fid);
figure; imagesc(im5);colorbar; colormap 'gray';
title 'GREEN DECOMPRESSED 256 x 256 bare metal';
fid = fopen('blue','r'); im6 = fread(fid, [256,inf], 'char'); fclose(fid);
figure; imagesc(im6);colorbar; colormap 'gray';
title 'BLUE DECOMPRESSED 256 x 256 bare metal';
