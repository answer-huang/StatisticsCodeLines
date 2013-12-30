#coding=utf-8
__author__ = 'answer-huang'

import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
代码行统计工具
"""

import wx
from MyInfo import AboutMe
from AHDropTarget import AHDropTarget
import os



class AHFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, wx.DefaultPosition, wx.Size(500, 380),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
                          #style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        self.SetTransparent(250)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetForegroundColour('red')
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-2, -1]) #大小比例2:1
        toolbar = self.CreateToolBar()
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(1, wx.Image('about.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "关于我", "")
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(2, wx.Image('donate.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "捐助我", "")
        toolbar.Realize()  #准备显示工具栏
        wx.EVT_TOOL(self, 1, self.OnAboutMe)
        wx.EVT_TOOL(self, 2, self.OnDonate)

        self.panel = wx.Panel(self)
        self.panel.SetDropTarget(AHDropTarget(self))

        self.font = wx.Font(18, wx.SCRIPT, wx.BOLD, wx.LIGHT)
        self.selectedPath = wx.StaticText(self.panel, -1, u'将项目拖拽到这里', pos=(178, 280))
        self.selectedPath.SetFont(self.font)

        self.panel.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.panel.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
        self.panel.Bind(wx.EVT_MOTION, self.OnMotion)

    def OnEnterWindow(self, event):
        #print event.LeftIsDown()
        event.Skip()

    def OnLeaveWindow(self, event):
        #print "leave"
        event.Skip()

    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            print '按住了鼠标移动'
        event.Skip()

    def UpdateStatus(self, path, codes_num):
        self.statusbar.SetStatusText(path, 0)
        self.statusbar.SetStatusText(codes_num, 1)


    def ShowImage(self, img):
        self.image = wx.Image(img, wx.BITMAP_TYPE_JPEG).Rescale(500, 350, quality=wx.IMAGE_QUALITY_HIGH)
        bitmap = self.image.ConvertToBitmap()
        self.logo = wx.StaticBitmap(self.panel, bitmap=bitmap, pos=(0, 0), size=(500, 350))

    def ShowPathDir(self, dirList):
        wx.CheckListBox(self.panel, -1, choices=dirList)

    def OnAboutMe(self, event):
        aboutMe = AboutMe(self)
        aboutMe.ShowModal()
        aboutMe.Destroy()

    def OnDonate(self, event):
        #wx.BeginBusyCursor()
        import webbrowser
        webbrowser.open('https://me.alipay.com/huangaiwu')
        #wx.EndBusyCursor()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = AHFrame(None, '代码统计工具')
    frame.Show(True)
    app.MainLoop()