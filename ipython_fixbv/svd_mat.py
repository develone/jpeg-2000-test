"""This example is based on work at
http://www.mathworks.com/help/matlab/ref/svd.html"""
import numpy  as np
a = np.array([[1,2],[3,4],[5,6],[7,8]])
U, s, V = np.linalg.svd(a, full_matrices=True)
print "a"
print a
print "s"
print s
print "U"
print U
print "V"
print V

"""http://www.math.nyu.edu/~neylon/linalgfall04/project1/dj/reqofmatrixmult.htm
In order to multiply two matrices, A and B, the number of columns in A
 must equal the number of rows in B. Thus, if A is an m x n matrix and B
 is an r x s matrix, n = r."""
#Reconstruction based on full SVD:
S = np.zeros((4, 2), dtype=float)
print S
#print np.diag(s)
S[:2, :2] = np.diag(s)
print S
np.allclose(a, np.dot(U, np.dot(S, V)))
print a
