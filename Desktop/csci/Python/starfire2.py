input = raw_input("Insert Key: ")
keylog = []
for character in input:
    a = ord(character)
    keylog.append(a)
for i in range(len(keylog)):
    if keylog(i)>=26:
        b=keylog(i)
        b=b-26
    if keylog(i)<=26:
        c=keylog(i)
        c=c+26
print keylog
