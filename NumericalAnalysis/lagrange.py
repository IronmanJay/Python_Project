import matplotlib.pyplot as plt
import math

# 给出一组数据进行lagrange插值，同时将结果用plot展现出来
def lagrange(x_,y,a):
    """
    获取拉格朗日插值
    :param x_: x的列表值
    :param y: y的列表值
    :param a: 需要插值的数
    :return: 返回插值结果
    """
    ans = 0.0
    for i in range(len(y)):
        t_ = y[i]
        for j in range(len(y)):
            if i != j:
                t_ *= (a - x_[j] / (x_[i] - x_[j]))
            ans += t_
    return ans

def draw_picture(x_list,y_list,node):
    plt.title("lagrange")
    plt.xlabel("x")
    plt.ylabel("y")
    for i in range(len(x_list)):
        plt.scatter(x_list[i],y_list[i],color="purple",linewidths=2)
    plt.scatter(node[0],node[1],color="blue",linewidths=2)
    plt.show()

if __name__ == '__main__':
    x = 0.54
    x_1 = [0.4, 0.5, 0.6, 0.7, 0.8]
    y_1 = [-0.9163, -0.6931, -0.5108, -0.3567, -0.2231]
    lagrange = lagrange(x_1,y_1,x)
    print("拉格朗日插值:{}".format(lagrange))
    # 画图
    draw_picture(x_1, y_1, (x, lagrange))