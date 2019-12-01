list = [10, 5, 6, 8, 2, 1]


def insertSort(list):
    n = len(list)
    for i in range(n):
        for j in range(i, 0, -1):
            if(list[j] < list[j-1]):
                list[j], list[j-1] = list[j-1], list[j]
                print(list)

            else:
                break


insertSort(list)
print(list)
