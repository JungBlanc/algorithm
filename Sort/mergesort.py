def merge_sorted(a):
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        l = merge_sorted(left)
        r = merge_sorted(right)
        print(l, r)
        return merge(l, r)
    else:
        return a


def merge(left, right):
    i = 0
    j = 0
    arr = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while (i < len(left)):
        arr.append(left[i])
        i += 1
    while (j < len(right)):
        arr.append(right[j])
        j += 1
    print("arr", arr)

    return arr


a = [3, 5, 1, 2, 9, 6, 4, 5, 7]
print(merge_sorted(a))
