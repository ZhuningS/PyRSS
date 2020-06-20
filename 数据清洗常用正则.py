# 「Python」数据清洗常用正则
# 对爬虫数据进行自然语言清洗时用到的一些正则表达式

# 标签中的所有属性匹配（排除src,href等指定参数）

# https://www.cnblogs.com/luyanru66/p/9761453.html

# \b(?!src|href)\w+=[\'\"].*?[\'\"](?=[\s\>])
# 匹配特征 id="..." 
# \b(?!...)排除属性名中的指定参数，零宽断言前向界定判断属性结束
# tips: 带\b的python正则匹配一定要加r转义

str1 = '''
<div class="concent" id="zoomcon" style="padding:15px;">
<img border="0" src="/xcsglj/zyhd/201802/f5492c1752094f44bcebae4a68480c64/images/9a900610afc54ee3b468780785a2ecec.gif">
<img border="0" src="/xcsglj/zyhd/201802/f5492c1752094f44bcebae4a68480c64/images/4b802f5d2d8c4ecd9a0525e0da7d886e.gif">
<img href="0" src="/xcsglj/zyhd/201802/f5492c1752094f44bcebae4a68480c64/images/4b802f5d2d8c4ecd9a0525e0da7d886e.gif">
'''

print(re.findall(r'\b(?!src)\w+=[\'\"].*?[\'\"](?=[\s\>])', string=str1))
# result: ['class="concent"', 'id="zoomcon"', 'style="padding:15px;"', 'border="0"', 'border="0"', 'href="0"']