from graphics import *
import random
a=[]
for i in range(1000):
    s=0
    for j in range(10):
        s=s+random.uniform(0,1)
    a=a+[s]
h=[]
for i in range(10):
    h=h+[0]
for i in range(1000):
    r=int(a[i])
    h[r]=h[r]+1
win=GraphWin(100,100)
win.setCoords(0,0,100,100)
L=len(h)
bl=[]
for i in range(L):
    bl=bl+[Point(i,0)]
tr=[]
for i in range(L):
    tr=tr+[Point(i+1,h[i])]
rec=[]
for i in range(L):
    rec=rec+[Rectangle(bl[i],tr[i])]
for i in range(L):
    rec[i].draw(win)
