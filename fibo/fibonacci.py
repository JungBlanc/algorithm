# [1, 1, 2, 3, 5, 8, 13 .....]


def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b

    return a


print(fibonacci(50))
