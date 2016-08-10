fid = fopen('inpimg.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
figure
imagesc(im1)
colorbar
title "1 lvl fwd dwt w/de-interleave"
