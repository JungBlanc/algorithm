# bubble 정렬
# 시간복잡도 n^2 for 2번

list = [10, 5, 6, 8, 2, 1]


def bub_sort(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                # temp = a[j]
                # a[j] = a[j+1]
                # a[j+1] = temp

                a[j], a[j+1] = a[j+1], a[j]

            print(a)


bub_sort(list)
print(list)
