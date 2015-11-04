import math
while 1==1:
    input = raw_input("ENCODE: ")
    input = input.lower()
    output = []
    for character in input:
        number = ord(character) - 82
        b = 1.414
        alpha = number*b
        beta = int(alpha)
        cipher = chr(beta)
        if beta<127:
            output.append(cipher)
        else:
            beta=beta-25
            cipher=chr(beta)
            output.append(cipher)
    print output
