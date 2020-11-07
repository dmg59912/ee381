import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string
import math


#PROBLEM 1. (P1.1). a=1.0 ; b=4.0 ; (P1.2). beta =40 ; (P1.3). mu=2.5 ; sigma= 0.75
#PROBLEM 2. The parameter values are: a=1.0 cm; b=4.0 cm
#PROBLEM 3. The parameter value is: beta = 40 days


# 1) Simulate continuous random variables with selected distributions 
    # 1.1 Simulate a Uniform Random Variable.
def uniform_random_variable():
    # Generate the values of the RV X
    a=1; b=4; n=10000
    x=np.random.uniform(a,b,n)

    # Create bins and histogram
    nbins=30; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph
    #
    bins=[float(x) for x in np.linspace(a, b,nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)

    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    #graph labels
    plt.title(' Continuous Random Variable:PMF - Uniform Distribution')
    plt.xlabel('Interval [a,b)')
    plt.ylabel('Probablility')
    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)


    #PLOT THE UNIFORM PDF
    def UnifPDF(a,b,x):
        f=(1/abs(b-a))*np.ones(np.size(x))
        return f

    f=UnifPDF(a,b,b1)
    plt.plot(b1,f,'r')

    plt.show()

    #CALCULATE THEORETICAL MEAN AND STANDARD DEVIATION
    e_x = (a + b)/2
    var_x = np.power(b-a, 2)/12
    print("1.1 statistics ")
    print("Theoretical mean = ", e_x )
    print("Theoretical standard deviation = ", var_x)
    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x=np.mean(x)
    print("\nMean = ", round( mu_x, 3))
    sig_x=np.std(x)
    print("Standard Deviation = ", round(sig_x, 3), '\n')


    # 1.2 Simulate an Exponentially distributed Random Variable.
def exponential_random_variable():
    # Generate the values of the RV X
    beta = 40; n = 10000
    x=np.random.exponential(beta,n)

    # Create bins and histogram
    nbins=30; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph
    

    h1, bin_edges = np.histogram(x,nbins,density=True)

    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    #graph lables
    plt.title(' Continuous Random Variable:PMF - Exponential  Distribution')
    plt.xlabel('Interval ')
    plt.ylabel('Frequency')

    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

    #PLOT THE Exponential PDF
    def EX_PDF(beta,x):
        f = (1/beta) * np.exp(-(1/beta)*x)
        return f

    f=EX_PDF(beta,b1)
    plt.plot(b1,f,'r')


    plt.show()

    print("1.2 statistics")
    #CALCULATE THEORETICAL MEAN AND STANDARD DEVIATION
    print("Theoretical mean = ", beta )
    print("Theoretical standard deviation = ", beta)

    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x=np.mean(x)
    print("\nMean = ", round( mu_x, 3))
    sig_x=np.std(x)
    print("Standard Deviation = ", round(sig_x, 3), '\n')


# 1.3 Simulate an Normal distributed Random Variable.
def normal_random_variable():
    # Generate the values of the RV X
    mu = 2.5; sigma = 0.75; n=10000
    x=np.random.normal(mu,sigma,n)

    # Create bins and histogram
    nbins=30; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph
    #
    bins=[float(x) for x in np.linspace(0, 5,nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)

    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    #graph lables
    plt.title(' Continuous Random Variable:PMF - Normal  Distribution')
    plt.xlabel('Interval ')
    plt.ylabel('Probablility')

    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
    #plt.show()

    #PLOT THE Normal PDF
    def NormalPDF(mu,sigma,x):
        f= (1/(sigma * math.sqrt(2 * math.pi)) ) * np.exp( - (((x - mu)*(x - mu))/(2 * (sigma * sigma)) )  )
        return f

    f=NormalPDF(mu,sigma,b1)
    plt.plot(b1,f,'r')

    plt.show()
    print("1.3 statistics")
    #CALCULATE THEORETICAL MEAN AND STANDARD DEVIATION
    print("Theoretical mean = ", mu )
    print("Theoretical standard deviation = ", sigma)

    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x=np.mean(x)
    print("\nMean = ", round( mu_x, 3))
    sig_x=np.std(x)
    print("Standard Deviation = ", round(sig_x, 3), '\n')


# 2) The Central Limit Theorem 
def central_limit(books):
    # Generate the values of the RV X
    N=100000; nbooks=books; a=1.0; b=4.0
    mu_x=(a+b)/2 ; sig_x=np.sqrt((b-a)**2/12)
    X=np.zeros((N,1))
    for k in range(0,N):
        x=np.random.uniform(a,b,nbooks)
        w=np.sum(x)
        X[k]=w

    # Create bins and histogram
    nbins=30; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph

    #
    bins=[float(x) for x in np.linspace(nbooks*a, nbooks*b,nbins+1)]
    h1, bin_edges = np.histogram(X,bins,density=True)
    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    #graph lables
    plt.title('Central Limit Theorem: PDF of book height and comparison with Gaussian')
    plt.xlabel('PDF')
    plt.ylabel('Book stack height')

    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

    #PLOT THE GAUSSIAN FUNCTION
    def gaussian(mu,sig,z):
        f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
        return f

    f=gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
    plt.plot(b1,f,'r')

    #calculate mean and stardard deviation of thinkness of a book 
    b_me = np.mean(X)
    b_std = np.std(X)
    print("Mean thickness of a single book = ", round(b_me * nbooks, 3))
    print("Standard deviation = ", round(b_std * np.sqrt(nbooks), 3))
    plt.show()


# 3) Distribution of the Sum of Exponential RVs 
def exponential_random_variable_q3():
    N = 10000
    n = 24
    beta = 40; 
    # create a vector of sum elements in random variable 
    sum_24_b = np.zeros((N,1))
    for i in range(0,N):
        x=np.random.exponential(beta,n)
        sm = np.sum(x)
        sum_24_b[i]= sm

    #for i in sum_24_b:
       #print(i)
    # Create bins and histogram
    nbins=30; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph
    

    h1, bin_edges = np.histogram(sum_24_b,nbins,density=True)

    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    #graph lables
    plt.title(' Continuous Random Variable:PMF - Exponential  Distribution')
    plt.xlabel('Battery Lifetime of a carton of 24 pack batteries')
    plt.ylabel('Probability for a carton of batteries')

    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

    #PLOT THE Normal PDF
    mu = n * beta
    sigma = beta * np.sqrt(n)
   
    def NormalPDF(mu,sigma,sum_24_b):
        f= (1/(sigma * math.sqrt(2 * math.pi)) ) * np.exp( - (((sum_24_b - mu)*(sum_24_b - mu))/(2 * (sigma * sigma)) )  )
        return f

    f=NormalPDF(mu,sigma,b1)
    plt.plot(b1,f,'r')

   

    plt.show()

 


    cdf = np.cumsum(h1 * barwidth)
     #graph lables
    plt.title(' Continuous Random Variable:CDF - Exponential  Distribution')
    plt.xlabel('Battery Lifetime of a carton of 24 pack batteries')
    plt.ylabel('Probability for a carton of batteries')

    # PLOT THE BAR GRAPH
    fig1=plt.figure(1)
    plt.bar(b1,h1, cdf, edgecolor=edgecolor)

    plt.plot( b1, cdf ,'r')

    plt.show()

    print("3 statistics")
    #CALCULATE THEORETICAL MEAN AND STANDARD DEVIATION
    print("Theoretical mean = ", beta )
    print("Theoretical standard deviation = ", beta)

    #CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x=np.mean(x)
    print("\nMean = ", round( mu_x, 3))
    sig_x=np.std(x)
    print("Standard Deviation = ", round(sig_x, 3), '\n')


    
#####################################################################################################
def main(): 
    num_book_array = [1,5,10,15]


    # problem 1.1
    uniform_random_variable()
    # problem 1.2
    exponential_random_variable()
    # problem 1.3 
    normal_random_variable()

   # problem 2
    for i in num_book_array:
       print("\nNumber of books = ", i)
       central_limit(i)

    # problem 3 
    exponential_random_variable_q3()


#########################################################################################################        
if __name__ == '__main__':
    main()
  
