from graphics import *
import random
import math
def zeros(n):
    a=[]
    for i in range(n):
        a=a+[0]
    return a
def sumArray(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]
    return s
def randomArray(n, mini, maxi):
    a=[]
    for i in range(n):
        a=a+[random.uniform(mini,maxi)]
    return a
def meanArray(a):
    s=0
    return sumArray(a)/len(a)
def varArray(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]**2
    m=meanArray(a)
    return(s/len(a)-m**2)
def maxArray(a):
    maxi=-8592739472
    for i in range(len(a)):
        if a[i]>maxi:
            maxi=a[i]
    return maxi
def histogramArray(mini,maxi,bins,a):
    h=zeros(bins)
    w=(maxi-mini)/bins
    for i in range(len(a)):
        for j in range(bins):
            if a[i]>(mini+j*w) and a[i]<(mini+(j+1)*w):
                h[j]=h[j]+1
    return h
def barGraph(a, window):
    #win=GraphWin("Graphique de la Journee",500,500)
    window.setCoords(-1,-1,(len(a))+1,maxArray(a)+1)
    for i in range(len(a)):
        rec=Rectangle(Point(i, 0),Point(i+1, a[i]))
        rec.draw(window)
def main():
    gauss=zeros(100)
    for i in range(len(gauss)):
        gauss[i]=sumArray(randomArray(10,0,1))
    histo=histogramArray(0. ,10. , 50, gauss)
    win=GraphWin("Graphique de la Journee",500,500)
    barGraph(histo, win)
    t=Text((Point(7,9)),str(meanArray(gauss)))
    t.draw(win)
    u=Text((Point(7,8)),str(varArray(gauss)))
    u.draw(win)
main()
