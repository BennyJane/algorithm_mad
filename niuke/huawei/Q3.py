"""
---------------------------------------------------------------------------
字符串专题
---------------------------------------------------------------------------
"""

# 37、拼接URL
from functools import cmp_to_key


def solution37():
    pass


# 38、求符合要求的结对方式
# TODO 组合数量：去重
# 暴力遍历、
def solution37():
    pass


# 39、求解连续数列
def solution39(s, n):
    diff = sum([i for i in range(n)])

    min_sum = s - diff
    if min_sum < 0 or min_sum % n != 0:
        return -1
    left = min_sum // n

    res = [str(left + i) for i in range(n)]

    return " ".join(res)


# 40、求字符串中所有整数的最小和
# TODO: 正数分离为单个数字，负数尽可能连接起来
def solution40(s):
    n = len(s)

    ans = 0
    left = 0

    neg = 1
    while left < n:
        c = s[left]
        if c != '-' and not ('0' <= c <= '9'):
            left += 1
            continue

        if c == '-':
            neg = -1
            left += 1
        cur = 0
        while left < n and '0' <= s[left] <= '9':
            if neg > 0:
                cur += int(s[left])
            else:
                cur = cur * 10 + int(s[left])
            left += 1
        ans += neg * cur
        neg = 1

    return ans


# 41、求最多可以派出多少支团队
# TODO 双指针
def solution41(s, val):
    array = [int(c) for c in s.split(" ")]
    array.sort()
    n = len(array)

    ans = 0

    left, right = 0, n - 1

    while left < right:
        if array[right] >= val:
            ans += 1
            right -= 1
            continue
        cur = array[left] + array[right]
        if cur >= val:
            left += 1
            right -= 1
            ans += 1
        else:
            left += 1
    if array[left] >= val:
        ans += 1
    return ans


# 42、删除字符串中字符最少字符

# 43、数据分类
# TODO 二进制操作：int类型每四个字节当做一个新值： num % 256 (2**8)

# 44、数列描述
# TODO 模拟法
def solution44(n):
    raw = [""] * (n + 1)
    raw[0] = "1"

    for i in range(1, n + 1):
        last = raw[i - 1]

        pre = "0"
        index = 0
        cnt = 0

        tmp = ""
        while index < len(last):
            c = last[index]
            if c == pre:
                cnt += 1
            else:
                if cnt > 0:
                    tmp += f"{cnt}{pre}"
                cnt = 1
                pre = c
            index += 1

        if cnt > 0:
            tmp += f"{cnt}{pre}"

        raw[i] = tmp
    return raw[n]


# 45、数字涂色
# 数组 + 标记数组，排序后从最小值开始，每次需要将其整数倍数且存在的数字标记为已经涂色

# 46、数组二叉树
# TODO 递归
def solution46(s):
    array = [0]
    for c in s.split(" "):
        array.append(int(c))

    n = len(array)

    ans = [float("inf")]

    def dfs(index, res):
        nonlocal ans
        cur = array[index] if index < n else -1

        # 判断是否到达叶子节点
        if cur == -1:
            if ans[-1] > res[-1]:
                ans = list(res)
            return

        res.append(cur)
        dfs(index * 2, res)
        dfs(index * 2 + 1, res)
        # FIXME 需要弹出该元素
        res.pop()

    dfs(1, [])

    return " ".join([str(c) for c in ans])


# 47、数组拼接

# 48、数组去重和排序


# 49、数组组成的最小数字
# TODO 数字重组：字典序重排
def solution49(s):
    array = [c for c in s.split(",")]

    # FIXME 需要先根据长度排序，只取前三个字符串，再进行下一轮排序
    array.sort(key=lambda x: len(x))

    from functools import cmp_to_key
    def compare(a, b):
        # 长度优先：尽量降低位数
        return int(a + b) - int(b + a)

    select = sorted(array[:3], key=cmp_to_key(compare))

    ans = "".join(select)
    return ans


# 179. 最大数
def solution49_1(s):
    # 使用字符串
    array = [c for c in s.split(",")]
    from functools import cmp_to_key

    # 第一步：定义比较函数，把最大的放左边
    # 第二步：排序
    # 第三步：返回结果
    def compare(x, y): return int(y + x) - int(x + y)

    nums = sorted(map(str, array), key=cmp_to_key(compare))
    return "0" if nums[0] == "0" else "".join(nums)


"""
public String getMinNumber(int[] numbers) {
	if (numbers == null || numbers.length == 0) return "";
	int len = numbers.length;
	String[] str = new String[len];
	for (int i = 0; i< len;i++) {
		// 转化为字符串数组，以便排序，直接使用 int 数组排序的话无法达到 高数位尽量小的要求
		str[i] = String.valueOf(numbers[i]); 
    }
    Arrays.sort(str,new Comparator<String>(){ //字符串数组排序，重写排序规则
			@Override
            public int compare(String s1, String s2) {
				String a = s1 + s2;
				String b = s2 + s1;
				return a.compareTo(b); // 从小到大排序
				// return c2.compareTo(c1);// 从大到小排序
			}
	});
 	StringBuilder sb = new StringBuilder();
 	for (int i = 0; i < len; i++) {
    	sb.append(str[i]);
    }
    return sb.toString();
}


"""


# 50、水仙花数
# TODO 模拟法
def solution50(n, m):
    if not (3 <= n <= 7):
        return -1
    start = 10 ** (n - 1)
    end = 10 ** n

    for c in range(start, end):
        total = 0
        tmp = c
        while tmp > 0:
            tail = tmp % 10
            total += tail ** n
            tmp //= 10
        if total == c:
            m -= 1
        if m == -1:
            return total

    return -1


if __name__ == '__main__':
    print(solution39(525, 6))
    print(solution39(3, 5))

    print(solution40("bb1234aa"))
    print(solution40("bb12-34aa"))

    print(solution41("3 1 5 7 9", 8))

    print(solution44(4))

    print(solution46("3 5 7 -1 -1 2 4"))

    print(solution49("21,30,62,5,31"))
    print(solution49_1("21,30,62,5,31"))

    print(solution50(3, 0))
    print(solution50(9, 1))
    pass
