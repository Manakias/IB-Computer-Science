import random
a=[]
for i in range(20):
    b=0
    a=a+[random.uniform(6,7)]
for i in range(len(a)):
    b=b+a[i]
print b/len(a)
