# coding=utf-8

while True:
    try:
        arr = input().split(" ")
        n = int(arr[0])
        m = int(arr[1])

        if not (1 <= n <= 100000):
            print("NULL")
            continue

        if not (1 <= m <= 100000):
            print("NULL")
            continue
        team_set = []
        all_key = set()


        # TODO 解决区间合并的问题
        def add(x, y):
            x_index = -1
            y_index = -1
            for i, t in enumerate(team_set):
                if x_index != -1 and y_index != -1:
                    break
                if x in t and y in t:
                    return
                if x in t:
                    x_index = i
                if y in t:
                    y_index = i
            if x_index == y_index == -1:
                new_set = set()
                new_set.add(a)
                new_set.add(b)
                team_set.append(new_set)
            elif x_index == -1:
                team_set[y_index].add(x)
            elif y_index == -1:
                team_set[x_index].add(y)
            else:
                all_set = team_set[x_index].union(team_set[y_index])
                team_set[x_index] = all_set
                team_set.pop(y_index)


        for _ in range(m):
            line = input()
            a, b, c = list(map(int, line.split(" ")))
            if not (1 <= a <= n) or not (1 <= b <= n) or c not in [0, 1]:
                print("da pian zi")
                continue
            if c == 0:
                union_key = f"{a}-{b}" if a < b else f"{b}-{a}"
                if union_key in all_key:
                    continue
                add(a, b)
                all_key.add(union_key)
            elif c == 1:
                for tmp in team_set:
                    if a in tmp and b in tmp:
                        print("we are a team")
                        break
                else:
                    print("we are not a team")
            else:
                pass
    except Exception as e:
        # print(e)
        break
