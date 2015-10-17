import random
#This imports the random library, needed to generate random coordinates
P=4000000
N=0.
#These two variables are the amount of points that will be
#tested to see if they are inside a circle
#with a radius of 1 within the 2x2 box.
for i in range (P):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (x*x+y*y)<1:
        N=N+1
#This is the algorithm that checks whether a point is within the circle. The
#coordinates of the point are generated randomly with the two random.uniform
#commands, and then if they satisfy the condition, they are added to a running
#tally of the points that are found to be within the circle.
A=4.0*(N/P)
#The total amount of points that are found to be within the circle are then
#calculated with the above equation to deliver the estimate for pi.
print A
