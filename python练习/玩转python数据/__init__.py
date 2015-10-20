#coding=utf-8
'''
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo('MSFT', start, today)
print  '###',quotesMS[2][0]
attributes=['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS, columns= attributes)
list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfMS.index = list
quotesdfMS = quotesdfMS.drop(['date'], axis = 1)
list = []
quotesdfMS14 = quotesdfMS['14/01/01':'14/12/31']
for i in range(0, len(quotesdfMS14)):
    list.append(int(quotesdfMS14.index[i][3:5])) #get month just like '02'
quotesdfMS14['month'] = list
print quotesdfMS14.groupby('month').mean().close

'''
'''
class Dog(object):
    "define Dog class"
    def __init__(self,name):
        self.name=name
    def greet(self):
        print "Call me %s" %self.name
if __name__=='__main__':
    dog=Dog()
    dog.setname('wc')
    dog.greet()

'''

## Filename: firstwxPython.py
'''
import wx
app=wx.App()
frame=wx.Frame(None,title="Hello,World")
frame.Show(True)
app.MainLoop()

# 上例修改后
#Filename: mouse.py
import  wx

class Myapp(wx.App):
    def OnInit(self):
        frame=wx.Frame(None,title="Hello,World")
        frame.show()
        return True
if __name__=='__main__':
    app=Myapp()
    app.MainLoop()
'''
#Filename:helloworld.py
'''
import  wx

class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title='Example',pos=
        (100,200),size=(200,100))
        self.panel=wx.Panel(self)
        text1=wx.TextCtrl(panel=self,value='Hello,world',size=(200,100))

        self.panel.Bind(wx.EVT_LEFT_UP,self.OnCLick)

    def OnClick(self,event):
        posm=event.GetPosition()
        wx.StaticText(parent=self.panel,label="Hello,World",pos=(posm.x,posm.y))
if __name__=='__main__':
    app=wx.App()
    frame=Frame1(None)
    frame.Show(True)
    app.MainLoop()

'''
#图形用户界面
#Filename: helloworldbtn.py
'''
import  wx
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="Hello World in wxPython")
        panel=wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)
        self.text1=wx.TextCtrl(panel,value="Hello,World",size
        =(200,180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP | wx.EXPAND)
        button=wx.Button(panel,label="Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.Onclick,button)
    def Onclick(self,text):
        self.text1.AppendText("\nHello,World!")

if __name__=='__main__':
    app=wx.App()
    frame=Frame1(None)
    frame.Show(True)
    app.MainLoop()
'''
'''
def ask(promt="Do you like Python?",hint="yes or no"):
    while True:
        answer=raw_input(promt)
        if answer.lower() in ('y','yes'):
            print "Thank you"
            return True
        if answer.lower() in ('n','no'):
            print 'Why not'
            return False
        else:
             print hint

ask("Do you like Python?")
'''


'''
def ask(prompt, hint = "yes or no", chance =2):
    while chance > 0:
        answer = raw_input(prompt)
        if answer.lower() in ('y', 'yes'):
            print "Thank you"
            return True
        if answer.lower() in ('n', 'no'):
            print "Why not "
            return False
        else:
            chance -= 1
        print hint
    print "Sorry, you have tried too many times."

'''
fp = open('test.txt', 'r+', 0)
fp.readline()
fp.seek(10, 1)
print fp.readline()




