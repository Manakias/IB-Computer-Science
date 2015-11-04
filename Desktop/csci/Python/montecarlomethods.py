import random
p=9500000
n=0.
for i in range(p):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (x**2)+(y**2)<1:
        n=n+1
a=4.0*(n/p)
print a
