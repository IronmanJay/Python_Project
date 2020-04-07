# 有参数的装饰器

def set_func(func):
    def call_func(num):
        print("----这是权限验证1----")
        print("----这是权限验证2----")
        func(num)
    return call_func

@set_func
def test1(num):
    print("----test1----%d" % num)

@set_func
def test2(num):
    print("----test2----%d" % num)

if __name__ == '__main__':
    test1(100)
    test2(200)