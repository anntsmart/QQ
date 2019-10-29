# -*- coding: cp936 -*-
import requests
import urllib
import os
import re
import xlwt
#from selenium import webdriver
#import qqlib



#browser = webdriver.Firefox()
#login_url="https://mail.qq.com/"
#browser = webdriver.Firefox("H:\\Python27\\geckodriver.exe")
#browser.get("http://www.baidu.com")
cookies=raw_input("Input QQ cookie:")
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'http://find.qq.com/index.html?version=1&im_version=6799&width=910&height=610&search_target=0',
        'Cookie':cookies,
        'DNT' : '1',
        'Content-Type' : 'application/x-www-form-urlencoded'
        }
url="http://ti.qq.com/mqqbase/cgi/qqrecommend/people"
data={
    "uinnum":"283",
    "page":"0",
     "startpos":"0",
    "type":"3",
     "use_846":"1",
     "filter_uin":"",
     "relationuin":"0",
     "ldw":"58932881"
}
r=requests.post(url,data=data,headers=header)
content=r.content
pat_num=r'uin":(.*?),'
pat_name=r'nickName":"(.*?)"'
pat_nums=r'strReason":"(.*?)"'
pat_realname=r'sRemark":"(.*?)"'
result_num=re.findall(pat_num,content)
result_name=re.findall(pat_name,content)
result_nums=re.findall(pat_nums,content)
result_realname=re.findall(pat_realname,content)
wb=xlwt.Workbook(encoding='utf-8')
ws=wb.add_sheet('QQ')
ws.write(0,0,u'禁止用于非法用途！！！！')
ws.write(1,0,u'QQ号码')
ws.write(1,1,u'QQ昵称')
ws.write(1,2,u'QQ共同好友数量')
ws.write(1,3,u'QQ真实姓名')
j=2
for i in range(len(result_num)):
    try:
        ws.write(j,0,result_num[i])
        ws.write(j,1,result_name[i])
        ws.write(j,2,result_nums[i])
        ws.write(j,3,result_realname[i])
        j+=1
    except:
        pass

wb.save('QQ.xls')
    

