import random
a=[]
for i in range(1000):
    s=[]
    for j in range(10):
        s=s+[random.uniform(0,1)]
    a=a+[s]
h=[]
for k in range(10):
    h=h+[s]
print h
