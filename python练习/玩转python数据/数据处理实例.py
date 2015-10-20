#coding=utf-8
#微软公司2014年第一季度股票收盘价的平均值

'''
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo('MSFT', start, today)
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
#csv格式数据存取
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today=date.today()
start=(today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo('IBM',start,today)
df=pd.DataFrame(quotes)
df.to_csv('stockIBM.csv')
'''
import  pandas as pd
result=pd.read_csv('stockIBM.csv')
print result['2']


##week4 编程练习
#用折线图比较Microsoft和Intel在2014年每个月股票的最高收盘价。
# 图标题为“Max Close of MS and INTEL”，横坐标是时间，纵坐标是价格

import time
from matplotlib.finance import quotes_historical_yahoo
from matplotlib.finance import  quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
start = datetime(2014,1,1)
end = datetime(2014,12,31)
quotesMSFT = quotes_historical_yahoo_ochl('MSFT', start, end)
quotesINTC = quotes_historical_yahoo_ochl('INTC', start, end)
fields = ['date','open','close','high','low','volume']
#quotesdf = pd.DataFrame(quotes, columns = fields)
#quotesdf = pd.DataFrame(quotes, index = range(1,len(quotes)+1),columns = fields)
list1 = []
for i in range(0,len(quotesMSFT)):
    x = date.fromordinal(int(quotesMSFT[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
#print list1
list2 = []
for i in range(0,len(quotesINTC)):
    x = date.fromordinal(int(quotesINTC[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list2.append(y)
quotesmsftdf = pd.DataFrame(quotesMSFT, index = list1, columns = fields)
quotesmsftdf = quotesmsftdf.drop(['date'], axis = 1)
#print quotesdf
quotesintcdf = pd.DataFrame(quotesINTC, index = list1, columns = fields)
quotesintcdf = quotesintcdf.drop(['date'], axis = 1)
listtemp1 = []
for i in range(0,len(quotesmsftdf)):
    temp = time.strptime(quotesmsftdf.index[i],"%Y-%m-%d")
    listtemp1.append(temp.tm_mon)
listtemp2 = []
for i in range(0,len(quotesintcdf)):
    temp = time.strptime(quotesintcdf.index[i],"%Y-%m-%d")
    listtemp2.append(temp.tm_mon)
tempmsftdf = quotesmsftdf.copy()
tempmsftdf['month'] = listtemp1
closemaxMSFT = tempmsftdf.groupby('month').max().close
listMSFT = []
for i in range(1,13):
    listMSFT.append(closemaxMSFT[i])
listMSFTIndex = closemaxMSFT.index
tempintcdf = quotesintcdf.copy()
tempintcdf['month'] = listtemp2
closemaxINTC = tempintcdf.groupby('month').max().close
listINTC = []
for i in range(1,13):
    listINTC.append(closemaxINTC[i])
listINTCIndex = closemaxINTC.index
pl.subplot(211)
plt.plot(listMSFTIndex,listMSFT,color='r',marker='o')
pl.subplot(212)
plt.plot(listINTCIndex,listINTC,color='green',marker='o')
plt.show()
plt.sc