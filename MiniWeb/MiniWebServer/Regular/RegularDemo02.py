import re

# 分组
ret1 = re.match(r"[a-zA-Z_0-9]{4,20}@(163|126)\.com$","laowang@126.com").group()
print(ret1)
ret2 = re.match(r"([a-zA-Z_0-9]{4,20})@(163|126)\.com$","laowang@163.com").group(2)
print(ret2)

html1 = "<h1>hahahaha</h1>"
ret3 = re.match(r"<(\w*)>.*</\1>",html1).group()
print(ret3)
html2 = "<body><h1>hahahaha</h1></body>"
ret4 = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>",html2).group()
print(ret4)
