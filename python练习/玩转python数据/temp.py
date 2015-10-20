#coding=utf-8

'''

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotes = quotes_historical_yahoo('MSFT', start, today)
attributes=['date','open','close','high','low','volume']
quotesdf=pd.DataFrame(quotes,columns=attributes)
list1=[]
for i in range(0,len(quotes)):
    x=date.fromordinal(int(quotes[i][0]))
    y=date.strftime(x,'%y/%m/%d')
    list1.append(y)
quotesdf.index=list1
quotesdf.drop(['date'],axis=1)

print quotesdf.ix['14/01/30':'14/02/10',['open', 'close']]

print quotesdf['14/01/01':'14/12/31'].sort('close', ascending=True)[:5]

print quotesdf['14/1/1':'14/5/31'].sort('volume')

'''
'''
##聚类
from pylab import *
from scipy.cluster.vq import *
list1=[88,74,96,85]
list2=[92,99,95,94]
list3=[91,87,99,95]
list4=[78,99,97,81]
list5=[88,78,98,84]
list6=[100,95,100,92]
data=vstack((list1,list2,list3,list4,list5,list6))

centroids,_=kmeans(data,2)

'''
'''
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,4.,0.1)
plt.plot(t,t,t,t+2,t,t**2)
plt.show()

'''
'''
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import  pandas as pd
x=np.linspace(0,1)
y=np.sin(4*np.pi*x)*np.exp(-5*x)

plt.plot(x,y,'-.*r')
plt.show()
'''
open('week5.txt','w')









