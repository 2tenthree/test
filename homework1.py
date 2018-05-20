#!/usr/bin/env python
# -*- coding:utf-8 -*-


def message(dic, name, weight):
    dic[name] = weight

lis1 = {}
message(lis1, '陈尧', '88kg')
message(lis1, '蔡志强', '50kg')
message(lis1, '豹王', '62kg')
message(lis1, '杨正茂', '66kg')

for key, value in lis1.items():
    print(key + '的体重是' + value)




