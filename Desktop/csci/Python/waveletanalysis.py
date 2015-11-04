a=[3,5,2,1,0,5]
for i in range(len(a)):
    d=[]
    for j in range(len(a)-1):
        d=d+[a[j+1]-a[j]]
c=[]
for i in range(len(a)/2):
    c=c+[(a[2*i+1]+a[2*i]/2)]
print d
print c
        

