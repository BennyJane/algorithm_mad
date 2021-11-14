class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        col = n // rows
        ans = ""
        for c in range(col):
            x, y = 0, c
            for r in range(rows):
                X, Y = x + 1 * r, y + 1 * r
                pos = X * col + Y
                if pos < n:
                    ans += encodedText[pos]
        length = len(ans)
        tail = length
        for i in range(length - 1, -1, 1):
            if ans[i] != " ":
                break
            tail = i
        ans = ans[:tail]
        return ans


if __name__ == '__main__':
    sol = Solution()
    # end = "ch   ie   pr"
    # k = 3

    end = "iveo    eed   l te   olc"
    k = 4
    sol.decodeCiphertext(end, k)
