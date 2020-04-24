import os
import sys
import re
from bs4 import BeautifulSoup
import requests
notice_list=[]  #储存最近的通知
login_url="http://erp.sdwz.cn/userPasswordValidate.portal"
login_ur2="http://my.sdwz.cn/uc/user/index"
url_img="http://my.sdwz.cn/s/verification" 
def getcookie():       #获取对话
    denglu=requests.session()
    data={}
    data['Login.Token1']='1817404059'
    data['Login.Token2']='cc39f38ac49ed223ea53970e8efca90bf1e92d37'
    data['goto']='http://erp.sdwz.cn/loginSuccess.portal'
    data['gotoOnFail']='http://erp.sdwz.cn/loginFailure.portal'
    b=denglu.post(login_url,data=data)
    print(b.text)
    a=denglu.get(login_ur2)
    print(a.text)
    return denglu
'''
#初始化
client=getcookie()
a=client.get("http://my.sdwz.cn/uc/notice/index")
print(a.text)
soup=BeautifulSoup(open("html.html","rb"),features="html.parser")
tags=soup.findAll("a",class_="layui-custom-card-li")
for tags1 in tags:
    notice={}
    #print(tags1.attrs["href"])           #获取地址
    tit=tags1.find("div",class_="layui-col-xs12 layui-col-sm8 layui-col-md8")   ##标题
    notice["地址"]=tags1.attrs["href"]
    notice["标题"]=tit.string
    notice_list.append(notice)
    notice_list.reverse()
print(notice_list)
#轮询一次
soup=BeautifulSoup(open("html.html","rb"),features="html.parser")
tags=soup.findAll("a",class_="layui-custom-card-li")
for tags1 in tags:
    notice={}
    #print(tags1.attrs["href"])           #获取地址
    tit=tags1.find("div",class_="layui-col-xs12 layui-col-sm8 layui-col-md8")   ##标题
    notice["地址"]=tags1.attrs["href"]
    notice["标题"]=tit.string
    if(notice  not in notice_list):
        print("不存在")
        notice_list.append(notice)#加入末尾
        #发送信息
        del notice_list[0]#删除首部
'''