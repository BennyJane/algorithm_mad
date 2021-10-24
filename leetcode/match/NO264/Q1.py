class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = []

        def check(s: str) -> bool:
            count = 0
            n = len(s)
            for i, c in enumerate(s):
                if c.isdigit():
                    return False
                if i == 0 or i == n - 1:
                    if c == "-":
                        return False
                if c in ["!", ".", ","]:
                    if i != n - 1:
                        return False
                if c == '-':
                    if not s[i - 1].isalpha() or not s[i + 1].isalpha():
                        return False
                    count += 1

            return count <= 1

        for word in sentence.split(" "):
            word = word.strip()
            if len(word) > 0 and check(word):
                ans.append(word)
                print(word)
        return len(ans)


if __name__ == '__main__':
    sol = Solution()
    s = " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
    # sol.countValidWords(s)

    print("!".isalpha())
    print("s".isalpha())
    print("!".isalnum())
