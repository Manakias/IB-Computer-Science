from graphics import *
import random
win=GraphWin()
win.setCoords(0,0,20,20)
t = Text(Point(8,9),"Exam Prep")
t.draw(win)
for i in range(10):
    p1=Point(random.uniform(0,5),i)
    p2=Point(random.uniform(0,5),i)
    r=Rectangle(p1,p2)
    r.draw(win)
    
