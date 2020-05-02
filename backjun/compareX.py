n = 10
t = 5
arr = [1 ,10, 4, 9, 2 ,3, 8 ,5, 7, 6]
answer = []

def compareX(question) :
    for i in question :
        if(t > i) :
            answer.append(i)


compareX(arr)

print(answer)

# a = "1 10 4 9 2 3 8 5 7 6"

# b = list(map(int, a.split(" ")))


# print(b)

for i in range(len(answer)) :
    print(answer[i], end=' ')