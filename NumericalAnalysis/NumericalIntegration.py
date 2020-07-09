import math

"""测试函数"""
def f(x,i):
  if i == 1:
    return (4 - (math.sin(x)) ** 2) ** 0.5
  if i == 2:
    if x == 0:
      return 1
    else:
      return math.sin(x) / x
  if i == 3:
    return (math.exp(x)) / (4 + x ** 2)
  if i == 4:
    return math.log(1+x,math.e) / (1 + x ** 2)

"""打印显示函数"""
def p(i,n):
  return "第" + str(i) + "题,n=" + str(n) + "时的积分值为："

"""复化Simpson函数"""
def Simpson(a, b, n, i):
  h = (b - a) / (2 * n)
  F0 = f(a,i) + f(b,i)
  F1 = 0
  F2 = 0
  for j in range(1,2 * n):
    x = a + (j * h)
    if j % 2 == 0:
      F2 = F2 + f(x,i)
    else:
      F1 = F1 + f(x,i)
  SN = (h * (F0 + 2 * F2 + 4 * F1)) / 3
  print("复化Simpson函数" + p(i,n) + str("%-10.7f"%(SN)))
  return SN

def T(a, b, n, i):
  h = (b - a) / n
  F0 = f(a,i) + f(b,i)
  F = 0
  for j in range(1,n):
    x = a + (j * h)
    F = F + f(x,i)
  SN = (h * (F0 + 2 * F)) / 2
  print("复化梯形函数" + p(i,n) + str("%-10.7f"%(SN)))
  return SN

def SimpsonTimes(x):
  n = 1
  y = Simpson(0, math.pi/4, n, 1)
  while(abs(y - 1.5343916) > x):
    n = n + 1
    y = Simpson(0, math.pi/4, n, 1)
  else:
    return n

def Times(x):
  n = 1
  y = T(0, math.pi/4, n, 1)
  while(abs(y - 1.5343916) > x):
    n = n + 1
    y = T(0, math.pi/4, n, 1)
  else:
    return n


"""测试部分"""
Simpson(0, math.pi/4, 10, 1)
Simpson(0, 1, 10, 2)
Simpson(0, 1, 10, 3)
Simpson(0, 1, 10, 4)
Simpson(0, math.pi/4, 20, 1)
Simpson(0, 1, 20, 2)
Simpson(0, 1, 20, 3)
Simpson(0, 1, 20, 4)

T(0, math.pi/4, 10, 1)
T(0, 1, 10, 2)
T(0, 1, 10, 3)
T(0, 1, 10, 4)
T(0, math.pi/4, 20, 1)
T(0, 1, 20, 2)
T(0, 1, 20, 3)
T(0, 1, 20, 4)

print("复化梯形函数求解第一问，精度为0.00001时需要" + str(Times(0.00001)) + "个步数")
print("复化Simpson函数求解第一问，精度为0.00001时需要" + str(SimpsonTimes(0.00001)) + "个步数")
print("复化梯形函数求解第一问，精度为0.000001时需要" + str(Times(0.000001)) + "个步数")
print("复化Simpson函数求解第一问，精度为0.000001时需要" + str(SimpsonTimes(0.000001)) + "个步数")