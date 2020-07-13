import requests
from lxml import etree

from urllib import request

import time

import time
 
#request.urlretrive()方法下载图片 抓取任意网站图片，比如知乎豆瓣，简书

def huyaSpider():
	url = "https://www.huya.com/g/lol"
	# url = "https://www.douban.com/people/113894409/"

	User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
	headers = {'User_Agent': User_Agent}
	
	response = requests.get(url,headers=headers)
	
	data = response.text
	
	dataDemo = etree.HTML(data)
	
	row = dataDemo.xpath('//img[@class="pic"]')
	# //re也可以，爬虫方式有区别
	# print(row)
 
	for i in row:
	  img = i.xpath('./@data-original')[0]
	  # //src容易变，data-original
	  
	  img = img.split('?')[0]
	  
	  name = i.xpath('./@alt')[0]
	  
	try:
		request.urlretrive(img, r'C:'+ name + '.jpg')
	except Exception as e:
		pass

	time.sleep(3)

	print("<%s> 下载完毕 ！" % name)
	  
	  
huyaSpider()


# scrapy 爬虫框架
