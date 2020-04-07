from queue import Queue
#创建队列
q = Queue(5)
print(q.empty())
#存数据
q.put('科比')
q.put('勒布朗')
q.put('JR')
q.put('汤普森')
print(q.qsize())
q.put('love')
print(q.full())
#取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get(False))
