#coding=utf-8
__author__ = 'answer-huang'

import os

#for i in os.walk('/Users/aiwuhuang/Desktop/wxPython'):
#    print i


def listdir(level, route):
    for i in os.listdir(route):
        if i.startswith(('.', '$')):
            continue
        subPath = os.path.join(route, i)
        if os.path.isdir(subPath):
            print('|  '*(level + 1) + i)
            listdir(level+1, subPath)
        else:
            print('|  '*(level + 1) + i)

#path = '/Users/aiwuhuang/Desktop/wxPython'
#listdir(0, path)

