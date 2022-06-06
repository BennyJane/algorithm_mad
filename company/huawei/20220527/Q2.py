# coding=utf-8
"""
we are a team
we are not a team
we are a team
da pian zi


"""
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

    team_set = []

    # TODO 解决区间合并的问题
    def merge(change):
        change_set = team_set[change]
        del_arr = []
        for k, t in enumerate(team_set):
            if k == change:
                continue
            common = change_set.intersection(t)
            if not common:
                del_arr.append(k)
                change_set.extend(t)
        for d_index in del_arr:
            team_set.pop(d_index)

    for _ in range(m):
        line = input()
        a, b, c = list(map(int, line.split(" ")))
        if not (1 <= a <= n) or not (1 <= b <= n):
            print("da pian zi")
            continue
        if c == 0:
            is_exist = False
            for i, tmp in enumerate(team_set):
                if a in tmp or b in tmp:
                    team_set[i].add(a)
                    team_set[i].add(b)
                    is_exist = True
                    merge(i)
                    break
            if not is_exist:
                tmp = set()
                tmp.add(a)
                tmp.add(b)
                team_set.append(tmp)
        elif c == 1:
            is_team = False
            for tmp in team_set:
                if a in tmp and b in tmp:
                    is_team = True
                    print("we are a team")
            if not is_team:
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
