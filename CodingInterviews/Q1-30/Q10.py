# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【模拟工作队列】

=================================================================================
"""


class JobQueue:
    def __init__(self, limit):
        self.items = []
        self.items_deleted = []
        self.length_limit = limit

    def add(self, item):
        if len(self.items) >= self.length_limit:
            self.items_deleted.append(self.items.pop(0))
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)


class Task:
    def __init__(self, start_time, during):
        self.start = start_time
        self.during = during


class Worker:
    def __init__(self, n: int):
        self.sign = n
        self.current_task = None
        self.end_time = 0

    def start_work(self, task, time):
        self.current_task = task
        self.end_time = time + self.current_task.during

    def isBusy(self):
        return self.current_task is not None

    def done(self, time):
        if time == self.end_time:
            self.current_task = None

    def __str__(self):
        return f"<Worker {self.sign}, isBusy:{self.isBusy()}, end_time:{self.end_time}>"

    # def __repr__(self):
    #     return f"<Worker {self.sign}, isBusy:{self.isBusy()}>"


def Solution(task_info: str, limit: int, worker_num: int):
    job_queue = JobQueue(limit)
    workers = [Worker(i) for i in range(worker_num)]
    task_info_list = [int(item.strip()) for item in task_info.split()]
    task_str_length = len(task_info_list)
    task_dict = {}
    for i in range(0, task_str_length, 2):
        start_time = task_info_list[i]
        spend_time = task_info_list[i + 1]
        task_dict[start_time] = Task(start_time, spend_time)

    _startTime = 0
    # 终止时间: 任务列表清空，队列为空，执行者全部空闲
    while True:
        # 优先处理执行者
        for worker in workers:
            if worker.current_task is None and not job_queue.isEmpty():
                task = job_queue.pop()
                worker.start_work(task)
                print("[执行任务]:", _startTime, worker)
            elif worker.current_task is not None:
                worker.done(_startTime)

        # 添加任务
        if task_dict.get(_startTime):
            todo_task = task_dict.get(_startTime)
            job_queue.add(todo_task)
            del task_dict[_startTime]

        # 每次添加完任务后，还需要再次检查是否有空闲的执行者
        for worker in workers:
            if worker.current_task is None and not job_queue.isEmpty():
                task = job_queue.pop()
                worker.start_work(task, _startTime)
                print("[执行任务]:", _startTime, worker)

        if len(task_dict) == 0 and job_queue.isEmpty() and \
                all(not worker.isBusy() for worker in workers):
            break
        _startTime += 1
        print(_startTime)
        # print("worker", workers)

    return _startTime, len(job_queue.items_deleted)


if __name__ == '__main__':
    l = "1 3 2 2 3 3"
    limit = 3
    workers = 2
    print(Solution(l, limit, workers))
