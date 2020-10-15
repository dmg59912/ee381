import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string 

#The probability vector for the multi-sided dice is: p=[0.2, 0.1, 0.15, 0.3, 0.2, 0.05]


# 1. Experimental Bernoulli Trials
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

def multi_die(N, p):
    success = 0
    for i in range (0,1000):
        die1 = nSidedDie(p)
        if die1!= 1:
            continue
        die2 = nSidedDie(p)
        if die2 != 2:
            continue
        die3 = nSidedDie(p)
        if die3 != 3:
            continue
        success = success + 1

    return success
        #print("Success! ", success)
        #print("first die = ", die1)
        #print("Second die = ", die2)
        #print("Third die = ", die3)
        #print('\n')

    
def plotting(p, N):
    s = np.zeros((N,1))
    for i in range (0,N):
        d=multi_die(N,p)
        s[i] = d
    b = range (0, 20)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    prob = h1/N
    plt.stem(b1,prob,use_line_collection=True)
    #graph labels
    plt.title('Bernoulli Trials:PMF -Experimental Results')
    plt.xlabel('Number successes for n = 1000')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()



# 2. Experimental Bernoulli Trials
def calculating_BD():
    count = 0




#####################################################################################################
def main(): 
    p = np.array([0.2, 0.1, 0.15, 0.3, 0.2, 0.05])
    N = 10000
    # problem 1
    plotting(p,N)

    # problem 2

#########################################################################################################        
if __name__ == '__main__':
    main()
  
