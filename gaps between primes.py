#This code calculates the gaps between all prime numbers between 1 and 1,000,000 and plots them in a histogram


#import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
#histogram of gaps between primes
#first make list of primes
primes=[]
for i in range(3,1000000):#exclude 2 as prime
    #check if prime
    if sp.isprime(i)==True:
        primes.append(i)
#then make list pf gaps between the primes
gaps=[]
for i in range(len(primes)-1):
    gaps.append(primes[i+1]-primes[i])
#make histogram w/out log scale
freq=[]
histo=[]
for i in gaps:
    if i not in histo:
        freq.append(1)
        histo.append(i)
    else:
        index=histo.index(i)
        freq[index]+=1
plt.scatter(histo,freq)
plt.title('Histogram of prime gaps')
plt.xlabel('Frequency')
plt.show()
#plot histogram with log axis to show exp relationship
plt.scatter(histo,freq)
plt.yscale('log')
plt.title('Histogram of prime gaps with a log distribution')
plt.xlabel('Frequency')
plt.show()