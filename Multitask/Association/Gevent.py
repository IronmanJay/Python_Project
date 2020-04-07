import gevent
from gevent import monkey
import time

monkey.patch_all()

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        # gevent.sleep(0.5)
        time.sleep(0.5)

gevent.joinall([
    gevent.spawn(f,5),
    gevent.spawn(f,5),
    gevent.spawn(f,5)
])