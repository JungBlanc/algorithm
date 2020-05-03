score = [10,
         65,
         100,
         30,
         95]
sum = 0
for i in score:
    if(i <= 40):
        i = 40
    sum += i

print(sum / len(score))
