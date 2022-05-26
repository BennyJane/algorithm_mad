import collections
from typing import List


#  082. 含有重复元素集合的组合
class Solution1:
    # 基础操作： 排序(去重)  + 回溯， 依然超时
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排除极端情况
        if sum(candidates) < target:
            return []
        candidates.sort()
        n = len(candidates)
        # 利用set与排序法，去重，并没有降低递归的次数，且红黑树效率比较低
        ans = set()

        def dfs(index, retain, arr):
            if retain == 0:
                ans.add(tuple(arr))
                return
            if index >= n:
                if retain == 0:
                    ans.add(tuple(arr))
                return
            for i in range(index, n):
                cur = candidates[i]
                if retain < cur:
                    break
                dfs(i + 1, retain, list(arr))
                arr.append(candidates[i])
                dfs(i + 1, retain - candidates[i], arr)
                arr.pop()

        dfs(0, target, list())
        res = []
        for t in ans:
            res.append(list(t))
        return res

    # https://leetcode-cn.com/problems/combination-sum-ii/comments/
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排除极端情况
        if sum(candidates) < target:
            return []
        # 必须排序，使得相同元素相邻
        candidates.sort()
        n = len(candidates)
        ans = list()

        # 根据递归深度，考虑可选择的数组中数字的所有情况
        # 第1次时可选范围为[0, n)；当第1次选择索引为index时，第2次可选范围为[index, n)....
        def dfs(index, retain, arr):
            if retain == 0:
                ans.append(list(arr))
                return
            # 不需要判断index >= n退出；因为当index >= n时，下面循环直接跳过
            for i in range(index, n):
                cur = candidates[i]
                # 剪枝：后续数字全部 > cur时，直接退出
                if retain < cur:
                    break
                # TODO 跳过重复元素： 三元，四元之和的题目
                if i > index and candidates[i] == candidates[i - 1]:
                    # 注意：比较对象时 i 与 index
                    continue
                # 回溯核心
                arr.append(candidates[i])
                # 下一次递归讨论范围缩小
                dfs(i + 1, retain - candidates[i], arr)
                arr.pop()

        dfs(0, target, list())
        return ans

    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            # 恰好和为target
            if rest == 0:
                ans.append(sequence[:])
                return
            # 遍历到末尾 or 剩余数字全部大于 剩余和
            if pos == len(freq) or rest < freq[pos][0]:
                return

            # 当前数字不选择，因为只能使用一次，需要跳过当前数字
            dfs(pos + 1, rest)

            # 重复元素：计算最大使用数量
            most = min(rest // freq[pos][0], freq[pos][1])
            # 讨论重复数字使用[1, most]的所有可能新
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                # pos +1： 跳过当前数字，避免重复讨论
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        # 统计重复数字的频率，并升序排列
        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans


# 104. 排列的数目
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 1:
            return 0
        nums.sort()
        if nums[0] > target:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            # 考虑每个值的最后一个累加值的所有可能
            for j in range(n):
                cur = nums[j]
                if i >= cur:
                    dp[i] += dp[i - cur]

        return dp[target]


# 51.N皇后
class Solution3:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                # 回溯思想： 先设值，再复原
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backTrack(rowIndex: int):
            if rowIndex == n:
                board = generateBoard()
                ans.append(board)
                return

            # 枚举列索引
            for i in range(n):
                if i in columns or rowIndex - i in diagonal1 or rowIndex + i in diagonal2:
                    continue
                # queens不需要复原，同rowIndex的不同情况会覆盖该值
                queens[rowIndex] = i
                # 回溯核心： 标记已占领位置
                columns.add(i)
                diagonal1.add(rowIndex - i)
                diagonal2.add(rowIndex + i)
                backTrack(rowIndex + 1)
                # 回溯核心： 解除标记
                columns.remove(i)
                diagonal1.remove(rowIndex - i)
                diagonal2.remove(rowIndex + i)

        ans = list()
        # 记录每列放置的王后
        columns = set()
        # 记录从左上角到右下角 且 已经被王后占领的斜线
        # 特征：行索引 - 列索引 = 固定值
        diagonal1 = set()
        # 记录从左下角到右上角 且 已经被王后占领的斜线
        # 特征：行索引 + 列索引 = 固定值
        diagonal2 = set()
        # 根据王后特征： 所有王后必然分布在不同的行、不同的列
        # queens记录每行Q的索引位置
        queens = [-1] * n
        row = ["."] * n
        backTrack(0)
        return ans

    def solveNQueens2(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions


# 52.N皇后II
class Solution4:
    def totalNQueens(self, n: int) -> int:
        def dfs(r, columns, diagonals1, diagonals2):
            if r == n: return 1
            cnt = 0
            availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
            while availablePositions:
                position = availablePositions & (-availablePositions)
                availablePositions = availablePositions & (availablePositions - 1)
                cnt += dfs(r + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)
            return cnt

        return dfs(0, 0, 0)


res = (1 << 8) - 1
print(bin(res))
print(bin(1 << 8))
print(1 << 8)
print((1 << 8) - 1)


# 47.全排列II
class Solution5:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 必须排序，利用相等数值相邻的特性，排除重复组合
        nums.sort()

        # 标记数组
        visited = [False] * n

        def dfs(index, arr):
            """
            :param index: 记录递归深度，即已经选择的元素个数； 可以不使用，直接使用len(arr)代替
            :param arr:
            """
            if index >= n:
                ans.append(list(arr))
                return
            # 每次需要遍历所有元素，
            for i in range(n):  # 错误表达： range(index, n)， index 前面存在未选择的对象
                if visited[i]:
                    continue
                # FIXME 核心：选择第index元素时，重复元素，只需要选择一次
                # 需要保证两个元素相等，且前一个元素已经被选择过
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                visited[i] = True
                dfs(index + 1, list(arr))
                arr.pop()
                visited[i] = False

        ans = []
        dfs(0, list())
        return ans

    # 使用集合特性去重
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        array = set()
        visited = [False] * n

        def dfs(tmp):
            if len(tmp) == n:
                # 数组 =》 元组，去重
                array.add(tuple(tmp))
                return
            for i in range(n):
                if visited[i]:
                    continue
                tmp.append(nums[i])
                visited[i] = True
                dfs(list(tmp))
                tmp.pop()
                visited[i] = False

        dfs(list())
        return [list(t) for t in array]


class Solution6:
    def combine(self, n, k):
        ans = list()

        def dfs(index, tmp):
            # 剪枝： 后续元素全部选择，长度也无法达到k的长度
            if len(tmp) + n - index + 1 < k:
                ans.append(list(tmp))
                return
            # 长度满足条件
            if len(tmp) == k:
                ans.append(list(tmp))
                return
                # index 之前的元素不需要再考虑
            for i in range(index, n + 1):
                # 情况1：不选择当前元素
                dfs(index + 1, tmp)
                # 情况2：选择当前元素
                tmp.append(i)
                dfs(index + 1, tmp)
                tmp.pop()

        dfs(1, list())
        return ans

    # FIXME 使用标记数组，for循环内只处理一个递归调用； 错误原因：[1, 2] [2, 1] 被同时包含在内
    def combine2(self, n, k):
        visited = [False] * n
        ans = list()

        def dfs(tmp):
            if len(tmp) == k:
                ans.append(list(tmp))
                return
            for i in range(1, n + 1):
                if visited[i - 1]:
                    continue
                tmp.append(i)
                visited[i - 1] = True
                dfs(tmp)
                visited[i - 1] = False
                tmp.pop()

        dfs(list())
        return ans
