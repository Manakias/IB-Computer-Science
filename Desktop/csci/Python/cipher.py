def setAlpha(n):
    a = n
def setBeta(n):
    b = n
def setGamma(n):
    y = n
def setXray(n):
    x = n
def PrintEncodedMessage(raw_input):
    code = []
    for character in input:
        number = ord(character) - 96
        cip =(number*2)%3
        her = chr(cip)
        code.append(her)
    print code
