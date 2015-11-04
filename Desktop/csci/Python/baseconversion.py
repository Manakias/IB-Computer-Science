ans=""
c=213
a=213
b=2
e=0
while b**e<c:
    x=a%(b**(e+1))
    y=x/(b**(e))
    ans=str(y)+ans
    a=a-x
    e=e+1
print ans
