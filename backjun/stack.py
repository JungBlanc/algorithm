class stack:
    def __init__(self):
        self.result = []

    def push(self, num):
        self.result.append(num)
        return self.result

    def top(self):
        top = len(self.result) - 1
        return self.result[top]

    def empty(self):
        if len(self.result):
            0
            return -1

    def size(self):
        return len(self.result)

    def pop(self):
        return self.result.pop()


stk = stack()


stk.push(3)

print(stk.result)
