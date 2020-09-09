from nonebot import CQHttpError, CommandSession, on_command
from bs4 import BeautifulSoup
import nonebot
import requests
import json
import re
import os
login_url="http://erp.sdwz.cn/userPasswordValidate.portal"
login_ur2="http://my.sdwz.cn/"
url_img="http://my.sdwz.cn/s/verification"
notice_list=[]
client=requests.session()
class_list=[]              #用于储存群
@on_command("通知")                        #主动查询
async def kb(session: CommandSession,only_to_me=False):
    a=session.event.group_id
    if a not in class_list and a:
        append_class(a)
    await session.send("来自学校最新五条通知")
    a=0
    while a<5:
        await session.send(notice_list[a]["标题"]+"http://my.sdwz.cn"+notice_list[a]["地址"])
        a=a+1
@nonebot.scheduler.scheduled_job('cron', second='1')
async def _():
    bot = nonebot.get_bot()
    await cha()
def getcookie():
    global client       #获取对话
    denglu=requests.session()
    data={}
    data['Login.Token1']='1817404059'
    data['Login.Token2']='你的密码md5'
    data['goto']='http://erp.sdwz.cn/loginSuccess.portal'
    data['gotoOnFail']='http://erp.sdwz.cn/loginFailure.portal'
    b=denglu.post(login_url,data=data)
    a=denglu.get(login_ur2)
    client=denglu
def main_one():
    print(os.getcwd())
    fi=open('class.json',mode='r')
    class_list=json.loads(fi.read())
    fi.close()
    a=client.get("http://my.sdwz.cn/uc/notice/index")
    soup=BeautifulSoup(a.text,features="html.parser")
    tags=soup.findAll("a",class_="layui-custom-card-li")
    for tags1 in tags:
        notice={}
        #print(tags1.attrs["href"])           #获取地址
        tit=tags1.find("div",class_="layui-col-xs12 layui-col-sm8 layui-col-md8")   ##标题
        notice["地址"]=tags1.attrs["href"]
        notice["标题"]=tit.string
        notice_list.append(notice)
#查询
async def cha():
    a=client.get("http://my.sdwz.cn/uc/notice/index")
    soup=BeautifulSoup(a.text,features="html.parser")
    tags=soup.findAll("a",class_="layui-custom-card-li")
    if tags:
        pass
        for tags1 in tags:
            notice={}
            #print(tags1.attrs["href"])           #获取地址
            tit=tags1.find("div",class_="layui-col-xs12 layui-col-sm8 layui-col-md8")   ##标题
            notice["地址"]=tags1.attrs["href"]
            notice["标题"]=tit.string
            #await fasong(notice["标题"]+"http://my.sdwz.cn"+notice["地址"]+"tes")
            if(notice     not in notice_list):
                print("不存在")
                notice_list.insert(0,notice)#加入末尾
                #发送信息
                for a in class_list:
                    pass
                    await fasong(a,notice["标题"]+"http://my.sdwz.cn"+notice["地址"])
                    notice_list.pop()#删除首部
    else:
        getcookie()
async def fasong(group_id,str):
    bot = nonebot.get_bot()
    try:
        await bot.send_msg(user_id=group_id,
                                 message=str)
    except CQHttpError:
        pass
#初始化
def append_class(str):           #添加数据.
    class_list.append(str)
    file=open('class.json',mode="w+")
    data=json.dumps(class_list,ensure_ascii=False)
    file.write(data)
    file.close()

getcookie()
main_one()
