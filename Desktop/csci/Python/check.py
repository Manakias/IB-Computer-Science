a=[]
for i in range(10):
    b=[0,0,0,0,0,0,0,0,0,0]
    if i%2==0:
        b[i]=b[i]+1
    a=a+[b]
print a
