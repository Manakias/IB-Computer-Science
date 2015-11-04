import math
input=raw_input("ENCODE: ")
input=input.lower()
output=[]
alphray=[]
x=math.sqrt(572)
for character in input:
    alpha = ord(character)
    alphray = alphray+[alpha]
    beta=2.53265
    for i in range(len(alphray)):
        beta=beta*1.4532
    gamma = math.sqrt(((alpha**3)*x)+(beta*x))
    delta = gamma**2
    omega = int(delta)
    output.append(omega)
print output
