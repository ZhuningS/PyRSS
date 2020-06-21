#!usr/bin/env python3

#coding:utf-8

# 实现一个程序小demo，定期抓取RSS并且修改文章中的特定信息（在阅读之前处理一下）
# 比如知乎每日精选RSS源：https://www.zhihu.com/rss。
# 抓取到本地：发送请求，接收并存为对象
# 先移除其中作者名字、关键词，再结构化数据： Python文本处理

# 然后再转换为rss阅读器那种方便阅读的文档格式（txt/md/htm等等都可以）: 对象 转为文档 使用第三方插件工具
# TODO:目前未完善的地方：1，定时，可以配合linux-定时任务-crontab 或者 win计划任务 2，修改，移除其中作者名字、关键词

# 写个循环，每次写入文件的时候给文件命名加个变量不就好了,或者在文件命名的时候加个系统时间
# 或者把xml全部抓取出来，然后用正则清洗，正则替换
# 移除作者名字可以找共同点 充其量也就是对字符串处理 新建文件这个每抓取一次新建一次


#  re.sub 可以实现正则替换，看文档：https://docs.python.org/3/library/re.html#module-contents
# 具体该怎么写，你得先定义好规则，然后才能写。。。
# 如果只是把 ell 替换成 一二三，那你不需要用 regex，用 string 的 replace 方法就够了 https://docs.python.org/3/library/stdtypes.html




# 编程首先要学习基础，然后用程序处理的解决方法和思路，前提是对各种常用库都很熟，或者能去网络搜索需要的库，学习方法，然后编写代码调试…

# feedparser： 可以轻松从任何 RSS 或 Atom 订阅源抓取标题、链接和文章的条目。简单方便。

# pprint: 格式化美观输出内容

# 安装feedparser模块
# pip install feedparser


import requests
from bs4 import BeautifulSoup
import feedparser
import pprint
import datetime
import time

url = 'https://rss.zhufn.fun/zhihu/people/activities/chenlong7890'

# url = 'http://www.tcmap.com.cn/shanghai/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

response = requests.get(url, headers=headers) #发送HTTP请求

response .encoding = 'utf-8' #设置一下网站的中文编码

soup = BeautifulSoup(response.text, 'html.parser') #使用 BeautifulSoup 进行解析

# rss解析
rss_zhihu = feedparser.parse(url)
# 抓取内容 ， depth 抓取深度
pprint.pprint(rss_zhihu,depth=2)

zhihudatas = []

# 找到数据对应的 html 节点，然后使用get_text()函数获取

for zhihudata in soup.find_all('description'):

    zhihudatas.append(zhihudata.get_text())

# 最后写入到相关文件夹中

with open(r'e:/tools/zhihu.md', 'w', encoding='utf-8') as f:

    f.write('\n'.join(zhihudatas)) 

# with open(r'e:/tools/pyRSS2.txt', 'w', encoding='utf-8') as f:

#     f.write('\n'.join(rss_zhihu)) 

# 这里仅用第三方的 requests 库访问链接，然后用 Beautifulsoup 库来提取页面源代码中的数据，最后将得到的数据存储到一个列表中。
