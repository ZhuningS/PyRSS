# Python通过正则表达式获取,去除(过滤)或者替换HTML标签的几种方法，具体内容如下

# python正则表达式关键内容:

# python正则表达式转义符:
# . 匹配除换行符以外的任意字符
# \w 匹配字母或数字或下划线或汉字
# \s 匹配任意的空白符
# \d 匹配数字
# \b 匹配单词的开始或结束
# ^ 匹配字符串的开始
# $ 匹配字符串的结束
# \W 匹配任意不是字母，数字，下划线，汉字的字符
# \S 匹配任意不是空白符的字符
# \D 匹配任意非数字的字符
# \B 匹配不是单词开头或结束的位置
# [^x] 匹配除了x以外的任意字符
# [^aeiou] 匹配除了aeiou这几个字母以外的任意字符


# 常用的python正则表达式限定符代码/语法说明:
# *重复零次或更多次
# +重复一次或更多次
# ?重复零次或一次
# {n}重复n次
# {n,}重复n次或更多次
# {n,m}重复n到m次


# 关于python正则表达式命名组:
# 命名组:(?P<name>.....)
# 这篇文章里面还提到了界定( 问号开头,前向则有个'<'号,非则有个'!' 号 ):
# 前向界定 (?<=…)
# 后向界定 (?=…)
# 前向非界定 (?<!....)
# 后向非界定 (?!.....)
# Python通过正则表达式获取,去除(过滤)或者替换HTML标签代码举例

# 1、Python通过正则表达式取html中天气信息代码示例:

#!/usr/bin/env python
#-*- coding: utf8 -*-
import re
   
html = """
  <h2>多云</h2>
"""
   
if __name__ == '__main__':
  p = re.compile('<[^>]+>')
  print p.sub("", html)
Python通过正则表达式取html中温度信息代码示例:
#!/usr/bin/env python
#-*- coding: utf8 -*-
import re
   
html = """
  <div class="w-number"> <span class="tpte">14℃</span> </div>
"""
   
if __name__ == '__main__':
  p = re.compile('<[^>]+>')
  print p.sub("", html)


# 2、Python通过正则表达式去除(过滤)HTML标签示例代码:

# -*- coding: utf-8-*-
import re
##过滤HTML中的标签
#将HTML中标签等信息去掉
#@param htmlstr HTML字符串.
def filter_tags(htmlstr):
  #先过滤CDATA
  re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
  re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
  re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
  re_br=re.compile('<br\s*?/?>')#处理换行
  re_h=re.compile('</?\w+[^>]*>')#HTML标签
  re_comment=re.compile('<!--[^>]*-->')#HTML注释
  s=re_cdata.sub('',htmlstr)#去掉CDATA
  s=re_script.sub('',s) #去掉SCRIPT
  s=re_style.sub('',s)#去掉style
  s=re_br.sub('\n',s)#将br转换为换行
  s=re_h.sub('',s) #去掉HTML 标签
  s=re_comment.sub('',s)#去掉HTML注释
  #去掉多余的空行
  blank_line=re.compile('\n+')
  s=blank_line.sub('\n',s)
  s=replaceCharEntity(s)#替换实体
  return s
  
##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
  CHAR_ENTITIES={'nbsp':' ','160':' ',
        'lt':'<','60':'<',
        'gt':'>','62':'>',
        'amp':'&','38':'&',
        'quot':'"','34':'"',}
    
  re_charEntity=re.compile(r'&#?(?P<name>\w+);')
  sz=re_charEntity.search(htmlstr)
  while sz:
    entity=sz.group()#entity全称，如>
    key=sz.group('name')#去除&;后entity,如>为gt
    try:
      htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
      sz=re_charEntity.search(htmlstr)
    except KeyError:
      #以空串代替
      htmlstr=re_charEntity.sub('',htmlstr,1)
      sz=re_charEntity.search(htmlstr)
  return htmlstr
def repalce(s,re_exp,repl_string):
  return re_exp.sub(repl_string,s)
if __name__=='__main__':
  s=file('169it.com_index.htm').read()
  news=filter_tags(s)
  print news
