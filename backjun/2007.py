a = 00
b = 59

if b < 45:
    a -= 1
    b += 60
    if a < 0:
        a = 23
    b -= 45

    print("%02d" % a, end=" ")
    print("%02d" % b)
else:

    print("%02d" % a, end=" ")
    print("%02d" % (b-45))
