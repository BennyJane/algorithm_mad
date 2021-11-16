from itertools import product

"""
-----------------------------------------------------------------------------------------
product: 嵌套循环，枚举所有组合

For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
-----------------------------------------------------------------------------------------
"""
for x in product("ab", range(3)):
    print(x)

for y in product((0, 1), (0, 1), (0, 1)):
    print(y)
