# 삽입정렬
# 필요할떄 바꿈 o(n^2)
list = [10, 5, 6, 8, 2, 1]


def insert_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if(a[j] < a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]

            else:
                break


insert_sort(list)
print(list)
