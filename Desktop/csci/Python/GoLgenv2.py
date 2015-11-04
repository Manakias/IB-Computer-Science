import random
a = []
for i in range(10):
    b = []
    for j in range(10):
        b=b+[0]
    a = a + [b]
for i in range(len(a)):
    for j in range(len(a)):
        r = random.uniform(0,1)
        if r >= 0.5:
            a[i][j]=a[i][j]+1
print a
def Rules(a):
    for i in range(len(a)):
        for j in range(len(a)):
            alpha = a[i-1][j-1]
            beta = a[i-1][j]
            gamma = a[i-1][j+1]
            delta = [i][j-1]
            eta = [i][j+1]
            theta = [i+1][j-1]
            sigma = [i+1][j]
            omega = [i+1][j+1]
            check = [alpha,beta,gamma,delta,eta,theta,sigma,omega]
            for k in range(len(check)):
                s = 0
                if check[k] == 1:
                    s = s+1
            if s == 2 or 3:
                a[i][j]=1
            elif s <=2 or >=4:
                a[i][j]=0
            elif a[i][j]==0 and s == 3:
                a[i][j]==a[i][j]+1
                
                
        