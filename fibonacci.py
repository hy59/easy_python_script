#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
实现斐波拉切数列
"""


class Fibonacci(object):
    '''返回一个斐波拉切数列'''

    def __init__(self):
        self.fList = [0, 1]  # 设置初始表
        self.main()

    def main(self):
        listLen = raw_input('请输入fibonacci数列的长度（3-50):')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print('得到的fibonacci数列为:\n %s ' % self.fList)

    def checkLen(self, lenth):  # 检查输入的数据是否符合要求
        lenList = map(str, xrange(3, 51))
        if lenth in lenList:
            print(u'输入的长度符合要求，程序继续运行')
        else:
            print(u'只能输入3-50长度的数列')
            exit()


if __name__ == '__main__':
    f = Fibonacci()
