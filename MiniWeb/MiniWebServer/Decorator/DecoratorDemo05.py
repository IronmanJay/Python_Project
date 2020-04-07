# 多个装饰器对同一个函数装饰

def set_qx(func):
    print("开始进行装饰权限1的功能")
    def call_func(*args,**kwargs):
        print("----这是权限验证1----")
        return func(*args,**kwargs)
    return call_func

def add_func(func):
    print("开始进行装饰权限2的功能")
    def call_func(*args,**kwargs):
        print("----这是权限验证2----")
        return func(*args,**kwargs)
    return call_func

@set_qx
@add_func
def test1():
    print("----test1----")

if __name__ == '__main__':
    test1()
