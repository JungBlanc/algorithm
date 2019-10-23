string = "ANndndnAAALLombdN"
arr = []


def swap_string(str):
    for i in range(len(string)):
        if str[i] >= "a" and str[i] <= "z":
            arr.append(str[i].upper())
        else:
            arr.append(str[i].lower())


swap_string(string)
a = "".join(arr)
print(a)


# 간단하게
# string.swapcase()
