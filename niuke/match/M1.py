"""
【删除】
有一个数组 a[N] 顺序存放 0 ~ N-1 ，要求每隔两个数删掉一个数，到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。以 8 个数 (N=7) 为例 :｛ 0，1，2，3，4，5，6，7 ｝，0 -> 1 -> 2 (删除) -> 3 -> 4 -> 5 (删除) -> 6 -> 7 -> 0 (删除),如此循环直到最后一个数被删除。

数据范围：


输入描述:
每组数据为一行一个整数n(小于等于1000)，为数组成员数

输出描述:
一行输出最后一个被删掉的数的原始下标位置。

输入例子1:
8

输出例子1:
6

输入例子2:
1

输出例子2:
0


"""


def one():
    while True:
        try:
            n = int(input())
            array = [i for i in range(n)]
            ans = -1
            index = 2
            while len(array) > 0:
                tmp = []
                limit = len(array)
                for i in range(limit):
                    if i != index:
                        tmp.append(array[i])
                    else:
                        ans = array[i]
                        index += 3
                index = index % limit
                array = tmp
            print(ans)
        except Exception as e:
            break


# def one1():
while True:
    try:
        n = int(input())
        array = [i for i in range(n)]
        index = 0
        ans = -1
        while len(array) > 0:
            index = (index + 2) % (len(array))
            ans = array[index]
            array = array[:index] + array[index + 1:]
        print(ans)
    except Exception as e:
        break


"""
字符集合
输入一个字符串，求出该字符串包含的字符集合，按照字母输入的顺序输出。

数据范围：输入的字符串长度满足  ，且只包含大小写字母，区分大小写。

本题有多组输入

输入描述:
每组数据输入一个字符串，字符串最大长度为100，且只包含字母，不可能为空串，区分大小写。

输出描述:
每组数据一行，按字符串原有的字符顺序，输出字符集合，即重复出现并靠后的字母不输出。

输入例子1:
abcqweracb

输出例子1:
abcqwer

输入例子2:
aaa
"""


def two():
    while True:
        try:
            s = input()

            d = set()
            ans = ""
            for i, c in enumerate(s):
                if c in d:
                    continue
                ans += c
                d.add(c)
            print(ans)
        except Exception as e:
            break


"""
数独: 9阶数独
数独是一个我们都非常熟悉的经典游戏，运用计算机我们可以很快地解开数独难题，现在有一些简单的数独题目，请编写一个程序求解。
如有多解，输出一个解

输入描述:
输入9行，每行为空格隔开的9个数字，为0的地方就是需要填充的。

输出描述:
输出九行，每行九个空格隔开的数字，为解出的答案。
"""
# while True:
#     try:
#         for _ in range(9):
#             row = input()
#     except Exception as e:
#         break

if __name__ == '__main__':
    # two()

    pass
