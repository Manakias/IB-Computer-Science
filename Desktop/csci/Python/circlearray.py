from graphics import *

win=GraphWin()
win.setCoords(0,0,10,10)
y=0
for i in range(9):
    x=5
    y=y+1
    c=Circle(Point(x,y), 1)
    c.draw(win)
#another way
#for i in range(9)
        #c=Circle(Point(5,i),1)
        #c.draw

