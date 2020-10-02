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
def conditional_p(N,p0,e0,e1):
    success = 0
    num_of_s = 0
    for i in range(0,N):
        #Generate S bit
        s = nSidedDie(p0) -1
        if s==1:
            num_of_s += 1
            r = nSidedDie(e1) -1
        else:
            continue
        
        #will check if s = 1 and r = 1 for (S ^ R)
        if s==r: 
            success += 1
    
    #calculate conditional Pr. P(R=1|S=1) = P(S ^ R)/ P(S=1)
    r1_give_s1 = success/num_of_s

    return r1_give_s1

# 3) Conditional probability: P(S=1|R=1)
def conditional_p2(N,p0,e0,e1):
    success = 0
    num_of_r = 0
    for i in range(0,N):
        #Generate S bit
        s = nSidedDie(p0) -1
        if s==1:
            r = nSidedDie(e1) -1
        else:
            r = nSidedDie(e0) -1
        #Will check whenever R = 1 
        if r == 1:
            num_of_r += 1
            #will check if s = 1 and r = 1 for (S ^ R)
            if s ==1:
                success += 1
        
  
    #calculate conditional Pr. P(R=1|S=1) = P(S ^ R)/ P(R=1)
    s1_give_r1 = success/num_of_r

    return s1_give_r1

# 4) Enhance transmission method 
def enhanced_transmission(N,p0,e0,e1):
    success = 0
    #Generate S bit and send 3 times
    s = nSidedDie(p0) -1
    for i in range(0, N):
        r_bits = []
        if s == 1:
            #generate R bit 3 times 
            for i in range(0,3):
                r = nSidedDie(e1) -1
                r_bits.append(r)
        else:
            for i in range(0,3):
                r = nSidedDie(e0) -1
                r_bits.append(r)

     
        majority_b = calculate_D(r_bits)

        #calcutate number of S = D
        if majority_b == s:
            success += 1
    return round(success/N, 3)

def calculate_D(rbits):
    count_0 = 0
    count_1 = 0

    #count majority bits 
    for i in rbits:
        if rbits[i] == 1:
            count_1 += 1
        elif rbits[i]== 0:
            count_0 += 1
    if count_1 > count_0:
        return 1
    else:
        return 0


#####################################################################################################
def main(): 
    # problem 1
    N = 100000
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

    p_success = success/N
    q_failure = 1 - p_success
    print("P of success ", round(p_success,2))
    print("P of failure ", round(q_failure,2))


    # problem 2
    problability = conditional_p(N,p0,e0,e1)
    print(round(problability,2))

    # problem 3
    problability2 = conditional_p2(N,p0,e0,e1)
    print(round(problability2,2))

    # problem 4
    probability3 = 1 - enhanced_transmission(N,p0,e0,e1)
    print(round(probability3, 3))

if __name__ == '__main__':
    main()
  
