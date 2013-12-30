#coding=utf-8
__author__ = 'answer-huang'

import wx
import os

class AHDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for filename in filenames:
            if os.path.isdir(filename):
                self.listAllFiles(filename)
            else:
                print os.path.basename(filename)



    def listAllFiles(self, route):
        for i in os.listdir(route):
            if i.startswith(('.', '$')):
                continue
            subPath = os.path.join(route, i)
            if os.path.isdir(subPath):
                self.listAllFiles(subPath)
            else:
                print i
        print self.num