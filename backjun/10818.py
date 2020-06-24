N = 5


arr = [20, 10 ,35, 30, 7]
maxValue = -1
minValue = 1000000
for i in arr :
    if i > maxValue : 
        maxValue = i
    if i < minValue :
        minValue = i

print(minValue, end=" ")
print(maxValue)