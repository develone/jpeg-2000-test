int ww, hh;
double memory;
int *y, *u, *v, flgyuv;
int loop, decomp, encode;
struct timeval currentTime,start,end;
 
long mtime, seconds, useconds;

double sqrt(double x);


typedef struct {
	int	m_w, m_h;
	int	*m_red, *m_green, *m_blue, *m_tmp;
	int	data[1];
} IMAGE, *IMAGEP;
