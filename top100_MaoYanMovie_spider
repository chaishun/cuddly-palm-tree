#coding=utf-8
import re
import urllib2
from sre_parse import Pattern
from numpy.ma.core import getdata
import string
import xlwt
wbk=xlwt.Workbook()
sheet1=wbk.add_sheet("mydy",cell_overwrite_ok=True)
def getHtml(path):
    hs={'User_Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    setReq=urllib2.Request(path,headers=hs)
    rep=urllib2.urlopen(setReq)
    return rep.read()
def getData(html,x):
    id_pattern=r'/\d{2,6}. title=.+ class'
    id=re.findall(id_pattern,html)
    star_pattern=r'<p class="star">\s+.+\s</p>'
    star=re.findall(star_pattern,html)
    date_pattern=r".releasetime.>.+</p> "
    date=re.findall(date_pattern,html)
    fs_pattern=r'\d.</i><i class="fraction">\d</i></p>'
    fs=re.findall(fs_pattern,html)     
    c1=sheet1.col(0)
    c1.width=250*30
    c2=sheet1.col(1)
    c2.width=50*30
    c3=sheet1.col(2)
    c3.width=480*30
    c4=sheet1.col(3)
    c4.width=480*30
    for data in range(0,len(id)):
        gid=getID(id[data])
        gdate=getDate(date[data])
        gfs=getfs(fs[data])
        gstar=getStar(star[data])
        sheet1.write(x*10+data,0,gid)
        sheet1.write(x*10+data,1,gfs)
        sheet1.write(x*10+data,2,gstar)
        sheet1.write(x*10+data,3,gdate)
    
def getID(id):       
    s1=string.maketrans('" title="',"\t        ")
    id=id.translate(s1,'" class')
    id=id.replace("/",' ')
    id=id.decode('utf-8')
    return id  
def getfs(fs):
    fq=fs.replace('</i><i class="fraction">',"")
    fs=fq.replace('  f on',"")
    fs=fs.replace('</i></p>','')
    fs=fs.decode('utf-8')
    return fs
def getStar(star):
    s1=string.maketrans('<p class="star">',"                ")
    star=star.translate(s1,'\n')
    star=star.replace("</p>",' ')
    star=star.replace("/",' ')
    star=star.decode('utf-8')
    return star    
def getDate(date):
    s1=string.maketrans('"releasetime">',"              ")
    date=date.translate(s1,'</p>')
    date=date.decode('utf-8')
    return date  
def spider():
    path="http://maoyan.com/board/4?offset="
    for i in range(0,10):
        PATH=path+str(i)+"0"
        getData(getHtml(PATH),i) 
    wbk.save("C://Users//admin//Desktop//maoyanmovie.xls")   
spider()
