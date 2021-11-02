import logging
from typing import List
from logging import DEBUG
from collections import defaultdict
from sortedcontainers import SortedList

logger = logging.getLogger()
logger.setLevel(DEBUG)
"""
--------------------------------------
有序队列：SortedList 保证内部数据有序性
Java内使用TreeMap
--------------------------------------
"""


def sortedListFunc():
    # 实例化
    l = SortedList([0, 1, 2, 3, 4])
    sorted_list = SortedList()
    # 添加元素
    sorted_list.add(1)
    sorted_list.add(1)
    sorted_list.add(5)
    sorted_list.add(5)
    sorted_list.add(4)
    sorted_list.add(3)
    print(sorted_list)
    # 获取长度
    print(len(sorted_list))
    # 获取元素索引
    index = sorted_list.index(5)
    print(index)
    # 没有实现append方法
    # sorted_list.append(0)
    # 计算元素是数量
    count = sorted_list.count(5)
    print(count)
    # 删除索引对应的值
    sorted_list.pop(0)
    print(sorted_list)
    # 删除元素
    sorted_list.discard(1)
    print(sorted_list)
    # 删除元素：没有会抛出错误
    sorted_list.remove(3)
    # extend 该方法未实现
    # sorted_list.extend([7, 8, 9])
    print(sorted_list)
    # insert 未实现
    # sorted_list.insert(0, 10)


"""
--------------------------------------
默认字段：设置字典的默认值 defaultdict
--------------------------------------
"""


def defaultdictFunc():
    d = defaultdict(int)
    l: List[int] = list()
    print(d)


def headqFunc():
    pass


if __name__ == '__main__':
    logging.info("---- demo1 ---")
    sortedListFunc()
    logging.info("---- demo2 ---")
    defaultdictFunc()
