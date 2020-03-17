arr = [1, 1, 1, 1, 1]
target = 3


def BFS(arr, target):
    visited_node = [0]

    for i in arr:
        tempArr = []
        for j in visited_node:
            tempArr.append(j+1)
            tempArr.append(j-1)
        visited_node = tempArr

    return visited_node


answer = BFS(arr, target)
print(answer.count(3))
