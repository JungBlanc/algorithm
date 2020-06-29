gener = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]
def d(n) :
    first = n // 1000
    second = n // 100
    third = n // 10
    forth = n % 10
    
    return (n + first + second + third + forth)

for i in range(13, 10000) : 
    gener.append(d(gener[-1]))
    
for i in gener :
    if i > 64 :
        break
    print(i)

print(" |")
print(" |")
print(" |")

for i in range(len(gener) - 10, len(gener)) :
    print(gener[i])