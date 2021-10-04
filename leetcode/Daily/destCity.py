from typing import List


# 1436. 旅行终点站
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = ""
        for s, _ in paths:
            start.add(s)
        for _, e in paths:
            if e not in start:
                end = e
        return end

    # 不如两次遍历来的快
    def destCity2(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for s, e in paths:
            start.add(s)
            end.add(s)
            if s in end:
                end.remove(s)
            if e in start:
                end.remove(e)
        return end


class Solution2:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)

    # 哈希表
    def destCity2(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)

