import numpy as np

# random matrix 1024 by 1024, composed of 0 and 1
def makeRandomOneZeroMatrix1024by1024():
    ran2d = np.zeros(2**20)
    ran2d[:2**19] = 1
    np.random.shuffle(ran2d)
    
    ran2dMat = ran2d.reshape(1024,1024)
    opposite_ran2dMat = np.logical_not(ran2dMat)*1
    
    return [ran2dMat, opposite_ran2dMat]
