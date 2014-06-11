#include <stdio.h>

#include <math.h>

#include "Image2.h"

#define ROW 128

#define COL 128

 

int Adr[128][128];

int Input[128][128];

int Ad[128][128];

int Even[128][64];

int Odd[128][64];

int High[128][64];

int Low[128][64];

int LEven[64][64];

int HEven[64][64];

int LOdd[64][64];

int HOdd[64][64];

int LH[64][64],LL[64][64],HH[64][64],HL[64][64];

int waveencodeImage[128][128];

int rowS=128;

int colS=128;

int rowL=128;

int colL=128;

int RLL[128][128];

int RHL[128][128];

int RHH[128][128];

int RLH[128][128];

int RL[ROW][COL];

int RH[ROW][COL];

int R[ROW][COL];

int H[ROW][COL];

int Output[ROW][ROW];

 

int aa,cc;

 

void integerdwt();

void reversedwt();

 

void integerdwt()

 

{

 

int i,j,k,a;

 

                                    for (j=0;j<128;j++)

                                    {

                                                a=1;

                                       for (k=0;k<64;k++)

                                       {

                                                            Even[j][k]=Input[j][a];

                                                            a=a+2;

                                       }

                                    }

 

            //////// one dimensional Odd component////////

 

 

                                    for (j=0;j<128;j++)

                                    {

                                                a=0;

                                       for (k=0;k<64;k++)

                                       {

                                                            Odd[j][k]=Input[j][a];

                                                            a=a+2;

                                       }

                                    }

 

 

            ////////////  comput L  AND  H pass component

                                    for (j=0;j<128;j++)

                                    {

                                       for (k=0;k<64;k++)

                                       {

                                                  

                                                 High[j][k]=Odd[j][k]-Even[j][k];

                                                 aa=Odd[j][k]-Even[j][k];

                                                 aa=aa/2;

                                                 cc=ceil(aa);

                                                 Low[j][k]=(Even[j][k]+cc);

                                       }

                                    }

 

            ///////////////////one dimensional L even

   

                                    for (j=0;j<64;j++)

                                    {

                                                a=1;

                                       for (k=0;k<64;k++)

                                       {

                                                            LEven[k][j]=Low[a][j];

                                                            HEven[k][j]=High[a][j];

 

                                                            a=a+2;

                                       }

                                    }

////////////////////////////////////////////////////////////////

           

 

            //////// one dimensional  L Odd component////////

 

                                    for (j=0;j<64;j++)

                                    {

                                                a=0;

                                       for (k=0;k<64;k++)

                                       {       

                                                            LOdd[k][j]=Low[a][j];

                                                            HOdd[k][j]=High[a][j];

 

                                                            a=a+2;

                                       }

                                    }

 

                                    for (j=0;j<64;j++)

                                    {

                                       for (k=0;k<64;k++)

                                       {

 

                                                 LH[j][k]=LOdd[j][k]-LEven[j][k];

                                                 aa=LOdd[j][k]-LEven[j][k];

                                                 aa=aa/2;

                                                 cc=ceil(aa);

                                                 LL[j][k]=(LEven[j][k]+cc);

                                                 HH[j][k]=HOdd[j][k]-HEven[j][k];

                                                 aa=HOdd[j][k]-HEven[j][k];

                                                 aa=aa/2;

                                                 cc=ceil(aa);

                                                 HL[j][k]=(HEven[j][k]+cc);

                                       }

                                    }

 

 

}

void reversedwt()

{//begin of reverse dwt

 

int i,j,k,a;

int columns1=128;

int Lenr =128;

int Lenc =128;

int rlen2r=128;

int valc;

 

/////init the RL RH arrays (4x2)

 

for(i=0;i<ROW;i++){

            for(j=0;j<COL;j++){

            RL[i][j]=0;

            RH[i][j]=0;

            }

}

 

            for (j=0;j<columns1;j++)

                                    {

                                       for (k=0;k<columns1;k++)

                                       {

 

                                                 aa=LH[j][k];

                                                 aa=aa/2;

                                                 cc=ceil(aa);

 

                                                 RLL[j][k]=(LL[j][k]-cc);

 

                                                 RLH[j][k]=RLL[j][k]+LH[j][k];

 

           

                                                 aa=HH[j][k];

                                                 aa=aa/2;

                                                 cc=ceil(aa);

 

 

                                                 RHL[j][k]=(HL[j][k]-cc);

 

                                                 RHH[j][k]=HH[j][k]+RHL[j][k];

 

                                       }

                                    }

 

                                                            k=0;

                                                            for(i=1;i<ROW;i=i+2){

                                                                        for(j=0;j<COL;j++){

                                                                                    RL[i][j]=RLL[k][j];

                                                                                    RH[i][j]=RHL[k][j];

                                                                                   

                                                                        }

                                                                        k++;

                                                            }

 

 

                                                                        k=0;

                                                            for(i=0;i<ROW;i=i+2){

                                                                        for(j=0;j<COL;j++){

                                                                                    RL[i][j]=RLH[k][j];

                                                                                    RH[i][j]=RHH[k][j];

                                                                                   

                                                                        }

                                                                        k++;

                                                            }

 

 

                                                            for(i=0;i<ROW;i=i+1)

                                                                        {

                                                                        for(j=0;j<COL;j++)

                                                                        {

                                                                                    aa=RH[i][j]/2;

                                                                                    cc=ceil(aa);

                                                                                    R[i][j]=RL[i][j]-cc;

                                                                                    H[i][j]=R[i][j]+RH[i][j];

 

                                                           

                                                                        }

                                                                       

                                                            }

                                   

                                                            for(i=0;i<ROW;i++){

                                                                                    k=0;

                                                                        for(j=1;j<ROW;j=j+2){

                                                                                    Output[i][j]=R[i][k];

                                                                                    k++;

                                                                                   

                                                                        }

                                                                       

                                                            }

                                   

                                                            for(i=0;i<ROW;i++){

                                                                                    k=0;

                                                                        for(j=0;j<ROW;j=j+2){

                                                                                    Output[i][j]=H[i][k];

                                                                                    k++;                                                                           

                                                                        }

                                                                       

                                                            }

}// end of reverse dwt

 

int main()

 

{

int i,j;

for( i=0;i<128;i++)

                                                            {

                                                                        for( j=0;j<128;j++)

                                                            {

                                                           

                                                            Input[i][j]=InputImage[i][j];

                                                            //                     xil_printf("%d\n",Input[i][j]);                                                       

 

                                                            }

                                                            }

integerdwt();

            for(i=0;i<128;i++){

                                                                                    for(j=0;j<128;j++)

                                                                                    {

 

                                                                                                if(i<64){

                                                                                                            if(j<64){

                                                                                                                        waveencodeImage[i][j]=LL[i][j];

                                                                                                            }

                                                                                                            else{

                                                                                                                        waveencodeImage[i][j]=LH[i][j-64];

                                                                                                            }

                                                                                                }

                                                                                                else{

                                                                                                            if(j<64){

                                                                                                                        waveencodeImage[i][j]=HL[i-64][j];

                                                                                                            }

                                                                                                            else{

                                                                                                                        waveencodeImage[i][j]=HH[i-64][j-64];

                                                                                                            }

                                                           

                                                                                                }

                                               //xil_printf(" %d\n",waveencodeImage[i][j]);

                                                                                    }

                                                                                    //xil_printf("\n");

                                                                        }

 

for( i=0;i<128;i++)

                                                                                                                        {

                                                                                        for( j=0;j<128;j++)

                                                                                                                        {                                                                                                                                              

                                                                                                                                    Ad[i][j]=waveencodeImage[i][j];

                                                                                                                                    //xil_printf(" %d\n",Ad[i][j]);

                                                                                                                        }

                                                                                                                       

                                                                                                                        }

reversedwt();                     

                                                                                    for(i=0;i<rowL;i++){

                                                                                    for(j=0;j<colL;j++){

                                                           

                                                                                                if(i<rowS){

                                                                                                            if(j<colS){

                                                                                                                        RLL[i][j]=Adr[i][j];

                                                                                                            }

                                                                                                            else{

                                                                                                                        RLH[i][j-colS]=Adr[i][j];

                                                                                                            }

                                                                                                }

                                                                                                else{

                                                                                                            if(j<colS){

                                                                          RHL[i-rowS][j]=Adr[i][j];

                                                                                                            }

                                                                                                            else{

                                                                                 RHH[i-rowS][j-colS]=Adr[i][j];

                                                                                                            }

                                                           

                                                                                                }

                                                                                                //xil_printf(" %d  ",all[i][j]);

                                                                                    }

                                                                                    //xil_printf("\n");

                                                                        }                                                          

                                                           

            //xil_printf("matrix Output: \n");

                                                            for( i=0;i<128;i++)

 

 

                                                            {

                                                                        for( j=0;j<128;j++)

                                                            {

                                                                                    xil_printf("%d\n",Output[i][j]);

                                                                        //wavedecode[i][j]=Output[i][j];

                                                            }

                                                           

                                                            }

                                                //         xil_printf("exit\n");

                                                            return 0;

//end of main loop

}

 
- See more at: https://www.pantechsolutions.net/spartan-3-edk-sourcecode/implementation-of-lifting-dwt-technique#sthash.7gNYbjQy.dpuf
