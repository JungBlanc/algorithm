n = "88765142"


def string_sort(a):
    return int(''.join(sorted(str(a), reverse=True)))


print(string_sort(n))
