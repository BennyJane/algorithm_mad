"""
---------------------------------------------------------------------------
二星题目：较难题目整理
---------------------------------------------------------------------------
"""


# 15、高矮个子排队
# 核心：身高不等，不存在重复值
# 贪心思想：不相邻的两个矮位置交换，距离过大（>=3），不如两个矮位置与两侧较小值交换（=2）
# 可以通过反证法推理，相邻两个矮位置，在不存在重复数据的情况下，无法成立 a < x < b > y > c
# ==> a < x < c, c < y < a 矛盾
def solution1(s):
    array = list(map(int, s.split(" ")))
    n = len(array)
    count = 0
    # 只考虑奇数位置，即矮的位置，
    # 如果小于两侧不变动
    # 如果大于其中一侧数值，则选择两侧位置中较小的值，交换到当前矮的位置
    for i in range(1, n, 2):
        pre = array[i - 1]
        cur = array[i]
        # 末尾索引可能超出范围
        back = array[i + 1] if i + 1 < n else cur + 1
        # 判断当前位置是否满足矮条件
        if pre > cur and cur < back:
            continue
        count += 1
        # 交换较小的值
        if pre < back:
            array[i], array[i - 1] = pre, cur
        else:
            array[i], array[i + 1] = back, cur
    print(array)
    return count


"""
题目
给定一字符集合a 和 一字符串集合b；用集合a里的字符匹配集合b中的字符串，求成功匹配的字符串总长度；

其中 a匹配b中一个字符串时，a中字符不能重复使用；但在匹配下一个字符串时，可重复使用；

输入
字符集合a : {‘1’,‘2’,‘3’,‘4’,‘4’}

字符串集合b：{‘123’,‘344’,‘112’,‘345’}

输出
集合b中字符串中，能与a匹配的有 123 与 344；顾输出总长度 6

其中

112不匹配是因为集合a中只有1个’1’

345不匹配是因为集合a中没有 ‘5’

样例输入:
{‘1’,‘2’,‘3’,‘4’,‘4’}

{‘123’,‘344’,‘112’,‘345’}

样例输出:
6

https://blog.csdn.net/q410654146/article/details/109790180
"""


# 五键键盘
def solution3(s):
    board = ""
    select = ""
    back = ""

    # 遍历所有操作
    # a：判断是否有选中操作，清空选中内容（只有全选一种情况）；写入a； TODO 取消选中状态
    # c：判断是否有选中操作，将选择对象赋值给剪切板，覆盖操作
    # x：判断是否有选中操作，将选择对象赋值给剪切板（覆盖），并删除显示屏上的内容，TODO 取消选中状态
    # v：类似a操作 TODO 取消选中状态
    # a：全选


# 12、第k个排列
# TODO 重点 ==》 相似题目整理
def solution4(n, k):
    from math import factorial

    array = [i + 1 for i in range(n)]

    ans = []
    # FIXME k 必须先减少1， 避免当k = factorial(cnt)时，索引计算错误
    # array数组从0开始
    k -= 1
    cnt = n - 1
    while cnt >= 0:
        # 首位固定，剩余位置变动，可以组合的子集数量 1 * (cnt) *(cnt - 1) *(cnt - 2) *(cnt - 3) ... 1
        index = k // factorial(cnt)
        # FIXME 选中数字，并从原数组中删除
        target = array[index]
        array.remove(target)
        ans.append(str(target))

        k -= index * factorial(cnt)
        cnt -= 1

    return "".join(ans)


# 时间排序：转同一单位
# http://www.amoscloud.com/?p=3448

# 花费最多金额
# http://www.amoscloud.com/?p=3446
# 递归、暴力遍历（三层循环）


# 水仙花数
# 模拟法：检测输入异常

# 字符串：交换两个位置，获取最小字符串
# http://www.amoscloud.com/?p=3155
"""
17、标题:字符串变换最小字符串
【字符串变换最小字符串】给定一个字符串s，最多只能进行一次变换，返回变换后能得到的最小字符串(按照字典序进行比较)。变化规则:交换字符串中任意两个不同位
置字符。
输入描述: 一串小写字母组成的字符串s
输出描述: 按照要求进行变换得到最小字符串
备注: s是都是小写字符组成1<=s.length<=1000
示例1:
输入
abcdef
输出
abcdef
"""


def solution5(s: str):
    order = list(s)
    order.sort()

    # 从前往后找到第一个不符合升序排列的位置
    # 从后往前找到应该排到上面的位置的字符，然后交换两个位置
    # 确保交换到最靠后的位置
    data = list(s)
    for i, c in enumerate(s):
        if c == order[i]:
            continue
        for j in range(len(s) - 1, i, -1):
            if s[j] == order[i]:
                data[i] = order[i]
                data[j] = c
                return "".join(data)
    return s


# 【计算面积】：
# - 计算每个横坐标对应的实际y轴的值， 该值决定了到下个坐标轴之间的面积
# - 利用横坐标分割多个区间，然后计算每个区间的面积
def Solution6(moves, end):
    array = [0] * end
    y = 0
    for i in range(end):
        y = y + moves.get(i, 0)
        array[i] = y

    return sum([abs(c) for c in array])


def Solution6_1(moves, end):
    pre_x, pre_y, area = 0, 0, 0

    for x, y in moves.items():
        area += (x - pre_x) * abs(pre_y)

        pre_x = x
        pre_y += y

    # 处理末尾
    area += (end - pre_x) * abs(pre_y)
    return area


# 流水线最小耗时

# 分糖果
# TODO 贪心思想
def solution7(n):
    count = 0

    current = n
    while current != 1:
        # 等于3， 快速退出
        if current == 3:
            count += 2
            break
        if current % 2 == 1:
            # 下一个值，是否还是偶数
            upper = (current + 1) / 2
            if upper % 2 == 0:
                print("current-2: {}".format(current))
                current += 1
            else:
                print("current-1: {}".format(current))
                current -= 1
        else:
            # 偶数，只考虑一种情况： FIXME 题目信息暗示
            current //= 2
        count += 1

    return count


def solution7_1(n):
    count = float("inf")

    def dfs(cur, cnt):
        nonlocal count
        if cur == 1:
            count = min(count, cnt)
            return
        if cnt >= count:
            return
        if cur % 2 == 0:
            dfs(cur // 2, cnt + 1)
        else:
            # FIXME 抛开题目含义，偶数情况下，也可以考虑其他操作
            pass
        dfs(cur + 1, cnt + 1)
        dfs(cur - 1, cnt + 1)

    dfs(n, 0)

    return count


# 两个没有相同字符的元素长度乘积的最大值
# http://www.amoscloud.com/?p=2915
def solution8(s):
    array = list(s.split(","))

    unique = [set(c) for c in array]

    ans = 0
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = unique[i]
            s2 = unique[j]
            if not s1.intersection(s2):
                ans = max(ans, len(array[i]) * len(array[j]))
    return ans


# 21、火星文计算
# TODO 递归函数设计
def solution9(s):
    def dfs(exp):
        # 按照运算顺序，逆向递归
        n = len(exp)
        for i in range(n - 1, -1, -1):
            c = exp[i]
            if c != "#":
                continue
            x = exp[:i]
            y = exp[i + 1:]
            return 2 * dfs(x) + 3 * dfs(y) + 4
        for i in range(n - 1, -1, -1):
            c = exp[i]
            if c != "$":
                continue
            x = exp[:i]
            y = exp[i + 1:]
            return 3 * dfs(x) + dfs(y) + 2

        # 剩余整数
        return int(exp)

    return dfs(s)


# 分积木
# 只分成两组; TODO 数组长度过长，只能使用动态规划判断
def solution10(s):
    array = list(map(int, s.split(",")))
    n = len(array)
    total = sum(array)

    array.sort()

    if total % 2 != 0:
        return False
    target = total // 2
    if array[-1] > target:
        return False
    if n <= 1: return False

    # 前i个数值，是否可以拼出j的值
    dp = [[False for _ in range(target + 1)] for _ in range(n)]
    # 只有1个值时，不选，可以实现0
    for i in range(n):
        dp[i][0] = True

    for i in range(1, n):
        for t in range(1, target + 1):
            # TODO 核心：选择当前值 or 不选择当前值
            cur = array[i] if t >= array[i] else 0
            dp[i][t] = dp[i - 1][t] | dp[i - 1][t - cur]
            # if t >= cur:
            #     dp[i][t] = dp[i - 1][t] | dp[i - 1][t - cur]
            # else:
            #     # 不使用当前值cur，是否可以组成t
            #     dp[i][t] = dp[i - 1][t]

    return dp[n - 1][target]


# 分成k组
def solution10_k(s, k):
    array = list(map(int, s.split(",")))
    n = len(array)
    total = sum(array)
    if n < k or total % k != 0:
        return False
    target = total // k

    array.sort()
    if array[-1] > target:
        return False

    used = [False] * n

    def dfs(begin, pre_sum, group_id):
        # 前面k-1组，可以完全分组后，最后一组不需要处理
        if group_id == k - 1:
            return True

        if pre_sum == target:
            # 完成一组分配后，继续下一组分配
            return dfs(n - 1, 0, group_id + 1)

        for i in range(begin, -1, -1):
            # FIXME 跳过相同字符: 必须确保当前递归深度中，前一个也没有使用
            # 即 在当前递归深度中，相同且可用的 数字，只需要讨论一次
            if i < begin and array[i] == array[i + 1] and not used[i + 1]:
                continue
            if used[i]:
                continue
            cur = array[i]
            if pre_sum + cur > target:
                continue

            used[i] = True
            # FIXME 核心：判断是否可以成立
            if dfs(i - 1, pre_sum + cur, group_id):
                return True
            used[i] = False
        return False

    return dfs(n - 1, 0, 0)


if __name__ == '__main__':
    # print(solution5("bcdefa"))

    # num7 = 15
    # print(solution7(num7))
    # print(solution7_1(num7))

    # for i in range(21, 300):
    #     solution7(i)
    # if solution7_1(i) != solution7(i):
    #     print("error: " + i)
    # else:
    #     print("success: {}".format(solution7_1(i)))

    # print(solution8("iwdvpbn,hk,iuop,iikd,kadgpf"))

    # print(solution10_k("4,3,2,3,5,2,1", 4))
    print(solution10_k("1,1,1,1,2,2,2,2", 4))
