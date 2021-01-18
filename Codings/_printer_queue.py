# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import random

"""
==================================================================================
问题描述
假设实验室里有一台打印机供学生共性。当学生向共享打印机发送打印任务时，任务被放置在队列中以便以先来先服务的方式被处理。
如何才能通过python程序模拟的方式得到每次提交任务的平均等待时间呢？（平均等待时间不包括打印本身的时间，仅指在队列中排队的时间。）

我们假定：
学生们每次打印的页数在1到20页之间。
打印机平均每小时会收到20个打印请求，即平均每180秒1个请求。
每秒新增任务的可能性相等，即任务的产生为独立同分布
打印机的打印速度恒定。

参考链接： https://www.jianshu.com/p/df116d5d103c
==================================================================================
"""

"""
任务类应包括以下几个功能：
随机生成页数、记录入队时间戳、返回需要打印的页数、根据当前时间戳返回等待的时间。
"""


class Queue:
    def __init__(self):
        """创建一个空的队列，不需要参数，并返回一个空列表"""
        self.items = []

    def add(self, item):
        """将item添加到队列末尾，无返回内容"""
        self.items.append(item)

    def pop(self):
        """从队首移除项，不需要参数，有返回值"""
        return self.items.pop(0)

    def isEmpty(self):
        """判断队列是否为空，返回布尔值"""
        return len(self.items) == 0

    def size(self):
        """返回队列长度"""
        return len(self.items)


class Task:
    def __init__(self, time):
        """任务初始化： time为传入的任务创建时间，也就是入队时间"""
        self.in_time = time
        self.pages = random.randrange(1, 21)  # 随机生成打印的页数（1-20）

    def getPage(self):
        """返回任务需要打印的页数"""
        return self.pages

    def waitTime(self, out_time):
        """out_time 为当前时间戳"""
        return out_time - self.in_time


class Printer:
    def __init__(self, timePerPage):
        """打印机初始化"""
        self.timePerPage = timePerPage  # timePerPage 为每页打印所需的时间，设定好后便是定值
        self.current_task = None  # 记录当前正在处理的任务
        self.remaining_time = 0  # 记录当前任务的剩余时间

    def isBusy(self):
        """"""
        return self.current_task is not None

    def loadTask(self, next_task):
        """"""
        self.current_task = next_task
        self.remaining_time = next_task.getPage() * self.timePerPage  # 计算新任务的剩余打印时间

    def printTask(self):
        if self.isBusy():  # 处理任务中
            self.remaining_time -= 1  # 打印，也就是将剩余打印时间减一
            if self.remaining_time <= 0:  # 当前任务打印结束
                self.current_task = None
        else:
            # 空闲中
            pass


def simulation(total_time, timePerPage):
    """
    :param total_time: 总的实验时间
    :param timePerPage: 每页打印所需要的时间
    :return:
    """
    waiting_time = []

    printer = Printer(timePerPage)
    waitQueue = Queue()

    for second in range(total_time):

        rand_num = random.randrange(1, 181)  # 产生1到180之间的随机数
        if rand_num == 1:
            new_task = Task(second)  # 产生新任务
            waitQueue.add(new_task)  # 新任务进入等待队列

        if (not printer.isBusy()) and (not waitQueue.isEmpty()):  # 打印机空闲并且有任务在等待
            next_task = waitQueue.pop()  # 弹出下一个任务
            waiting_time.append(new_task.waitTime(second))  # 计算并记录等待时间
            printer.loadTask(next_task)  # 载入新的任务

        printer.printTask()  # 打印

    average_time = sum(waiting_time) / len(waiting_time)
    return average_time


def main():
    timeperpage = 5
    total_time = 36000  # 10小时
    print("-----------------")
    for i in range(10):
        average_time = simulation(total_time, timeperpage)
        print("平均等待打印时间为：%.5f 秒" % average_time)
        print("-----------------")


if __name__ == "__main__":
    main()
