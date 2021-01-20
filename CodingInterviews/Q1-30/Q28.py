# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
使用列表存储树结构： 索引1对应根节点，2*N索引存储左节点，2*N+1索引存储右节点，
求最小的节点值（不会存在相同值的情况）
"""


def Solution(s: str):
    # s = "3 5 7 -1 -1 2 4"
    s = '5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6'
    s = "0 " + s
    ori_l = [int(i) for i in s.split()]
    _len = len(ori_l) - 1

    def f_root(node):
        res = []
        while node > 1:
            if node % 2 == 0:
                node = int(node / 2)
                if ori_l[node] != -1:
                    res.append(ori_l[node])
            else:
                node = int((node - 1) / 2)
                if ori_l[node] != -1:
                    res.append(ori_l[node])
        return res[::-1]

    tree_nodes = [2 ** (i - 1) for i in range(1, 8)]
    print("tree_nodes", tree_nodes)
    _max_c = 0
    total = 0
    for i in range(1, 8):
        total += 2 ** (i - 1)
        if total >= _len:
            _max_c = i  # 最小节点在第三层
            break

    def f_min(node_ceng):
        l = sum([tree_nodes[i] for i in range(node_ceng - 1)])
        r = l + tree_nodes[node_ceng - 1]

        targets = ori_l[l: r]
        # print("f_min",node_ceng,  l, r, targets)
        valid_list = [i for i in targets if i != -1]
        print(valid_list)
        if not valid_list:
            return None, None
        _min = min(valid_list)
        _min_index = ori_l.index(_min)
        if _min_index * 2 <= _len and (_min_index * 2 + 1) <= _len:
            return None, None
        other_nodes = f_root(_min_index)
        other_nodes = other_nodes[::-1]
        other_nodes.append(_min)
        return _min, other_nodes

    print("_max_c", _max_c)

    res = []
    for i in range(2, _max_c + 1):
        result = f_min(i)
        if result[0] is not None:
            res.append(result)

    res = sorted(res, key=lambda x: x[0])
    print(res[0][1])
    return


if __name__ == '__main__':
    t = 120
    print(Solution(t))
