from collections import defaultdict, Counter
from typing import List


class Solution1:
    # 451. 根据字符出现频率排序
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        # FIXME 需要升序排列
        array = sorted(d.items(), key=lambda x: -1 * x[1])
        ans = ""
        for c, cnt in array:
            ans += c * cnt
        return ans

    # 桶排序
    def frequencySort2(self, s: str) -> str:
        d = defaultdict(int)
        maxFreq = 0
        for c in s:
            d[c] += 1
            maxFreq = max(maxFreq, d[c])

        # 每个桶存储 指定频率的字符，可能存在相等的情况
        buckets = ["" for _ in range(maxFreq + 1)]
        for c, cnt in d.items():
            # 同频率字符，不分先后顺序，一次性拼接
            buckets[cnt] += c * cnt
        ans = ""
        for b in buckets:
            ans = b + ans
        return ans


# 347. 前 K 个高频元素
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        maxFreq = 0
        for n in nums:
            d[n] += 1
            maxFreq = max(maxFreq, d[n])

        buckets = [[] for _ in range((maxFreq + 1))]
        for n, cnt in d.items():
            buckets[cnt].append(n)

        ans = list()
        freq = len(buckets) - 1
        while k > 0:
            temp = buckets[freq]
            ans.extend(temp)
            k -= len(temp)
            freq -= 1

        return ans

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        ans = map.most_common(k)
        return [item[0] for item in ans]
