# n 은 먼저 3 과 5 로 나눠져야한다 아닐경우 -1

n = 20
answer = 0
temp = 0

while n > 0 :
if n % 3 == 0:
    answer = + n // 3
elif n % 5 == 0:
    answer = + n // 5

else:
    while n > 0:
        if n % 5 == 0:
            print(n)
            answer = +  n // 5
