
def create_num(all_num):
    a,b = 0,1
    current_num = 0
    while current_num < all_num:
        yield a # 如果一个函数中yield语句，那么这个就不是函数，就是一个生成器的模板
        a,b = b,a+b
        current_num += 1
    return "ok"

# 在调用create_num的时候，发现这个函数中有yield，那么现在就不是调用函数，而是创建一个生成器
obj1 = create_num(10)
for num in obj1:
    print(num)
print("-------------")
obj2 = create_num(10)
for num in obj2:
    print(num)
print("-------------")
obj3 = create_num(10)
while True:
    try:
        ret = next(obj3)
        print(ret)
    except Exception as ret:
        print("-------------")
        print(ret.value)
        break