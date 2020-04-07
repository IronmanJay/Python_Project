import re

# re高级语法

ret1 = re.search(r"\d+","阅读次数为9999，点赞数为10000").group()
print(ret1)
ret2 = re.findall(r"\d+","阅读次数为9999，点赞数为10000")
print(ret2)
ret3 = re.sub(r"\d+","998","python=997")
print(ret3)
