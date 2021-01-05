# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
参数传递:
一般函数：在调用时，完成参数传递，引用传递，内部s与外部s指向同一个引用对象; 外部s被修改后，外部变量s指向新的引用地址，内部不受影响
生成器表达式：定义的时候，存储的是变量名称，而不是内存对象；当变量值被修改后，表达式内部的变量值也被修改； （s被修改，i正常）
匿名函数<1>：在生成列表时，匿名函数直接被执行，s，i都正常
匿名函数<2>：先生成匿名函数列表，在求和时，逐个调用匿名函数，此时s,i作为匿名函数内部变量，直接引用当前环境中最后的s、i的值(100 99),结果错误
匿名函数<3>：先生成匿名函数列表，s作为匿名函数关键字参数传入，为0，正常；i使用循环后的最后一个值 99；计算错误
匿名函数<4>：先生成匿名函数列表，s、i作为匿名函数关键字参数传入，记录每个循环时的特定值，最后调用时，使用的时每个匿名函数自身保存的关键字参数，正常。
"""
s = 0
print(id(s), s)


def f(s=None):
    print("s", id(s), s)
    return [s + i for i in range(100)]


function_result = f(s)
generator_expression = (s + i for i in range(100))
lambda_func_called = [(lambda i: i + s)(i) for i in range(100)]  # <1>
lambda_func_list = [lambda: i + s for i in range(100)]  # <2>
lambda_func_kwarg = [lambda s=s: i + s for i in range(100)]  # <3>
lambda_func_kwargs = [lambda s=s, i=i: i + s for i in range(100)]  # <4>
s = 100
print(id(s), s)

print("一般函数执行结果：", sum(function_result))
print("生成器表达式执行结果：", sum(generator_expression))
print("匿名函数直接被调用的结果：", sum(lambda_func_called))
print("匿名函数没有被调用的结果(s作为常量)：", sum([f() for f in lambda_func_list]))
print("匿名函数没有被调用的结果(s作为变量)：", sum([f() for f in lambda_func_kwarg]))
print("匿名函数没有被调用的结果(s，i都作为变量)：", sum([f() for f in lambda_func_kwargs]))
