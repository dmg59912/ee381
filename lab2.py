import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string 

##### use probablity p:0.6; e0 = 0.05; e1 = 0.03  #######

# 1) Probability of erroneous transmission 
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

# 2) Conditional probability: P(R=1|S=1)




#####################################################################################################
def main(): 
    # problem 1
    #N = 100000
    N = 100
    success = 0
    p0 = np.array([0.6, 0.4])
    e1 = np.array([0.03,0.97])
    e0 = np.array([0.95,0.05])
    
    for i in range(0,N):
        s = nSidedDie(p0)
        s = s -1 
        if s == 1:
            r = nSidedDie(e1)
            r = r-1
        else:
            r = nSidedDie(e0)
            r = r-1

        if s == r:
            success +=1

    print("success ", success)
    p_success = success/N
    q_failure = 1 - p_success
    print("P of success ", p_success)
    print("P of failure ", round(q_failure,2))
    # problem 2


if __name__ == '__main__':
    main()
  
