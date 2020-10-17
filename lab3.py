import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string
import math


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

def multi_die(N, p,):
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
    
    
def plotting(p, N ):
    s = np.zeros((N,1))
    for i in range (0,N):
        d=multi_die(N,p)
        s[i] = d
    b = range (0, 16)
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
def calculating_BD(n,x , prob ):
    q = 1.0 - prob
    q_power = n - x
    return float(nCr(n,x) * pow(prob,x)*pow(q,q_power))

def nCr(n,r):
    f = math.factorial
    return f(n)//f(r)//f(n-r)

def plotting2(p, bern,  N ):
    s = []
    for i in range (0,bern):
        d=calculating_BD(1000,i,1/216)

        num_of_occurrences = int ( round(d * N))
        for j in range (0,num_of_occurrences):
            s.append(i)

    b = range (0, 16)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    prob = h1 / N 
    plt.stem(b1,prob,use_line_collection=True)
    plt.title('Bernoulli Trials:PMF - Binomial Distribution')
    plt.xlabel('Number successes for n = 1000')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()



# 3. poisson distribution 
def poisson(n,x,prob):
   lam = n * prob
   f = math.factorial
   e_to_power_lambda = np.exp(1 * -lam )
   return (pow(lam,x) * e_to_power_lambda)/f(x)


def plotting3(p,X_range_bernolli, N):
    s = []
    for i in range (0,X_range_bernolli):
        d=poisson(1000,i,1/216)
        num_of_occurrences = int ( round(d * N))
        for j in range (0,num_of_occurrences):
            s.append(i)

    b = range (0, 16)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s , bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    prob = h1 / N 
    plt.stem(b1 ,prob ,use_line_collection=True)
    plt.title('Bernoulli Trials:PMF - Poisson Distribution')
    plt.xlabel('Number successes for n = 1000')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()


#####################################################################################################
def main(): 
    p = np.array([0.2, 0.1, 0.15, 0.3, 0.2, 0.05])
    N = 10000
    X_range_bernolli = 14
    # problem 1
    plotting(p,N)

    # problem 2
    plotting2(p,X_range_bernolli,N)

    # problem 3
    plotting3(p,X_range_bernolli,N)
#########################################################################################################        
if __name__ == '__main__':
    main()
  
