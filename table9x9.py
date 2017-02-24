#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
九九乘法表
"""

class printTable(object):
    def __init__(self):
        print(u'打印九九乘法表')
        self.print99()

    def print99(self):
        for i in xrange(1,10):
            for j in xrange(1,i+1):
                print('%d*%d=%2s ' % (j,i,i*j)),
            print('\n')


if __name__ == '__main__':
    printTable = printTable()
