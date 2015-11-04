import random
a = []
for i in range(1000):
    b = []
    for j in range(1000):
        b=b+[0]
a = a+[b]
for i in range(len(a)):
    r = random.uniform (0,1)
    if r >= 0.5:
        a[i][j]=a[i][j]+[1]
print a
#for i in range(len(a)):
    #for j in range(len(a)):
        #alpha = (a[i-1],[j-1])
        #beta  = (a[i-1],[j])
        #gamma = (a[i-1],[j+1])
        #delta = (a[i], [j-1])
        #sigma = (a[i], [j+1])
       # eta = (a[i+1], [j-1])
        #echo = (a[i+1], [j])
       # omega = (a[i+1], [j+1])
#check = [alpha,beta,gamma,delta,sigma,eta,echo,omega]
#for i in range(len(check)):
    #s = 0
    #if check[i] == 1:
       # s = s+1
    #if s == 2 or 3:
        #a[i] = a[i]+1
        
        
    