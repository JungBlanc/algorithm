list = [10, 5, 6, 8, 2, 1]


def selection(list):
    n = len(list)

    for i in range(0, n - 1):
        min_idx = i
        for j in range(i+1, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]


selection(list)
print(list)
