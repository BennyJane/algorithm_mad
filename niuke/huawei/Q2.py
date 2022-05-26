# 1、5键键盘的输出
from collections import defaultdict


def solution1(s):
    s = s.replace(" ", "")
    # 面板上字符数量
    count = 0

    # 剪切板上字符数量
    copy_cnt = 0
    # 选中字符数量
    # TODO 只有一种选择方式：全选
    select_cnt = 0

    for c in s:
        if c == '1':  # 输入a
            # 选中状态下，清空选中字符
            if select_cnt > 0:
                # count = count - select_cnt + 1
                count = 1
            else:
                count += 1
            # 取消选中状态
            select_cnt = 0
        elif c == '2':  # 复制
            if select_cnt > 0:
                copy_cnt = select_cnt
            # 复制不会取消选中状态
        elif c == '3':  # 剪切
            # 有效剪切：必然是选中状态
            # if select_cnt > 0:
            copy_cnt = select_cnt
            select_cnt = 0
            count = 0
        elif c == '4':  # 粘贴
            # 选中状态下，覆盖选择对象
            if select_cnt > 0:
                count = copy_cnt
                select_cnt = 0
            else:
                count += copy_cnt
        else:  # 全选
            select_cnt = count
    return count


# 2、N进制减法
def solution2(n, a, b):
    if len(a) > 1 and a[0] == "0":
        return "-1"
    if len(b) > 1 and b[0] == "0":
        return "-1"

    flag = 0
    a_int = int(a, n)
    b_int = int(b, n)
    res = a_int - b_int
    if res < 0:
        flag = -1
        res *= -1
    print(res)
    # 十进制转n进制
    arr = []
    while res > 0:
        arr.append(res % n)
        res //= n
    # res_str = ""
    # for i in range(len(arr) - 1, -1, -1):
    #     res_str += str(arr[i])
    res_str = "".join(list(map(str, arr)))[::-1]
    return f"{flag} {res_str}"


# 4、VLAN资源池
def solution4(s, target: int):
    array = s.split(",")

    sorted_arr = []
    for area in array:
        if "-" in area:
            a, b = area.split("-")
            sorted_arr.append([int(a), int(b)])
        else:
            sorted_arr.append([int(area)])
    for i in range(len(sorted_arr)):
        tmp = sorted_arr[i]
        if len(tmp) == 1:
            if tmp[0] == target:
                sorted_arr = sorted_arr[:i] + sorted_arr[i + 1:]
                break
        else:
            a, b = tmp
            if a == target:
                sorted_arr[i] = [target + 1, b]
                break
            elif b == target:
                sorted_arr[i] = [a, target - 1]
                break
            elif a < target < b:
                sorted_arr[i] = [a, target - 1]
                sorted_arr.append([target + 1, b])
                break
            else:
                continue
    sorted_arr.sort()
    res = ""
    for vlan in sorted_arr:
        if len(vlan) == 1:
            res += str(vlan[0]) + ","
        else:
            a, b = vlan
            res += f"{a}-{b}" + ","

    if res[-1] == ",":
        res = res[:-1]
    return res


# 5、按身高和体重排队
def solution4(height, weight):
    pass


# 6、按索引范围翻转文章片段


# 7、报数游戏
# TODO 重点题目
def solution7(m):
    if m <= 1 or m >= 100:
        return "ERROR!"

    array = [i + 1 for i in range(100)]

    # 每次前进m
    index = m - 1
    while len(array) >= m:
        # 直接删除目标值
        cur = array[index]
        array.remove(cur)
        # 重新修正索引
        index += m - 1
        # 根据当前数组长度修改索引
        index %= (len(array))

    return ",".join(list(map(str, array)))


# 8、比赛
# 排序


# 9、查找接口成功率最优时间段
def solution9(avg, s):
    # 滑动窗口
    nums = list(map(int, s.split(" ")))
    n = len(nums)

    ans = []
    left, right = 0, 0
    total = 0
    max_width = 1
    while right < n:
        total += nums[right]
        width = right - left + 1
        if total / width <= avg and width == max_width:
            ans.append([left, right])
        if total / width <= avg and width > max_width:
            ans.clear()
            ans.append([left, right])
            max_width = width

        while left <= right and total / width > avg:
            # FIXME 先减值，再移动左指针
            total -= nums[left]
            left += 1
            width -= 1
        right += 1

    if not ans:
        return "NULL"
    ans.sort()
    final_str = " ".join([f"{a}-{b}" for a, b in ans])
    return final_str


# 10、查找众数及中位数

# 11、磁盘容量排序

# 12、单词接龙
def solution12(start, n, s):
    words = list(s.split(" "))
    ans = [words[start]]

    used = [False] * n
    used[start] = True

    sorted_index = [i for i in range(n)]
    sorted_index.sort(key=lambda x: (-len(words[x]), words[x]))

    while True:
        isRun = False
        for index in sorted_index:
            if used[index]:
                continue
            w = words[index]
            if w[0] == ans[-1][-1]:
                isRun = True
                ans.append(w)
                used[index] = True
                break
        if not isRun:
            break
    return "".join(ans)


# 12、第k个排列
# TODO 重点 ==》 相似题目整理
def solution12_2(n, k):
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
        # 选中数字，并从原数组中删除
        target = array[index]
        array.remove(target)
        ans.append(str(target))

        k -= index * factorial(cnt)
        cnt -= 1

    return "".join(ans)


# 13、斗地主之顺子


# 14、非严格递增连续数字序列
def solution14(s):
    n = len(s)
    dp = [0] * n

    for i, c in enumerate(s):
        if not str(c).isdigit():
            continue
        cur = int(c)
        pre = cur + 1
        if i >= 1 and str(s[i - 1]).isdigit():
            pre = int(s[i - 1])

        if cur >= pre:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

    return max(dp)


# 14、分班
# TODO 经典题目
def solution14_2(s):
    pass


# 15、分糖果
# TODO 经典题目： 递归
def solution15(n):
    ans = float("inf")

    def dfs(cnt, depth):
        nonlocal ans
        if cnt == 1:
            ans = min(ans, depth)
            return
        if depth >= ans:
            return

        if cnt % 2 == 0:
            dfs(cnt // 2, depth + 1)
        else:
            dfs(cnt + 1, depth + 1)
            dfs(cnt - 1, depth + 1)

    dfs(n, 0)

    return ans


def solution15_2(n):
    def dfs(cnt, depth):
        if cnt == 1:
            return depth

        if cnt % 2 == 0:
            return dfs(cnt // 2, depth + 1)
        return min(dfs(cnt + 1, depth + 1), dfs(cnt - 1, depth + 1))

    return dfs(n, 0)


# 15、高矮个子排队
# 贪心思想：遍历奇数位置，当不满足>=两侧数值时，取两者中较大的值
def solution15_3(s):
    array = list(map(int, s.split(" ")))
    n = len(array)
    for i in range(n):
        if i % 2 == 0:
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        else:
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]


# 16、工号不够用了怎么办？


# 17、勾股数元组

# 18、喊7的次数重排

# 19、猴子爬山
# TODO 经典：动态规划
def solution19(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        if i >= 3:
            dp[i] += dp[i - 3]

    return dp[n]


# 20、滑动窗口最大和
# TODO 前缀和 + 滑动窗口

# 21、火星文计算
# TODO 递归函数设计
def solution21(s):
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


# 22、计算面积

# 23、计算最大乘积
# TODO 二进制表达


# 24、检查是否存在满足条件的数字组合
def solution24(s):
    array = [int(c) for c in s.split(" ")]
    array.sort(reverse=True)

    n = len(array)

    for i in range(n - 2):
        if i > 0 and array[i - 1] == array[i]:
            continue
        num1 = array[i]
        for j in range(i + 1, n - 1):
            if j > i + 1 and array[j - 1] == array[j]:
                continue
            num2 = array[j]
            for k in range(j + 1, n):
                num3 = array[k]
                if num1 == (num2 + 2 * num3):
                    return f"{num1} {num2} {num3}"

    return "0"


# 25、矩阵扩散
# TODO 多源广度优先搜索
def solution25(m, n, pos1, pos2):
    x1, y1 = pos1.split(" ")
    x2, y2 = pos2.split(" ")

    mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    matrix = [[0 for _ in range(n)] for _ in range(m)]
    sk = [(int(x1), int(y1)), (int(x2), int(y2))]
    for x, y in sk:
        matrix[x][y] = 1

    time = 0
    while sk:
        tmp = []
        # FIXME 最后一轮空扫描，不需要增加时间
        isAdd = False
        for x, y in sk:
            for mx, my in mov:
                nx = x + mx
                ny = y + my
                if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] == 1:
                    continue
                matrix[nx][ny] = 1
                tmp.append((nx, ny))
                isAdd = True

        time += isAdd
        sk = tmp
    return time


# 26、矩阵最大值
# 每个二进制，考虑所有1位置作为开头的情况，取最大值
def solution26(m, n, pos1, pos2):
    pass


# 27、考勤信息

# 28、靠谱的车

# 29、快递运输
# 贪心

# 30、连续字母长度


# 31、两数之和绝对值最小
"""
排序后，嵌套遍历
"""


# 32、流水线
# TODO 贪心思想
def solution32(m, n, s):
    cost = list(map(int, s.split(" ")))
    cost.sort()

    task = [0 for _ in range(m)]
    for i in range(n):
        index = i % m
        task[index] += cost[i]

    return max(task)


# 33、乱序整数序列两数之和绝对值最小
# TODO 需要更好的算法
"""
构建索引数组，然后根据原数值进行升序排列，
嵌套遍历计算绝对值，记录最小值，并用于剪枝
"""


# 34、内存资源分配
def solution34(source: str, need: str):
    need_array = list(map(int, str(need).split(",")))
    data = []
    for info in source.split(","):
        vol, cnt = info.split(":")
        data.append([int(vol), int(cnt)])
    data.sort()

    ans = []

    for req in need_array:
        if not data:
            ans.append(False)
        elif req > data[-1][0]:
            ans.append(False)
        else:
            # 可以使用二分法查询
            left = 0
            right = len(data) - 1
            target = -1
            while left <= right:
                mid = (left + right) // 2
                if data[mid][0] >= req:
                    target = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if target == -1:
                ans.append(False)
                continue
            ans.append(True)

            data[target][1] -= 1
            if data[target][1] == 0:
                data = data[:target] + data[target + 1:]
    return ans


# 35、判断一组不等式是否满足约束并输出最大差


# 36、判断字符串子序列
# TODO　双指针遍历 、 动态规划

def solution36(target, source):
    target = target[::-1]
    source = source[::-1]

    n = len(source)
    m = len(target)
    for i, c in enumerate(source):
        if c != target[0]:
            continue
        right = 1
        for j in range(i + 1, n):
            if source[j] == target[right]:
                right += 1
            if right >= m:
                return n - 1 - j
    return -1


if __name__ == '__main__':
    # print(solution1("111"))
    # print(solution1("1 1 5 1 5 2 4 4"))

    # print(int("17", 8))
    # print(int("a7", 17))
    # print(solution2(8, "07", "1"))
    # print(solution2(2, "11", "1"))

    # print(solution4("20-21,15,18,30,5-10", 15))
    # print(solution4("5,1-3", 10))

    # print(solution7(3))
    # print(solution7(4))
    #
    # print(solution9(1, "0 1 2 3 4"))
    # print(solution9(2, "0 0 100 2 2 99 0 2"))
    #
    # print(solution12(0, 6, "word dd da dc dword d"))
    #
    # print(solution12_2(3, 3))
    #
    # print(solution14("abc2234019A334bc"))
    #
    # print(solution15(15))
    # print(solution15_2(15))

    print(solution34("64:2,128:1,32:4,1:128", "50,36,64,128,127"))
    print(solution34("64:2,128:1,32:4,1:128", "50,36,64,128,127"))

    print(solution25(4, 4, "0 0", "3 3"))

    print(solution24("2 7 3 0"))
    print(solution24("1 1 1"))

    print(solution21("7#6$5#12"))

    print(solution19(50))
    pass
