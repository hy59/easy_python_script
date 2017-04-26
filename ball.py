#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
概率计算，有10个同样的小球，从1-10标号，然后随机从中选出1个小球。如果选出的次数足够多，就可以
计算各个小球备选取出来的概率。
"""

import random


class selectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = raw_input('输入测试的次数：')
            try:
                num = int(numStr)
            except ValueError:
                print(u'要求输入一个整数')
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in xrange(num):
            n = random.randint(1, 10)
            ball[n - 1] += 1
        for i in xrange(1, 11):
            print(u'获取第%d号球的概率为%f' % (i, ball[i - 1] * 1.0 / num))


if __name__ == '__main__':
    SB = selectBall()
