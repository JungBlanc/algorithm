
def quick_sort(arr):
    n = len(arr)
    if n > 1 :
        pivot = arr[0]
        left, mid, right = [], [], []
        for i in range(1, len(arr)):
            if arr[i]< pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else :
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sort(left) + mid + quick_sort(right)
    else :
        return arr


