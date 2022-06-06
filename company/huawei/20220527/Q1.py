# coding=utf-8

# 字符串处理
def core():
    fail = "ERROR"

    passwd = "******"

    index = int(input())
    line = input()

    if len(line) > 127:
        return fail

    res = []

    first = line.split('"')
    for i, cmd1 in enumerate(first):
        if i % 2 == 1:
            res.append(f'"{cmd1}"')
            continue
        second = cmd1.split("_")
        for cmd2 in second:
            if len(cmd2) == 0:
                continue
            res.append(cmd2)
    if index >= len(res):
        return fail
    res[index] = passwd
    return "_".join(res)


if __name__ == '__main__':
    while True:
        try:
            res = core()
            print(res)
        except Exception as e:
            break
