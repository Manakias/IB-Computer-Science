import random
def zeroes(n):
    a = []
    for i in range(n):
        a = a+[0]
        return a
def arrayGenerateRand(mi,ma,n):
    b = []
    for i in range(n):
        b=b+[random.uniform(mi,ma)]
    return b
def mean(ar):
    return sum(ar)/len(ar)
def mean_square(ar):
    s=0
    for i in range(len(ar)):
        s=s+ar[i]**2.
    return s/len(ar)
def variance(ar):
    return mean_square(ar) - mean(ar)**2.
