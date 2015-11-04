from graphics import *
import random
a=[]
for k in range(25):
    b=int(random.uniform(0,2))
    if b == 1:
        a=a+[1]
    elif b == 0:
        a=a+[0]
print a
win=GraphWin()
win.setCoords(0,0,200,200)
L=len(a)





    
