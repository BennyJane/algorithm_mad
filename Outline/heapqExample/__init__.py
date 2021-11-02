import heapq
import itertools
from itertools import chain
from heapq import *

# heapq 常见用法
"""
python官方文章
https://docs.python.org/zh-cn/3/library/heapq.html


heapq默认创建小跟堆
使用数组来实现，从0开始计数，对于所有索引i，都有 heap[i] <= heap[2 * i +1] and heap[i] <= heap[2 * k +2]
为了便于比较，不存在的元素被认为是无限大
堆最有趣的特性在于最小的元素总是在根结点：heap[0
"""

"""
-----------------------------------------------------------------------------------------
基础用法
-----------------------------------------------------------------------------------------
"""
# 创建堆
l = [1, 245, 32, 4, 24, 6, 2]
# heapify() 将list转化为堆
# 原地转化，线性时间范围内
heapq.heapify(l)
print(l)

min_value = heapq.heappop(l)
print(min_value)
heapq.heappush(l, 100)
print(l)
# 先插入item，然后再弹出heap的最小元素； 该操作比heappush  heappop 结合起来效率更高
heapq.heappushpop(l, 3)
print(l)
# 先弹出最小元素，然后再插入item； 堆的大小不变，如果堆为空，则抛出IndexError异常
# 该方法比 heappop + heappush 更高效，尤其适用于固定大小的堆
# FIXME 该方法返回值可能比插入item更大，即不能保证返回值是包含item在内的最小值 ==》 对比 heappushpop
heapq.heapreplace(l, 200)

"""
-----------------------------------------------------------------------------------------
基于堆的通用功能
merge
nlargest
nsmallest
-----------------------------------------------------------------------------------------
"""
l2 = [i for i in range(10, 20)]
l3 = [i for i in range(21, 30)]
l4 = [1, 2, 3, 5, 30, 31, 32, 35]
# merge 合并多个已经排序的列表(可迭代对象)，并返回一个迭代器
# 合并结果：默认为升序, 要求输入序列，也必须是升序，否则返回结果无序
iter_res = heapq.merge(l3, l2, l4)
# 调用方法： next(iter_res)
list_res = list(iter_res)
print(list_res, len(list_res))
# 要求输入序列为降序
iter_res = heapq.merge(sorted(l2, reverse=True),
                       sorted(l3, reverse=True),
                       sorted(l4, reverse=True),
                       key=lambda x: x, reverse=True)
print(list(iter_res))

# 相似方法

list_res = sorted(chain(l2, l3, l4), key=lambda x: x)
print(list_res)

# 返回前n个最大元素组成的列表
# TODO 当n较小时，性能最好，但n==1时，使用max min函数，更高效
topK = heapq.nlargest(5, l2, key=lambda x: x)
print(topK)

botK = heapq.nsmallest(5, l2, key=lambda x: x)
print(botK)

"""
-----------------------------------------------------------------------------------------
官方实例: 
堆排序
优先队列
    优先队列 是堆的常用场合，并且它的实现包含了多个挑战：
        排序稳定性：你该如何令相同优先级的两个任务按它们最初被加入时的顺序返回？
        如果优先级相同且任务没有默认比较顺序，则 (priority, task) 对的元组比较将会中断。
        如果任务优先级发生改变，你该如何将其移至堆中的新位置？
        或者如果一个挂起的任务需要被删除，你该如何找到它并将其移出队列？
-----------------------------------------------------------------------------------------
"""


# 堆排序
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

# 堆元素为元组：支持多种条件比较排序
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
heappop(h)

"""
-----------------------------------------------------------------------------------------
优先队列
-----------------------------------------------------------------------------------------
"""
from dataclasses import dataclass, field
from typing import Any


# 忽略任务条目并且只比较优先级字段的包装器类
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


# 移除条目或改变其优先级的操作实现起来更为困难，因为它会破坏堆结构不变量。
# 因此，一种可能的解决方案是将条目标记为已移除，再添加一个改变了优先级的新条
pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
