import redis

if __name__ == '__main__':
    try:
        #密码
        password = '990929'
        #创建一个StrictRedis对象，连接redis数据库
        sr = redis.Redis(host='localhost', port=6379, db=15,password=password)
        # 添加一个key，为name，value itheima
        res = sr.set('name','itheima')
        print(res)
        #获取name的值
        res = sr.get('name')
        print(res)
        # 删除name及对应的值
        res = sr.delete('name')
        print(res)
        # 获取数据库中所有的键
        res = sr.keys()
        print(res)
    except Exception as e:
        print(e)

