"""This example is based on work at
http://www.mathworks.com/help/matlab/ref/svd.html"""
import numpy  as np
a = np.array([[3,1],[1,3]])
U, s, V = np.linalg.svd(a, full_matrices=True)
print "a"
print a
print "s"
print s
print "U"
print U
print "V"
print V

 
