# coding=utf-8
from collections import defaultdict


def core():
    arr = input().split(" ")
    n = int(arr[0])
    m = int(arr[1])

    if not (1 <= n <= 100000):
        print("NULL")
        return

    if not (1 <= m <= 100000):
        print("NULL")
        return

    FLAG = -1
    graph = [FLAG for _ in range(n + 1)]
    all_key = set()

    team_ids = defaultdict(set)

    def build(x: int, y: int):
        nonlocal team_ids
        x_id = graph[x]
        y_id = graph[y]
        if x_id == y_id == FLAG:
            graph[x] = graph[y] = x
            team_ids.get(x, set()).add(x)
            team_ids.get(x, set()).add(y)
        elif x_id == FLAG:
            graph[x] = graph[y]
            team_ids.get(y_id, set()).add(x)
        elif y_id == FLAG:
            graph[y] = graph[x]
            team_ids.get(x_id, set()).add(y)
        else:
            # FIXME 解决区间合并的问题
            other_ids = team_ids.get(x_id, set())
            for pos in other_ids:
                graph[pos] = y_id
            all_set = team_ids.get(x_id, set()).union(team_ids.get(y_id))
            team_ids[y_id] = all_set
            del team_ids[x_id]

    for _ in range(m):
        line = input()
        a, b, c = list(map(int, line.split(" ")))
        if not (1 <= a <= n) or not (1 <= b <= n):
            print("da pian zi")
            continue
        if c == 0:
            union_key = f"{a}-{b}" if a < b else f"{b}-{a}"
            if union_key in all_key:
                continue
            build(a, b)
            all_key.add(union_key)
        elif c == 1:
            a_id = graph[a]
            b_id = graph[b]
            if a_id == b_id and a_id != FLAG:
                print("we are a team")
            else:
                print("we are not a team")
        else:
            print("da pian zi")


if __name__ == '__main__':
    while True:
        try:
            core()
        except Exception as e:
            # print(e)
            break

"""
5 6
1 2 0
1 2 1
1 5 0
2 3 1
2 5 1
1 3 2
"""
