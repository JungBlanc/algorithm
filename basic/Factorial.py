# 팩토리얼 구하기
# 팩토리얼 n! = n (n - 1) (n - 2) ... 1


def factorial(n) :
    mul = 1

    for i in range(1, n+1) :
        mul = mul * i

    return mul


print(factorial(5))