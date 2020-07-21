arr = []


def size():
    return len(arr)

    if len(arr) == 0:
        return True
    else:
        return False


def push(item):
    arr.append(item)


def prepend(item):
    arr.insert(0, item)


def pop():
    arr.pop()

def at(idx) :
    arr.index