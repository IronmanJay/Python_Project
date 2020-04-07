# 无参数的装饰器

def set_func(func):
    def call_func():
        print("----这是权限验证1----")
        print("----这是权限验证2----")
        func()
    return call_func

@set_func
def test1():
    print("----test1----")

if __name__ == '__main__':
    test1()