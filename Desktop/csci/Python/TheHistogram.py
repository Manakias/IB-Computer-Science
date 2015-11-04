from graphics import *
import random
a=[]
for k in range(1000):
    s=0
    for j in range(10):
        s=s+random.uniform(0,1)
    a=a+[s]
h=[]
for k in range(10):
    h=h+[0]
for k in range(1000):
    r=int(a[k])
    h[r]=h[r]+1
L=len(h)
M=250
win=GraphWin("Le Graf",)
win.setCoords(-0.2,0,L+10,L+10.2)
bl=[]
for k in range(L):
    bl=bl+[Point(k,0)]
tr=[]
for k in range(L):
    tr=tr+[Point(k+1,h[k])]
rec=[]
for k in range(L):
    rec=rec+[Rectangle(bl[k],tr[k])]
for k in range(L):
    rec[k].draw(win)
