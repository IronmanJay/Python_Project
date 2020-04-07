from lxml import etree
#生成对象
tree = etree.parse('xpath.html')
ret = tree.xpath('//div[@class="tang"]/ul/li[@class="love" and @name="yang"]')
print(ret)