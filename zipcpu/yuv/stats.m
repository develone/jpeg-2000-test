[x,y] = histc(im8,unique(im8));
figure
plot(x)
title('u hist')

figure
plot(y)
title('u unique')

[x,y] = histc(im9,unique(im9));
figure
plot(x)
title('blue hist')
figure
plot(y)
title('blue unique')

[x,y] = histc(im10,unique(im10));
figure
plot(x)
title('v hist')

figure
plot(y)
title('v unique')

[x,y] = histc(im11,unique(im11));
figure
plot(x)
title('red hist')
figure
plot(y)
title('red unique')
