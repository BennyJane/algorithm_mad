from typing import List


class Solution1:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            ans = max(ans, len(s.split(" ")))
        return ans


class Solution2:
    # 互相包含
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        visited = [False] * n

        supplies = set(supplies)

        for i in range(n):
            ing = ingredients[i]
            canMake = True
            for c in ing:
                if c not in supplies:
                    canMake = False
                    break
            if canMake:
                visited[i] = True
                supplies.add(recipes[i])
        while not all(visited):
            isChange = False
            for i in range(n):
                if visited[i]:
                    continue
                ing = ingredients[i]
                canMake = True
                for c in ing:
                    if c not in supplies:
                        canMake = False
                        break
                if canMake:
                    visited[i] = True
                    supplies.add(recipes[i])
            if not isChange:
                break
        ans = []
        for i, t in enumerate(visited):
            if t:
                ans.append(recipes[i])
        return ans


class Solution3:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        minCount = maxCount = 0
        for i in range(n):
            c = s[i]
            num = locked[i]
            if c == "(":
                if num == "0":
                    minCount = max(minCount - 1, 0)
                else:
                    minCount += 1
                maxCount += 1
            else:  # 右括号
                minCount = max(minCount - 1, 0)
                if num == "0":
                    maxCount += 1
                else:
                    maxCount -= 1
                    if maxCount < 0:
                        return False
        return minCount == 0


class Solution4:
    def abbreviateProduct(self, left: int, right: int) -> str:
        # 统计2与5的数量
        two = five = 0
        for i in range(left, right + 1):
            j = i
            while j % 2 == 0:
                j //= 2
                two += 1
            j = i
            while j % 5 == 0:
                j //= 5
                five += 1
        # 统计 2 5因子个数，计算末尾0的个数
        two = five = MIN = min(two, five)

        flag = 0
        # 计算前5 与 后5位置的数字
        first = last = 1
        TEN_LIMIT = 10000000000
        FIVE_LIMIT = 100000
        for i in range(left, right + 1):
            last *= i
            # last 除以2 5；需要整除，去掉小数
            while last % 2 == 0 and two > 0:
                last //= 2
                two -= 1
            while last % 5 == 0 and five > 0:
                five -= 1
                last //= 5
            if last > TEN_LIMIT:
                flag = 1
                last %= TEN_LIMIT
            first *= i
            while first > FIVE_LIMIT:
                # FIXME 需要保留小数； 精度还是会出问题
                first /= 10
        if flag == 0:
            return "{}e{}".format(int(last), MIN)
        return "{}...{}e{}".format(int(first), "%05d" % (last % FIVE_LIMIT), MIN)


if __name__ == '__main__':
    # sol = Solution3()
    # s = "))()))"
    # l = "010100"
    # sol.canBeValid(s, l)

    print("%05d" % 2)
