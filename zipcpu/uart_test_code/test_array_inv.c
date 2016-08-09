#ifdef __ZIPCPU__
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif
void array_inv(int *xxx, int ww) {
	FILE *ptr_myfile, *ofp;
	 
	int zz[2*ww][2*ww],*zzz;
	int row,col;
    int *l_xxx;
    l_xxx = xxx;
    
	int yy[ww][ww],*yyy;
    
	//point to the 3 lvls of dwt within the image to 
	//create the yy array
	//32768 + 16384 + 8192 + 128 + 64 + 32
	if (ww==32) l_xxx = l_xxx + 57568;
	//32768 + 16384 + 128 + 64 
	if (ww==64) l_xxx = l_xxx + 49344;
	//32768  + 128 
	if (ww==128) l_xxx = l_xxx + 32896;
	//printf("0x%x\n",l_xxx);
	for (row= 0 ;row<ww;row++) {
                
                for(col=0;col< ww;col++) {
                        //printf("%d ",xxx[col]);
                        yy[row][col]=*l_xxx;
                        l_xxx++;
                        
                    //printf("%d ",yy[row][col]);
                }
                l_xxx+=256-ww;
                //printf("\n");
        }
    for (col=0;col<ww;col++){
    for (row=0;row<ww;row++){ 
		zz[row][col]=0;
	}
    }       
    yyy=&yy[0][0];
	    
	ofp = fopen("inpimg.bin","w");
	fwrite(yyy, sizeof(int), ww*ww, ofp);
	fclose(ofp);
 	  
	for (col=0;col<2*ww/2;col++){
    for (row=0;row<2*ww;row++){
		//printf("*%d %d \n",row,col);
		zz[col*2][row]=(int)yy[row][col];
		zz[col*2+1][row]=(int)yy[row][col+2*ww/2];
		//printf("*%d %d %d %d \n",row,col,zz[col*2][row],zz[col*2+1][row]);
	}
    }

    zzz = &zz[0][0];
	ofp = fopen("lnterleave.bin","w");
	fwrite(zzz, sizeof(int), 2*ww*2*ww, ofp);
	fclose(ofp);
	for (col=0;col<ww;col++){
    for (row=0;row<ww;row++){ 
		yy[row][col]=zz[row][col];
	}
    }
    
    for (col=0;col<ww;col++){
    for (row=0;row<ww;row++){ 
		zz[row][col]=0;
	}
    }     
    /*
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]
    */
    
	for (col=0;col<ww;col++) {
		for(row=1;row<ww-1;row+=2){
			printf("%d dd %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] - ((yy[row-1][col]+yy[row+1][col]+2)>>2));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
		for(row=2;row<ww;row+=2){
			printf("%d %d %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] + ((yy[row-1][col]+yy[row+1][col])>>1));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
	}
	for (col=0;col<ww;col++) {
		for(row=1;row<ww-1;row+=2){
			printf("%d %d %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] - ((yy[row-1][col]+yy[row+1][col]+2)>>2));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
		for(row=2;row<ww;row+=2){
			printf("%d %d %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] + ((yy[row-1][col]+yy[row+1][col])>>1));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
	}	
	zzz = &zz[0][0];
	
	
	/*octave
    fid = fopen('64x64idwt.bin','r'); im = fread(fid, [64,inf], 'int32'); fclose(fid);
    imagesc(im)
    */
	
	ofp = fopen("64x64idwt.bin","w");
	fwrite(zzz, sizeof(int), ww*ww, ofp);
	fclose(ofp);
	
}
