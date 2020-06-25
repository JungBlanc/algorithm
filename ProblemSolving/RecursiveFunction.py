# 예제 중첩 반복문

# n 개의 원소 중 m 개를 고르는 모든 조합을 찾는 알고리즘


def pick(n, picked, to_pick):
    """
    n: 전체 원소의 수
    picked: 지금까지 고른 원소들의 번호
    to_pick: 더 고를 원소의 수
    """
    # 기저 조건: 더 고를 원소가 없을 때 고른 원소들을 출력
    if to_pick == 0:
        print(picked)
        return

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1] + 1

    for _next in range(smallest, n):
        picked.append(_next)
        pick(n, picked, to_pick-1)
        picked.pop(-1)


print(pick(7, [], 4))
