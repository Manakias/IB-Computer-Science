import random
t=[]
for i in range(10000000):
        r=[]
        for j in range(10000000):
                if random.uniform(0,1)<1:
                        r=r+[1]
                else:
                        r=r+[0]
        t=t+[r]
print t
