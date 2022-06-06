# coding=utf-8


# 最长连续字符串
def core():
    a = input()
    b = input()
    v = int(input())

    n = len(a)

    nums = [0] * n

    for i in range(n):
        diff = abs(ord(a[i]) - ord(b[i]))
        nums[i] = diff
    max_width = 0

    left = 0
    right = 0
    total = 0
    while right < n:
        total += nums[right]
        if total <= v:
            max_width = max(right - left + 1, max_width)

        while left <= right and total > v:
            total -= nums[left]
            left += 1

        right += 1

    print(max_width)


if __name__ == '__main__':
    while True:
        try:
            core()
        except Exception as e:
            # print(e)
            break

"""
xxcdefg
cdefghi
5
"""
