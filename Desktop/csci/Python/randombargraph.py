from graphics import *
import random
win=GraphWin()
win.setCoords(0,0,10,10)
import random
x=[1,2,3,4,5,6,7,8,9,10]
a=[]
o=0
for i in range(10):
    o=o+1
    p1=Point(x[o], a[o])
    p2=(4,5)
    a=a+[random.uniform(0,10)]
    r=Rectangle(p1,p2)
    r.draw(win)
    
