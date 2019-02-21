from lxml import etree
import requests
import json
from collections import Counter
red=[]
blue=[]
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response=requests.get('https://chart.cp.360.cn/zst/ssq/?lotId=220051&chartType=zhfb&spanType=0&span=2000&r=0.8490470014183018#roll_132',headers=headers)
ht=response.content.decode('gbk')
html=etree.HTML(ht,etree.HTMLParser())
result=html.xpath('//tr/td[@class="tdbg_1 thide"]/strong/text()')
for item in result:
    if len(item)>3:
        red.append(item)
    else:
        blue.append(item)
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]

for x,y in zip(red,blue):
    res=x+' '+y
    re=res.split(' ')
    print(re)
    list1.append(re[0])
    list2.append(re[1])
    list3.append(re[2])
    list4.append(re[3])
    list5.append(re[4])
    list6.append(re[5])
    list7.append(re[6])
    with open('彩票.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(re, ensure_ascii=False) + '\n')



def max_list(lt):
    temp = 0
    for i in lt:
        if lt.count(i) > temp:
            max_str = i
            temp = lt.count(i)
    with open('彩票.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(max_str, ensure_ascii=False) + '\n')
    print(max_str)
max_list(list1)
max_list(list2)
max_list(list3)
max_list(list4)
max_list(list5)
max_list(list6)
max_list(list7)


