__author__ = 'Administrator'
from sklearn import datasets
iris=datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
y_pred=gnb.fit(iris.data,iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d"\
     % (iris.data.shape[0],(iris.target != y_pred).sum()))

'''
在多项式模型中：

在多项式模型中， 设某文档d=(t1,t2,…,tk)，tk是该文档中出现过的单词，允许重复，则
先验概率P(c)= 类c下单词总数/整个训练样本的单词总数
类条件概率P(tk|c)=(类c下单词tk在各个文档中出现过的次数之和+1)/(类c下单词总数+|V|)
V是训练样本的单词表（即抽取单词，单词出现多次，只算一个），|V|则表示训练样本包含多少种单词。 P(tk|c)可以看作是单词tk在证明d属于类c上提供了多大的证据，而P(c)则可以认为是类别c在整体上占多大比例(有多大可能性)。
在伯努利模型中：

P(c)= 类c下文件总数/整个训练样本的文件总数
P(tk|c)=(类c下包含单词tk的文件数+1)/(类c下单词总数+2)

http://blog.163.com/jiayouweijiewj@126/blog/static/1712321772010102802635243/
'''