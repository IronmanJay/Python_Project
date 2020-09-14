"""
    起点->村庄->矿山->村庄->终点
"""


# 返回对应天的天气消耗的食物和水和钱数的总和
def Consume(gx, qx, sx):
    water = gx * 8 + qx * 5 + sx * 10  # 箱数
    food = gx * 6 + qx * 7 + sx * 10  # 箱数
    money = water * 5 + food * 10  # 钱数
    return [money, water, food]


# 前八天消耗的数目，到达村庄需要八天
eightConsumeMoney = 2 * Consume(3, 3, 0)[0] + Consume(0, 0, 2)[0]
eightConsumeWater = 2 * Consume(3, 3, 0)[1] + Consume(0, 0, 2)[1]
eightConsumeFood = 2 * Consume(3, 3, 0)[2] + Consume(0, 0, 2)[2]
print("从起点到村庄八天消耗的水为：" + str(eightConsumeWater) + "箱，""消耗的食物为" + str(eightConsumeFood) + "箱，消耗的钱为：" + str(
    eightConsumeMoney) + "元")
tenMoneyAfter = 10000 - eightConsumeMoney
print("到达村庄还剩" + str(tenMoneyAfter) + "元")
FoodStart = (1200 - (98 * 3)) / 2
print("起点购买食物" + str(FoodStart) + "箱")
WaterStart = 98
print("起点购买水" + str(WaterStart) + "箱")
FoodValage = 453 - eightConsumeFood
print("到达村庄还剩食物" + str(FoodValage) + "箱")
waterValage = 98 - eightConsumeWater
print("到达村庄还剩水" + str(waterValage) + "箱")
ValageAfter = 1200 - FoodValage * 2
print("到达村庄还可负重" + str(ValageAfter) + "千克")
waterAdd = ValageAfter / 3
print("如果在村庄全部补水，需要补水" + str(round(waterAdd)) + "箱" + "，花费" + str(163 * 5 * 2) + "元")
print("此时准备从村庄走还剩水" + str(153) + "箱" + "，还剩食物" + str(345) + "箱" + "，还剩金钱" + str(8530 - 1630) + "元")
print("====================================================================")
# 从起点经过村庄到达矿山还剩多少水
mRemainWater = 153 - (2 * 5 + 2 * 8)
# 从起点经过村庄到达矿山还剩多少食物
mRemainFood = 355 - (2 * 6 + 2 * 7)
# 从起点经过村庄到达矿山还剩多少钱
mRemainMoney = 6900
print("从起点经过村庄到达矿山还剩的水为：" + str(mRemainWater) + "箱，""剩余的食物为" + str(mRemainFood) + "箱，剩余的的钱为：" + str(mRemainMoney) + "元")
print("====================================================================")
# 可求全部买水效益最大
# 天气数组：晴朗->1；高温->2；沙暴->3；
weather = [2, 2, 1, 3, 1, 2, 3, 1, 2, 2,
           3, 2, 1, 2, 2, 2, 3, 3, 2, 2,
           1, 1, 2, 1, 3, 2, 1, 1, 2, 2]
# 最后结果
money2 = []
for n in range(1, 16):
    nweather = weather[10:10 + n]
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

    # 在矿山消耗的水
    MineConsumeWater = 3 * Consume(hotNum, sunNum, stromNum)[1] + Consume(1, 0, 0)[1]
    # 在矿山消耗的食物
    MineConsumeFood = 3 * Consume(hotNum, sunNum, stromNum)[2] + Consume(1, 0, 0)[2]

    # 总钱数
    allMoney = 6900
    # 在矿山赚的钱
    earn = n * 1000
    resMoney = allMoney + earn
    money1 = [n, resMoney]
    # 如果超载，break
    # if MineConsumeWater > 127 or MineConsumeFood > 329:
    #     break
    money2.append(money1)
    print("矿山工作第" + str(n) + "天后还剩水" + str(127 - MineConsumeWater) + "箱")
    print("矿山工作第" + str(n) + "天后还剩食物" + str(329 - MineConsumeFood) + "箱")
print(money2)
print("====================================================================")
print("第三天回到村庄还剩水" + str(24) + "箱")
print("第三天回到村庄还剩食物" + str(242) + "箱")
print("第三天回到村庄还剩钱" + str(9900) + "元")
print("=====================================================================")

# 如果此时直接回终点，先需要补充水，在第17天回到终点
print("如果此时直接回终点，先需要补充水，补充之后还剩" + str(32) + "箱")
print("那么还剩钱" + str(9900 - 8 * 10) + "元")
print("到终点还剩食物" + str(242 - 16) + "箱")
# 如果直接到终点还剩下面这些钱
print("如果从村庄直接返回终点剩余" + str(9700 + 226 * 5))

# 如果此时回矿山全部补充水
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("回到村庄后全部补充水，补充之后还剩水" + str(round((1200 - 24 - 242 * 2) / 3 + 24)) + "箱")
print("回到村庄后不再补充食物，还剩食物" + str(242) + "箱")
print("回到村庄补充之后，还剩钱" + str(9900 - 231 * 5) + "元")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# 第19天回到矿山
print("回到矿山水还剩" + str(223) + "箱")
print("回到矿山食物还剩" + str(218) + "箱")
# 最后结果
money3 = []
for n in range(1, 9):
    nweather = weather[17:17 + n]
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

    # 挖矿消耗的水
    MineConsumeWater = 3 * Consume(hotNum, sunNum, stromNum)[1] + Consume(0,0,1)[1]
    # 挖矿消耗的食物
    MineConsumeFood = 3 * Consume(hotNum, sunNum, stromNum)[2] + Consume(0,0,1)[2]

    # 总钱数
    allMoney = 8745
    # 在矿山赚的钱
    earn = n * 1000
    resultMoney = allMoney + earn
    money1 = [n, resultMoney]
    # 如果食物或者水耗尽，break
    if MineConsumeWater > 223 or MineConsumeFood > 218:
        break
    money3.append(money1)
    print("矿山工作" + str(n) + "天后还剩水" + str(223 - MineConsumeWater) + "箱")
    print("矿山工作" + str(n) + "天后还剩食物" + str(218 - MineConsumeFood) + "箱")
print(money3)
# 最后五天回到终点，先经过村庄补水
print("回到村庄剩水" + str(10) + "箱")
print("需补充水" + str(32) + "箱")
print("回到终点剩食物" + str(5) + "箱")
print("需要补食物" + str(33) + "箱")
print("最终剩余" + str(16745 - 32 * 10 - 33 * 20) + "元")
