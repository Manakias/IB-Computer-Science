import random
x=[]
for i in range(5):
    r=[]
    for j in range(5):
        if random.uniform(0,10)<3:
            r=r+[1]
        else:
            r=r+[0]
    x=x+[r]
print x
