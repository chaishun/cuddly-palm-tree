import urllib2
import os
import re
import string
import shutil
import time
from pip._vendor.requests.api import request
def mkDir():
    if os.path.exists("C://Users//admin//Desktop//getPages")==False:
        dir=os.mkdir("C://Users//admin//Desktop//getPages")
        dir2=os.mkdir("C://Users//admin//Desktop//getPages//keys")
def getHtml(path):
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    hs={"User-Agent":user_agent}
    setReq=urllib2.Request(path,headers=hs)
    getRep=urllib2.urlopen(setReq)
    reponse=getRep.read()
    return reponse
def makeFile(data,i):
    getFile=file("C://Users//admin//Desktop//getPages//"+str(i)+".txt",'w+').write(data)
    return getFile
def getData(getfile,i):
    pattern=ur'<span>\s+?.+\s+?</span>'
    getKeys=re.findall(pattern, getfile)
    keyfile=file("C://Users//admin//Desktop//getPages//keys//"+str(i)+".txt",'w+')
    for s in range(0,len(getKeys)-1):
        keyfile.write( str(s)+anlayData(getKeys[s]))
def anlayData(getdata):
    s1=string.maketrans("<span>","      ")
    s2=string.maketrans("br/","   ")    
    getdata=getdata.translate(s1, "h2")
    getdata=getdata.translate(s2, " ")
    return getdata
def spider(pages):
    path="http://www.qiushibaike.com/hot/page/"
    for i in range(1,pages):
        mkDir()
        data=getHtml(path+str(i))
        getfile=makeFile(path+str(i)+data, i)
        getData(data, i)
page=input("you want amount of pages<15")
if page>15:
    page=14
spider(page)
print "process finshed"
time.sleep(3)
