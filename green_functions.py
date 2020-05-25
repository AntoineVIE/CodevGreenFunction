import numpy as np
import cmath 

#Green function (1)
def green1(k,r):
    return np.exp(-1j*k*r)
    
#Green function (2)
def green2(k,r):
    return np.exp(-1j*k*r)/r