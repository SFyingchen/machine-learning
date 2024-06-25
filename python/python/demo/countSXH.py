#!/usr/bin/python3``
# -*- coding: utf-8 -*-``
# @Author : chen``
# @Time : 2024/6/24 16:30
# countSXH: 计算水仙花数目

listResult = []
for i in range(100, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = (i - (a * 10 + b) * 10)
    temp = a ** 3 + b ** 3 + c ** 3
    if (temp == i):
        listResult.append(i)

# print(listResult)

stringList = "Hello world"

print(stringList[0], stringList[-1],stringList[-4])