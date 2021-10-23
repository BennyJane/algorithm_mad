from typing import List
from ipaddress import ip_address, IPv6Address

"""
# 93. 复原 IP 地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# TODO 广度优先算法
class Solution:
    ans = None

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = set()
        self.dfs(s, 0, "")
        return list(self.ans)

    def dfs(self, s: str, left: int, pre: str):
        if left >= len(s):
            if pre.count(".") == 3:
                self.ans.add(pre)
            return
        if pre.count(".") > 3:
            return
        if s[left] == "0":
            temp = pre + "." + s[left] if pre else s[left]
            self.dfs(s, left + 1, temp)
            return
        # 只需要考虑长度在3范围内的情况
        for i in range(1, 4):
            cur = s[left: left + i]
            if int(cur) > 255:
                continue
            temp = pre + "." + cur if pre else cur
            self.dfs(s, left + i, temp)


"""
751. IP 到 CIDR
给定一个起始 IP 地址 ip 和一个我们需要包含的 IP 的数量 n，返回用列表（最小可能的长度）表示的 CIDR块的范围。 

CIDR 块是包含 IP 的字符串，后接斜杠和固定长度。例如：“123.45.67.89/20”。固定长度 “20” 表示在特定的范围中公共前缀位的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ip-to-cidr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution2(object):
    def ipToInt(self, ip):
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
        return ans

    def intToIP(self, x):
        return ".".join(str((x >> i) % 256)
                        for i in (24, 16, 8, 0))

    def ipToCIDR(self, ip, n):
        start = self.ipToInt(ip)
        ans = []
        while n:
            mask = max(33 - (start & -start).bit_length(),
                       33 - n.bit_length())
            ans.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans


"""
468. 验证IP地址
编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

如果是有效的 IPv4 地址，返回 "IPv4" ；
如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。
IPv4 地址由十进制数和点来表示，每个地址包含 4 个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由 8 组 16 进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-ip-address
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution3:
    def validIPAddress(self, IP: str) -> str:
        ans = "Neither"
        if "." in IP:
            ans = self.isIPV4(IP)
        if ":" in IP:
            ans = self.isIPV6(IP)
        return ans

    def isIPV4(self, target: str):
        res = "Neither"
        arr = target.split(".")
        if len(arr) != 4:
            return res
        for s in arr:
            if not s:
                return res
            if len(s) > 1 and s[0] == "0":
                return res
            try:
                if int(s) > 255:
                    return res
            except Exception as e:
                return res
        return "IPv4"

    def isIPV6(self, target: str):
        res = "Neither"
        arr = target.split(".")
        if len(arr) != 8:
            return res
        for s in arr:
            if len(s) > 4 or len(s) == 0:
                return res
            # TODO 需要验证十六进制是否正确
            try:
                int(s, 16)
            except Exception as e:
                return res

        return "IPv6"

    # TODO 使用PY JAVA 内置检测函数
    def validIPAddress2(self, IP: str) -> str:
        try:
            if type(ip_address(IP)) is IPv6Address:
                return "IPv6"
            else:
                return "IPv4"
        except ValueError:
            return "Neither"


import re


class Solution3_1:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')

    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            return "IPv4" if self.patten_IPv4.match(IP) else "Neither"
        if ':' in IP:
            return "IPv6" if self.patten_IPv6.match(IP) else "Neither"
        return "Neither"


class Solution3_2:
    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"

    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"


if __name__ == '__main__':
    sol = Solution()
    # sol.restoreIpAddresses("25525511135")
    sol.restoreIpAddresses("101023")
