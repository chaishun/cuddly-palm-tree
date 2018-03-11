#coding=utf-8
import requests
import xlwt
from bs4 import BeautifulSoup

wbk=xlwt.Workbook()
sheet1=wbk.add_sheet('1')
list=["排名",'学校','国家排名','总分','学术ALUMNI']
for i in range(0,len(list)):
    celli=sheet1.col(i)
    if i!=0:
        celli.width=256*30
    sheet1.write(0,i,list[i])
  
hs={"user-agent":"Mozilla/5.0"}
r=requests.get("http://www.zuihaodaxue.cn/ARWU2017.html",headers=hs)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,"html.parser")   
x=0
y=0
for s in soup.find_all('tr'):
    tp=''
    for t in s.find_all('td',limit=6):
        text=t.string
        tp=tp+' '+str(text)
        if str(text)!='None':
             sheet1.write(x,y,str(text))
             y=y+1
        else :
            pass
    print(tp)
    x=x+1
    y=0    
wbk.save("C://Users//admin//Desktop//dxpm.xls")  

