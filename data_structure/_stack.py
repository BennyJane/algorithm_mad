# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

class StackBase:
    def __init__(self):
        """使用列表模拟栈：列表左侧为栈底部， 右侧未栈顶部"""
        self.items = []

    def isEmpty(self):
        """判断栈是否为空"""
        return self.items == []

    def push(self, item):
        """向栈顶添加元素"""
        self.items.append(item)

    def pop(self):
        """弹出栈顶元素，删除该元素"""
        return self.items.pop()  # 默认弹出列表末尾的数据，空列表为报错

    def peek(self):
        """查看栈顶元素，不删除"""
        return self.items[-1]

    def size(self):
        """返回栈的长度"""
        return len(self.items)
