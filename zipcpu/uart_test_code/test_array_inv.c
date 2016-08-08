#ifdef __ZIPCPU__
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif
void array_inv(int *xxx) {
	FILE *ptr_myfile, *ofp;
	 
	int zz[64][64],*zzz;
	int row,col;
    int *l_xxx;
    l_xxx = xxx;
    
	int yy[32][32],*yyy;
    
	printf("in test_array 0x%x 0x%x\n",xxx,l_xxx);
	l_xxx = l_xxx + 57568;
	printf("0x%x\n",l_xxx);
	for (row= 0 ;row<32;row++) {
                
                for(col=0;col< 32;col++) {
                        //printf("%d ",xxx[col]);
                        yy[row][col]=*l_xxx;
                        l_xxx++;
                        
                    printf("%d ",yy[row][col]);
                }
                l_xxx+=256-32;
                printf("\n");
        }
    for (col=0;col<64;col++){
    for (row=0;row<64;row++){ 
		zz[row][col]=0;
	}
    }       
    yyy=&yy[0][0];
	    
	ofp = fopen("32x32dwt.bin","w");
	fwrite(yyy, sizeof(int), 1024, ofp);
	fclose(ofp);
 	  
	for (col=0;col<32/2;col++){
    for (row=0;row<32;row++){
		printf("*%d %d \n",row,col);
		zz[col*2][row]=(int)yy[row][col];
		zz[col*2+1][row]=(int)yy[row][col+32/2];
		printf("*%d %d %d %d \n",row,col,zz[col*2][row],zz[col*2+1][row]);
	}
    }

    zzz = &zz[0][0];
	ofp = fopen("64x64inter.bin","w");
	fwrite(zzz, sizeof(int), 4096, ofp);
	fclose(ofp);
	for (col=0;col<32;col++){
    for (row=0;row<32;row++){ 
		yy[row][col]=zz[row][col];
	}
    }
    
    for (col=0;col<64;col++){
    for (row=0;row<64;row++){ 
		zz[row][col]=0;
	}
    }     
    /*
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]
    */
    
	for (col=0;col<32;col++) {
		for(row=1;row<32-1;row+=2){
			printf("%d %d %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] - ((yy[row-1][col]+yy[row+1][col]+2)>>2));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
		for(row=2;row<32;row+=2){
			printf("%d %d %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] + ((yy[row-1][col]+yy[row+1][col])>>1));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
	}
	for (col=0;col<32;col++) {
		for(row=1;row<32-1;row+=2){
			printf("%d %d %d \n",row,col,yy[row][col]);
			zz[col][row] = (yy[row][col] - ((yy[row-1][col]+yy[row+1][col]+2)>>2));
			yy[row][col] = zz[col][row];
			printf("%d %d %d \n",zz[row][col],yy[row-1][col],yy[row-1][col]);
		}
		for(row=2;row<32;row+=2){
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
	fwrite(zzz, sizeof(int), 4096, ofp);
	fclose(ofp);
	
}
