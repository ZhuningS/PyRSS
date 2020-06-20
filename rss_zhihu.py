import feedparser
import pprint
# import datetime
# import PyRSS2Gen
import json

"""抓取知乎RSS"""
# rss解析
rss_zhihu = feedparser.parse('https://rss.zhufn.fun/zhihu/people/activities/chenlong7890')
# 整理为JSON数组
mylist = [{'title': entry['title'], 'description':entry['description']} for entry in rss_zhihu['entries']]
# pprint.pprint(mylist)

# 强制类型转换
dict_string = str(mylist)


# rssdatas = []
# for rssdata in mylist['description']:

#     rssdatas.append(rssdata.get_text())

# 抓取内容 ， depth 抓取深度
# pprint.pprint(rss_zhihu,depth=1)

# mylist = mylist.applymap(str)

with open(r'e:/tools/pyRSS3.md', 'w', encoding='utf-8') as f:

    f.write(''.join(dict_string)) 

# with open(r'e:/tools/22342.md', 'w', encoding='utf-8') as f:

#     f.write('\n'.join(rssdatas)) 






# for content in rss_zhihu.entries:
#     title=content.title
#     description=content.description

# item=PyRSS2Gen.RSSItem(				#构造一个item
# 		title=title,	#每一项内容的标题
# 		description = description,	#每一项内容的描述/内容
# 		pubDate =datetime.datetime.now()	#更新时间
# 		)
# rssitems=[]
# rssitems.append(item)  				#rssitems即为所有内容



# with open(r'e:/tools/zhihu23423.md', 'w', encoding='utf-8') as f:

#     f.write('\n'.join(rssitems)) 