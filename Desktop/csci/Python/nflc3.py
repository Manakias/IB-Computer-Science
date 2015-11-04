a=[0,1,2,3,4,5]
for i in range(len(a)):
    b=[]
    for j in range(len(a)-1):
        b=b+[i+1-i]
c=[]
for i in range(len(a)/2):
    c=c+[(2*i+1-2*i)]
print c
print b
