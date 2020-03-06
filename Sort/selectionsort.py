# # 선택정렬
# 최소 값을 선택헤서 정렬 하는 방법
# # 시간복잡도 n^2 for 2번

list = [10, 5, 6, 8, 2, 1]


# def sel_sort(a):
#     n = len(a)
#     for i in range(0, n - 1):
#         min_idx = i
#         for j in range(i+1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         temp = a[i]
#         a[i] = a[min_idx]
#         a[min_idx] = temp

#         # a[i], a[min_idx] = a[min_idx], a[i] //둘다 가능


# sel_sort(list)
# print(list)


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if(arr[min] > arr[j]):
                min = j

        arr[i], arr[min] = arr[min], arr[i]


selection_sort(list)
print(list)
