__author__ = 'Administrator'

from sklearn import linear_model
clf=linear_model.Ridge(alpha=.5)
clf.fit([[0,0],[0,0],[1,1]],[0,1,1])
clf.coef_
clf.intercept_