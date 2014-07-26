import numpy  as np
a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
print 'a '
print a

#Reconstruction based on full SVD:
U, s, V = np.linalg.svd(a, full_matrices=True)
U.shape, V.shape, s.shape
print 'U '
print U
print 's '
print s
print 'V '
print V

S = np.zeros((9, 6), dtype=complex)
S[:6, :6] = np.diag(s)
np.allclose(a, np.dot(U, np.dot(S, V)))
print 'a '
print a
#Reconstruction based on reduced SVD:

U, s, V = np.linalg.svd(a, full_matrices=False)
U.shape, V.shape, s.shape

S = np.diag(s)
np.allclose(a, np.dot(U, np.dot(S, V)))
