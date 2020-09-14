"""
    起点->终点
"""
print("Part1:")
print("负重上限1200千克，初始资金10000元，基础收益1000元，截止日期第30天")
road1 = [1, 25, 26, '27终点']
print(road1)
wx = 8 + 8 + 5
fx = 6 + 6 + 7
consume1 = [wx, fx]  # [21, 19]
print("分别花费：【水，食物】（箱）" + str(consume1))
post = consume1[0] * 5 + consume1[1] * 7  # 238元
print("花费：" + str(post) + "元")
weight = consume1[0] * 3 + consume1[1] * 2
print("配重：" + str(weight) + "kg")
print("剩余钱数：" + str(10000 - post) + "元")
