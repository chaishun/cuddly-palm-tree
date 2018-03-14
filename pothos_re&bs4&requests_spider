#coding=utf-8
import requests
import re
from bs4 import  BeautifulSoup
from pip._vendor.requests.api import request
from wsgiref import headers
from nt import mkdir
import traceback
from lib2to3.patcomp import pattern_convert

class spider:
    srcs=[]
    names=[]
    paths=[]
    local="C://Users//admin//Desktop//春装//"  
    star_path="https://www.duitang.com/search/?kw=春装&type=feed#!s-p"
    hs={'user_agent':'Mozilla/5.0'}
    def getPath(self):
        for i in range(0,31):
            path=self.star_path+str(i)
            self.paths.append(path)
    def getHtml(self,path):
        try:
            req=requests.get(path,headers=self.hs)
            req.encoding=req.apparent_encoding
            return req.text
        except:
                 return req.status_code   
    def getdata(self,text):
        soup=BeautifulSoup(text,'html.parser')
        for s in soup.select('img'):
            try:
                if s.attrs['alt']=='春装':
                    src= s.attrs['src']
                    self.srcs.append(src)
                    pattern=r'\d{14}.+g'
                    name=re.findall(pattern,src)
                    self.names.append(name[0])           
            except:    
                   continue    
    def mkfile(self,src,l,name):
         file1=open(self.local+l+name,'wb+')
         response=requests.get(src,headers=self.hs)
         file1.write(response.content)
         file1.close()             
    def main(self):
        try:   
             dir=mkdir(self.local)
        except:
               print("is not empty")
        self.getPath()
        for x in range(0,len(self.paths)):
            html=self.getHtml(self.paths[x])
            self.getdata(html)
            for i in range(0,len(self.srcs)):
                self.mkfile(self.srcs[i],str(x),str(self.names[i]))      
            self.srcs.clear()
            self.names.clear() 
        print('process finished')      
spider1=spider()
spider1.main()
