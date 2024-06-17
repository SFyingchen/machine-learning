#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : chen``
# @Time : 2024/6/17 16:43
# test_wrap: 测试一下wrap的功能
#  作用： wraps 是一个装饰器工厂函数，它用于帮助创建新的装饰器函数，同时保持被装饰函数的元信息（如函数名、文档字符串、注解等）不变


from functools import wraps


def decoration(func):
    @wraps(func)
    def _wraps(n):
        print("运行函数之前执行：")
        result = func(n)
        print("运行之后执行：")
        return result

    return _wraps


@decoration
def example(name):
    print("执行example")
    return name


example("test123456")
# 运行函数之前执行：
# 执行example
# 运行之后执行：
# test123456
