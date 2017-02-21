int ww, hh;
double memory;
int *y, *u, *v, flgyuv;
int loop, decomp, encode;
struct timeval currentTime,start,end;
 
long mtime, seconds, useconds;

double sqrt(double x);
void yuv(int w,int *r,int *g,int *b,int *u,int *v,int *y);
void invyuv(int w,int *r,int *g,int *b,int *u,int *v,int *y);
void lift_config(int dec, int enc, int mct, int bp, long imgsz,int *bufferptr);

typedef struct {
	int	m_w, m_h;
	int	*m_red, *m_green, *m_blue, *m_tmp;
	int	data[1];
} IMAGE, *IMAGEP;
