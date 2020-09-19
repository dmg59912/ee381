import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string 
import multiprocessing




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

#plotting
def plotting(p, N):
    n = np.size(p)
    s = np.zeros((N,1))
    for i in range (0,N):
        d=nSidedDie(p)
        s[i] = d
    b = range (1, n + 2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    prob = h1/N
    plt.stem(b1,prob,use_line_collection=True)
    #graph labels
    plt.title('PMF for an n sided die')
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()

################################################################################################################

# 2. Number of rolls needed to get a "7" with two dice
def sum2dice():
    count = 0
    success = False
    while(success == False):
        d1 = np.random.randint(1,7)
        d2 = np.random.randint(1,7)
        sum = d1 + d2
       # print(sum)
        if sum == 7:
            count = count + 1
            success = True
        else:
            count = count + 1
    return count

def plotting2(N):
    s = np.zeros((N, 1))
    higest_success_number = 0
    for i in range (0,N):
        d = sum2dice()
        if d > higest_success_number:
            higest_success_number = d
        s[i] = d
    b = range(1, higest_success_number + 2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    plt.stem(b1, h1, use_line_collection=True)
   

    #graph labels
    plt.title('PMF For number or rolls needed to get to 7 with two dies ')
    plt.xlabel('Successes')
    plt.ylabel('Total Number of successes')
    plt.xticks(b1)
    plt.show()


#####################################################################################################

# 3 Getting 50 heads when tossing 1000 coins 
def coin(N):
    success = 0
    for i in range(0,100000):
        coin = np.random.randint(0,2,N)
        heads = sum(coin)
        #
        if heads == 50:
            success = success + 1
    print('number of 50 heads = ', success, ' with probability of ', success/1000000)

########################################################################################################

# 4 The password hacking problem 
def hack():
    N = 1000
    my_password = "guns"
    m = 80000
    k = 7
    successes = 0
    letter_words = string.ascii_lowercase

    # Generating m random 4 letter words
    for j in range(0,N):
        m_words = []

        for i in range(m ):
            rand_4_letter_word_result = ''.join(random.choice(letter_words) for i in range(4))
            m_words.append(rand_4_letter_word_result)
            if my_password == m_words[i]:
                successes = successes + 1
                break

    print('password was found ', successes, ' times out of ', N ,' a percent of p = ', successes/N)
    

    # Generating m * k random 4 letter words 
    m_words_location  = 0
    successes = 0
    for j in range(0,N):
        m_longer_words= []

        for i in range(m * k ):
            rand_4_letter_word_result = ''.join(random.choice(letter_words) for i in range(4))
            m_longer_words.append(rand_4_letter_word_result)
            if my_password == m_longer_words[i]:
               m_words_location = m_words_location + i 
               successes = successes + 1
               break

    average_m_words_found = round(m_words_location / successes,2)
    probability_of_m = round(average_m_words_found / (m * k),2)
    print('password was found ', successes, ' times out of ', N ,' a percent of p = ', successes/N)
    print('Average of m words produce before finding password is ', average_m_words_found, ', with probablity ', probability_of_m)



#####################################################################################################
def main(): 
    # problem 1
    p = np.array([0.10, 0.15,0.20,0.05,0.30,0.10,0.10])
    N = 100000
    plotting(p,N)

    # problem 2
    plotting2(N)


    # problem 3
    coin(100)

    # problem 4
    hack()


if __name__ == '__main__':
    main()
  