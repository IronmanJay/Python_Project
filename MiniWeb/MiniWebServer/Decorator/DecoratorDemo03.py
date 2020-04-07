# 对不定长参数的函数装饰

def set_func(func):
    def call_func(*args,**kwargs):
        print("----这是权限验证1----")
        print("----这是权限验证2----")
        func(*args,**kwargs)
    return call_func

@set_func
def test1(num,*args,**kwargs):
    print("----test1----%d" % num)
    print("----test1----",args)
    print("----test1----",kwargs)

if __name__ == '__main__':
    test1(100,200,300,mm=100)