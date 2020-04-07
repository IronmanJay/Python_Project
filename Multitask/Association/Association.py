from collections.abc import Iterable
from collections.abc import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个可以迭代的对象即可以使用for，那么就必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("老王")
classmate.add("李四")
classmate.add("张三")

# # 判断classmate是否是可以迭代的对象
# print(isinstance(classmate,Iterable))
#
# classmate_iterator = iter(classmate)
# # 判断classmate_iteratore是否是迭代器
# print(isinstance(classmate_iterator,Iterator))
#
# print(next(classmate_iterator))

for name in classmate:
     print(name)
     time.sleep(1)