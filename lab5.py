import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import string
import math


# Use the following numbers 
# Total number of bearings: N=1,500,000
# • Population mean: μ = 55  grams;
# • Population standard deviation: σ= 5  grams;
# • Sample sizes: n= 1, 2, ... 200


# 1) Effect of Sample Size on Confidence Levels

def confidence_intervals():

    N = 15000000 
    mu = 55
    sigma = 5 
    n = range(1, 201) 
    average_values = []
    pop = np.random.normal(mu, sigma, N)

    for i in n:
        X = pop[random.sample(range(N), i)]
        mean = X.mean()
        average_values.append(mean)

    #graph labels 
    plt.figure("1A")
    plt.title("Sample Means and 95% Confidence Intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("x_bar")

    plt.plot(n, average_values, "ob", marker = 'x', linestyle = 'none')
    plt.plot(n, [mean for x in n])
    X = np.linspace(1, 200)
    plt.plot(X, mu + 1.96*sigma / (X**(1/2)), color = 'red', linestyle = '--')
    plt.plot(X, mu - 1.96*sigma / (X**(1/2)), color = 'red', linestyle = '--')
    plt.ylim(top = 55 + 10)
    plt.ylim(bottom = 55 - 10)

    #graph labes 
    plt.figure("1B")
    plt.title("Sample Means and 99% Confidence Intervals")
    plt.title("Sample means and 99% confidence intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("x_bar")

    plt.plot(n,average_values,"ob",marker = 'x', linestyle = 'none')

    # Plot average line
    plt.plot(n,[mean for x in n]) 
    x = np.linspace(1,200)
    plt.plot(X, mu + 2.58*sigma / (x**(1/2)), color = "green", linestyle = '--')
    plt.plot(X, mu - 2.58*sigma / (x**(1/2)), color = "green", linestyle = '--')
    plt.ylim(top = 55 + 10)
    plt.ylim(bottom = 55 - 10)
    plt.show()


def sample_mean_population_mean(trials,t_95,t_99,size):
    N = 15000000 
    mu = 55
    sigma = 5
    bn = np.random.normal(mu,sigma,N)
    sample = size

    success_for_95 = 0
    success_for_99 = 0
    success_for_95_t = 0
    success_for_99_t = 0


    for i in range (0, trials):

        pop = bn[random.sample(range(N), sample)]
        pop_mean = np.sum(pop)/sample
        total = 0
        for j in range(0, len(pop)):
            total = total + (pop[j]-pop_mean) ** 2
        pop_s = total/(sample-1)
        pop_s = math.sqrt(pop_s)
        pop_sd = pop_s/math.sqrt(sample)
        

        #using normal distribution 
        u_upper_95 = pop_mean + 1.96*(pop_sd)
        u_lower_95 = pop_mean - 1.96*(pop_sd)

        u_upper_99 = pop_mean + 2.58*(pop_sd)
        u_lower_99 = pop_mean - 2.58*(pop_sd)
        
        #using t-distribution 
        t_upper_95 = pop_mean + t_95*(pop_sd)
        t_lower_95 = pop_mean - t_95*(pop_sd)

        t_upper_99 = pop_mean + t_99*(pop_sd)
        t_lower_99 = pop_mean - t_99*(pop_sd)
        
        #calculating number of success 
        if u_lower_95 <= mu and u_upper_95 >= mu:
            success_for_95 += 1
        if u_lower_99 <= mu and u_upper_99 >= mu:
            success_for_99 += 1
        if t_lower_95 <= mu and t_upper_95 >= mu:
            success_for_95_t += 1
        if t_lower_99 <= mu and t_upper_99 >= mu:
            success_for_99_t += 1
    
    print('Success Rate using normal, sample =', sample, '95% confidence interval ',success_for_95/trials )
    print('Success Rate using normal, sample =', sample, '99% confidence interval ',success_for_99/trials)
    print('Success Rate using student t, sample =' , sample, '95% confidence interval ',success_for_95_t/trials)
    print('Success Rate using student t, sample =', sample, '99% confidence interval ',success_for_99_t/trials)
    print('')

#######################################################################################################
def main():


    # problem 1
    #confidence_intervals()

    # problem 2
    trials = 10000

    sample_mean_population_mean( trials, 2.78, 4.6, 5)
    sample_mean_population_mean( trials, 2.02, 2.7, 40)
    sample_mean_population_mean( trials, 1.98, 2.62, 120)
#########################################################################################################        
if __name__ == '__main__':
    main()
  