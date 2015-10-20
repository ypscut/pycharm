# -*- coding: UTF-8 -*-

#<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>
import urllib
import time
url=['']*350
page=1
while page<=7:
    con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html').read()
    i=0
    title = con.find(r'<a title=')
    href=con.find(r'href=',title)
    html=con.find(r'.html',href)
    while title!=-1 and href!=-1 and html!=-1and  i<40:
        url[i]=con[href+6:html+5]
        print url[i]
        title = con.find(r'<a title=',html)
        href=con.find(r'href=',title)
        html=con.find(r'.html',href)
        i+=1
    else:
        print page ,'find end!'
    page += 1
else:
    print 'all find end!'
j=0
while j<350:
    content=urllib.urlopen(url[j]).read()
    open(r'hanhan/'+url[j][-26:],'w+').write(content)
    j+=1
    time.sleep(15)
else:
    print 'download article finished'


'''
str0='<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
title=str0.find(r'<a title')
print title

href=str0.find(r'href=')
html=str0.find(r'.html')
url=str0[href+6:html+5]
print url
content=urllib.urlopen(url).read()
#print content

filename=url[-26:]
print filename
open(filename,'w').write(content)
'''




