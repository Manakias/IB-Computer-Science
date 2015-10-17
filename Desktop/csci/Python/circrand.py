from graphics import *
import random
wind=GraphWin()
wind.setCoords(0,0,15,15)
for i in range(9):
    r=random.uniform(1,3)
    x=random.uniform(1,10)
    y=random.uniform(1,10)
    d=Circle(Point(x,y), r)
    d.draw(wind)
    
