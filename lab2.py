import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string 

##### use probablity p:0.6; e0 = 0.05; e1 = 0.03  #######

# 1) funtion for an n sided die
def nSidedDie(p):
    n = np.size(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = np.random.rand()
    for k in range (0,n):
        if r > cp [k] and r <= cp[k + 1]:
             d = k + 1
             break
    return d
#





#####################################################################################################
def main(): 
    # problem 1
    p0 = np.array([0.6, 0.4])
    e1 = np.array([0.03,0.97])
    e0 = np.array([0.95,0.05])
    s = nSidedDie(p0)
    s = s -1 
    if s == 1:
        r = nSidedDie(e1)
        r = r-1
    else:
        r = nSidedDie(e0)
        r = r-1

    print("S is ", s, " and R is " , r)
    # problem 2


if __name__ == '__main__':
    main()
  
