# 선택정렬
# 시간복잡도 n^2 for 2번

list = [10, 5, 6, 8, 2, 1]


def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

        # a[i], a[min_idx] = a[min_idx], a[i] //둘다 가능


sel_sort(list)
print(list)
