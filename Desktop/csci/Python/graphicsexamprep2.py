from graphics import *
import random
win=GraphWin()
win.setCoords(0,0,10,10)
for i in range(10):
    r=random.uniform(0,5)
    center=Point(i,i)
    c=Circle(center, r)
    c.draw(win)
    p2=Point(-i,-i)
    r=Rectangle(center,p2)
    r.draw(win)
