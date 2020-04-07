import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downer(img_name,img_url):
    ret = urllib.request.urlopen(img_url)
    img_content = ret.read()
    with open(img_name,"wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downer,"1.jpg","https://rpic.douyucdn.cn/asrpic/200318/8103518_1239.png/dy1"),
        gevent.spawn(downer,"2.jpg","https://rpic.douyucdn.cn/asrpic/200318/5807021_1238.png/dy1")
    ])

if __name__ == '__main__':
    main()