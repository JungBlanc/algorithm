list = [10, 5, 6, 8, 2, 1]

# 뒤에서부터 정렬


def sorter(list):
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


sorter(list)
print(list)
