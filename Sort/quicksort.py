# 퀵 정렬
# 분활 정렬이라고도 부름 (N*logN))


def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[0]
        left, mid, right = [], [], []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr


arr = [3, 5, 1, 2, 9, 6, 4, 7]
print(quick_sorted(arr))
