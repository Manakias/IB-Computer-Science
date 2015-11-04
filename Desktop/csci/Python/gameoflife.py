import graphics
import random
a = []
for i in range(10):
    b = []
    for j in range(10):
        b=b+[0]
    a = a+[b]
for i in range(len(a)):
    r = random.uniform(0,1)
    if r >= 0.5:
        a[i] = a[i]+[1]
print a
