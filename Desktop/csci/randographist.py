from graphics import *
import random
a=[]
#get the fill
for i in range(1000):
    s=0
    for j in range(10):
        s=s+random.uniform(0,1)
    a=a+[s]
#get the bins
h=range(10)
for k in range(10):
    h[k]=0
#fill the bins
for i in range(1000):
    r=int(a[i])
    h[r]=h[r]+1
win=GraphWin("Graph",35,35)
win.setCoords(0,0,35,35)
#make the graph

    
