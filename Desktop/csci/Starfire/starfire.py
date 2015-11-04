import numpy
import random
keygen = raw_input("Do you have a key? Y or N: ")
if keygen == "N":
    rgk = []
    print "A key has been randomly generated. Take note of it if you plan to use it further."
    for i in range(256):
        r = random.uniform(65,123)
        g = int(r)
        rgk = rgk+[g]
    rgkey = ""
    for i in range(len(rgk)):
        c = chr(rgk[i])
        rgkey = rgkey+c
    print rgkey            
choice = raw_input("Encode or Decode? ")
key=[]
m=[]
ecm=[]
dcm=[]
dct=[]
if choice == "Encode":
    input2 = raw_input("Insert message to encode: ")
    for character in input2:
        m=m+[ord(character)]
    print m
    input3 = raw_input("Input Key: ")
    for character in input3:
        key=key+[ord(character)]
    usablekey=[]
    for i in range(len(m)):
        usablekey=usablekey+[key[i]]
    print usablekey
    ecmo=numpy.multiply(m,usablekey)
    ecm.append(ecmo)
    print ecm
    print "Encoded Message"
if choice == "Decode":
    input2 = raw_input("Insert sequence to decode: ").split(', ')
    m=m+(input2)
    print len(m)
    print m
    input3 = raw_input("Input Key: ")
    for character in input3:
        key=key+[ord(character)]
    usablekey=[]
    for i in range(len(m)):
        usablekey=usablekey+[key[i]]
    print usablekey
    dcm=numpy.divide(m,usablekey)
    c1=[]
    c1.append(dcm)
    c2=[]
    for i in range(len(c1)):    
        c2 = c2+int(c1[i])
    final = ""
    for i in range(len(c2)):
        final = final+chr(c2[i])
    print final
    print "Decoded Message"
