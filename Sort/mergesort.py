def merge_sort(arr):
    if len(arr) > 1:
        n = len(arr) // 2
        left = arr[:n]
        right = arr[n:]

        le = merge_sort(left)
        re = merge_sort(right)

        return merge(le, re)
    else:
        return arr


def merge(l, r):
    # index
    i = 0
    j = 0
    arr = []

    while (i < len(l)) & (j < len(r)):
        if l[i] < r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1

    while i < len(l):
        arr.append(l[i])
        i += 1
    while j < len(r):
        arr.append(r[j])
        j += 1

    return arr


a = [3, 5, 1, 2, 9, 6, 4, 5, 7]
print(merge_sort(a))
