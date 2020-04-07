import re

# re.match(正则表达式，需要处理的字符串)
res1 = re.match(r"hello","hello world").group()
print(res1)
res2 = re.match(r"[hH]ello","hello world").group()
print(res2)

# 匹配单个字符
res3 = re.match(r"速度与激情\d","速度与激情4")
res4 = re.match(r"速度与激情[1-8]","速度与激情8")
res5 = re.match(r"速度与激情[1-36-8]","速度与激情8")
print(res3.group())
print(res4.group())
print(res5.group())
res6 = re.match(r"速度与激情[1-8a-zA-Z]","速度与激情A").group()
print(res6)
res7 = re.match(r"速度与激情\w","速度与激情_").group()
print(res7)
res8 = re.match(r"速度与激情\s\d","速度与激情\t1").group()
print(res8)
res9 = re.match(r"速度与激情.","速度与激情哈").group()
print(res9)

# 匹配多个字符
res10 = re.match(r"\d{11}","12345678901").group()
print(res10)
res11 = re.match(r"\d{3,4}-?\d{8}","021-12345678").group()
print(res11)
html = """hjjbhnjk
asdf
asfsf
asd"""
res12 = re.match(r".*",html,re.S).group()
print(res12)
