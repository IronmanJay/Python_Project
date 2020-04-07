"""
问题：
在csv文件中随机读取一个不重复的数据。
"""

import csv
import random

reader = csv.reader(open("a.csv"))

a = list(reader)

for i in range(len(a)):

    num = random.randint(0,len(a)-1)

    print(a[num])

    a.remove(a[num])
