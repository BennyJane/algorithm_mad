class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        limit = 10 ** 32

        def check(num: int) -> bool:
            s = str(num)
            d = dict()
            for c in s:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
            for k, v in d.items():
                if int(k) != v:
                    return False
            return True

        for i in range(n + 1, limit):
            if check(i):
                return i

        return 0

if __name__ == '__main__':
    sol =Solution()
    sol.nextBeautifulNumber(10 ** 6)