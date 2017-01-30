int sam, lf, rh, dwt;
int fwd;
struct timeval currentTime;
long start_sec;
long end_sec;
int i;
int lift(int sam, int lf, int rh, int fwd);
void delay(int dd);
typedef struct {
	int	m_w, m_h;
	int	*m_red, *m_green, *m_blue;
	int	data[1];
} IMAGE, *IMAGEP;
