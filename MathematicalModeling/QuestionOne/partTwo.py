"""
    起点->矿山->终点
"""
# 返回对应天的天气消耗的食物和水和钱数的总和
def Consume(gx, qx, sx):
    if gx < 0:
        gx = 0
    if qx < 0:
        qx = 0
    if sx < 0:
        sx = 0
    water = gx * 8 + qx * 5 + sx * 10  # 箱数
    food = gx * 6 + qx * 7 + sx * 10  # 箱数
    money = water * 5 + food * 10  # 钱数
    return [money, water, food]

# 前十天消耗的数目，走到金矿应走了八天，有两天风暴，即走了十天
tenConsumeMoney = 2 * Consume(5, 3, 0)[0] + Consume(0, 0, 2)[0]
tenConsumeWater = 2 * Consume(5, 3, 0)[1] + Consume(0, 0, 2)[1]
tenConsumeFood = 2 * Consume(5, 3, 0)[2] + Consume(0, 0, 2)[2]
print("从起点到矿山十天消耗的水为：" + str(tenConsumeWater) + "箱，"
       "消耗的食物为" + str(tenConsumeFood) + "箱，消耗的钱为：" + str(tenConsumeMoney) + "元")
# 天气数组：晴朗->1；高温->2；沙暴->3；
weather = [2, 2, 1, 3, 1, 2, 3, 1, 2, 2,
           3, 2, 1, 2, 2, 2, 3, 3, 2, 2,
           1, 1, 2, 1, 3, 2, 1, 1, 2, 2]
# 最后结果
money2 = []
for n in range(0, 15):
    nweather = weather[10:10 + n + 1]
    # 采矿期间的各个天气占比
    sunNum = 0
    for i in nweather:
        if 1 == i:
            sunNum += 1
    hotNum = 0
    for i in nweather:
        if 2 == i:
            hotNum += 1
    stromNum = 0
    for i in nweather:
        if 3 == i:
            stromNum += 1

    # 判断后五天有几天是沙暴
    times = 5
    index = 9 + n + 1
    count = 0
    while times > 0:
        if weather[index] == 3:
            index += 1
            count += 1
        else:
            index += 1
            times -= 1

    # 最后五天金矿到终点的各个天气占比
    lastFiveDay = weather[9 + n + 1:15+n+count]
    print(lastFiveDay)
    sunNumLast = 0
    for i in lastFiveDay:
        if 1 == i:
            sunNumLast += 1
    hotNumLast = 0
    for i in lastFiveDay:
        if 2 == i:
            hotNumLast += 1
    stromNumLast = 0
    for i in lastFiveDay:
        if 3 == i:
            stromNumLast += 1

    # 总钱数
    allMoney = 10000
    # 在矿山赚的钱
    earn = n * 1000
    # 前十天晴朗和高温行走消耗的钱+前十天沙暴停留消耗的钱
    tenConsumeMoneySunAndHotAndStorm = 2 * Consume(5, 3, 0)[0] + Consume(0, 0, 2)[0]
    # 矿山挖矿消耗的钱
    MineConsume = 3 * Consume(hotNum, sunNum, stromNum - 1)[0] + Consume(1,0,0)[0]
    # 后五天晴朗和高温行走消耗的钱+后五天沙暴停留消耗的钱
    fiveConsumeMoneySunAndHotAndStorm = 2 * Consume(hotNumLast, sunNumLast, 0)[0] + Consume(0, 0, stromNumLast)[0]
    # 计算到终点的剩余钱数
    resultMoney = allMoney + earn - tenConsumeMoneySunAndHotAndStorm - MineConsume - fiveConsumeMoneySunAndHotAndStorm

    # 消耗水食物箱数
    # 前十天行走消耗的水+前十天停留消耗的水 + 后五天行走消耗的水+后五天停留消耗的水+挖矿消耗的水
    allConsumeWater = 2 * Consume(5, 3, 0)[1] + Consume(0, 0, 2)[1] + 2 * Consume(hotNumLast, sunNumLast, 0)[1] + Consume(0, 0, stromNumLast)[1] + 3 * Consume(hotNum, sunNum, stromNum - 1)[1] + Consume(1,0,0)[1]
    # 前十天行走消耗的食物+前十天停留消耗的食物 + 后五天行走消耗的食物+后五天停留消耗的食物
    allConsumeFood = 2 * Consume(5, 3, 0)[2] + Consume(0, 0, 2)[2] + 2 * Consume(hotNumLast, sunNumLast, 0)[2] + Consume(0, 0, stromNumLast)[2] + 3 * Consume(hotNum, sunNum, stromNum - 1)[2] + Consume(1,0,0)[2]
    print("第" + str(n + 1) + "天共消耗水：" + str(allConsumeWater) + "箱，共消耗食物" + str(allConsumeFood) + "箱")
    money1 = [n + 1, resultMoney]
    # 如果超载，将剩余钱数定为-10000
    if (allConsumeFood * 2 + allConsumeWater * 3) > 1200:
        money1 = [n + 1, 0]
    money2.append(money1)
print(money2)
