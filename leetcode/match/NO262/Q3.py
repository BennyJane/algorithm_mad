# FIXME 超时
from heapq import heappop, heappush


class StockPrice1:

    def __init__(self):
        self.last_time = None
        self.time_list = []
        self.price_list = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_list:
            index = self.time_list.index(timestamp)
            self.price_list[index] = price
        else:
            self.time_list.append(timestamp)
            self.price_list.append(price)

        if self.last_time is None:
            self.last_time = timestamp
        else:
            if timestamp > self.last_time:
                self.last_time = timestamp

    def current(self) -> int:
        return self.price_list[self.time_list.index(self.last_time)]

    def maximum(self) -> int:
        return max(self.price_list)

    def minimum(self) -> int:
        return min(self.price_list)


from sortedcontainers import SortedList
from collections import defaultdict


# TODO 使用两个优先队列
# TODO 有序集合： Multiset/SortedList/HashHeap
class StockPrice:

    def __init__(self):
        self.cur_time = 0
        self.stock_record = defaultdict(int)
        self.prices_set = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        self.cur_time = max(self.cur_time, timestamp)
        # 如果存在，先将该时间对应的旧值删除
        self.prices_set.discard(self.stock_record[timestamp])
        self.prices_set.add(price)
        self.stock_record[timestamp] = price

    def current(self) -> int:
        return self.stock_record[self.cur_time]

    def maximum(self) -> int:
        return self.prices_set[-1]

    def minimum(self) -> int:
        return self.prices_set[0]


class StockPrice2:
    def __init__(self):
        self.maxPrice = []
        self.minPrice = []
        self.timePriceMap = {}
        self.maxTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        heappush(self.maxPrice, (-price, timestamp))
        heappush(self.minPrice, (price, timestamp))
        self.timePriceMap[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)

    def current(self) -> int:
        return self.timePriceMap[self.maxTimestamp]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxPrice[0]
            if -price == self.timePriceMap[timestamp]:
                return -price
            heappop(self.maxPrice)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minPrice[0]
            if price == self.timePriceMap[timestamp]:
                return price
            heappop(self.minPrice)
