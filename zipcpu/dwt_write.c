 
void dwt_write(int *a, int c, int r, int v) {
	int *b;
	b = a;
	*(a+c+r*256) = v;
 
}
