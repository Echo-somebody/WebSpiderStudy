import requests
from pyquery import PyQuery as pq
import logging
logging.basicConfig(level=logging.INFO,format='line:%(lineno)d %(message)s')
'''
1,pyquery库的安装
'''
session = requests.session()
html = session.get('https://www.baidu.com/')
html.encoding = 'utf-8'     #网页编码charset=utf-8时不一定不乱码
# file = 'baidu.html'
# with open(file=file,mode='w',encoding='utf-8') as f:
#     f.write(html.text)
'''
2，PyQuery的初始化：
    字符串初始化  给pq传入字符串
    URL初始化    给pq传入URL连接  pq(url='')
    文件初始化    给pq传入文件名   pq(filename='')
'''
doc = pq(html.text)
'''
3,基本CSS选择器
'''
logging.info(doc('div'))
logging.info(doc('#u1 .lb')) #初始化PyQuery对象之后，传入一个CSS选择器#u1 .lb li，其含义是先选取id为u1的节点，再选取该节点中class=lb的节点，再选取节点名称为li
logging.info(type(doc('#u1 .lb')))
'''
4,查找节点
    子节点 使用find()方法，传入CSS选择器
    父节点 使用parent()方法获取某个节点的父节点
    兄弟节点 使用siblings()方法
'''
items = doc('.head_wrapper')
logging.info(items)
logging.info(type(items))
lis = items.find('form')
logging.info(lis)
lis = items.find('.s_form')
logging.info(lis)
lis = items.find('.s_form').children()
logging.info(lis)
logging.info(type(lis))
logging.info(lis.parent())
logging.info(lis.parents())
logging.info(lis.parents('div'))
'''
5,遍历：pyquery选择的结果可能是多个节点，也有可能是单个节点，类型都是PyQuery的类型，并没有返回像BeautifulSoup那样的列表
'''
mnav = doc('.mnav').items()
logging.info(mnav)
logging.info(str(mnav))
for i in mnav:
    logging.info(i)
    logging.info(type(i))
'''
6,获取信息  常用的是获取属性和文本
'''
a = doc('#u1 a')
logging.info(a.attr('href')) #或者logging.info(a.attr.href)
for i in a.items():
    logging.info(i.attr('href'))
logging.info(a.text())
'''
7,节点操作：对某一节点进行增加或删除修改  
    对属性进行增、删 remove_class()  add_class() attr()
    对节点内部内容进行修改   text()和html()
    remove()
'''
form = doc('form')
logging.info(form)
form.remove_class('fm')
logging.info(form)
form.add_class('fm')
logging.info(form)
form.attr('test','01')  #attr()方法只传入第一个参数的属性名，则是获取这个属性值；如果也传入第二个参数，可以用来修改属性值
logging.info(form)
form.text('changed item') #text()和html()方法不传入参数，则是获取节点内纯文本和HTML文本，如果传入参数，则进行修改重新赋值
logging.info(form)
form.html('<span>changed items</span>')
logging.info(form)
wrapper = doc('.s_form_wrapper')
logging.info(wrapper)
wrapper.find('form').remove()
logging.info(wrapper)
'''
8,伪类选择器
'''






















