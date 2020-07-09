import matplotlib.pyplot as plt
import numpy as np

# 可以显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False

# 设置风格
plt.style.use('ggplot')


class QuadraticSplineinter():

    def __init__(self):
        self.x_train = None  # 训练数据
        self.X = None  # 系数矩阵
        self.Y = None  # f(x)
        self.W = None  # 系数求值
        self.N = None  # 区间个数

    def fit(self, x, y):  # 0-n
        self.x_train = x
        self.N = len(x) - 1
        self.X = np.zeros([3 * (self.N) - 1, 3 * (self.N)])
        self.Y = np.zeros([3 * (self.N) - 1, 1])
        j = 0

        # 1-n-1 前2n-2个
        for i in range(self.N - 1):
            self.Y[2 * i] = y[i + 1]
            self.Y[2 * i + 1] = y[i + 1]
            #            label_y=i*2+1
            if j > 1:  # 两个多项式相邻时候使用使对齐
                j -= 1
            for p in range(2):
                self.X[2 * i + p, 3 * j] = x[i + 1] ** 2
                self.X[2 * i + p, 3 * j + 1] = x[i + 1]
                self.X[2 * i + p, 3 * j + 2] = 1
                j += 1
        # 填充外点2个
        self.Y[2 * self.N - 2] = y[0]
        self.X[2 * self.N - 2, 0] = x[0] ** 2
        self.X[2 * self.N - 2, 1] = x[0]
        self.X[2 * self.N - 2, 2] = 1

        self.Y[2 * self.N - 1] = y[-1]
        self.X[2 * self.N - 1, -3] = x[-1] ** 2
        self.X[2 * self.N - 1, -2] = x[-1]
        self.X[2 * self.N - 1, -1] = 1
        # 填充后n-1个，一介导0-2n-1已经填充
        # Y在这一段为0
        j = 0
        for i in range(self.N - 1):
            self.X[i + 2 * self.N, 3 * j + 0] = x[i + 1] * 2
            self.X[i + 2 * self.N, 3 * j + 1] = 1
            #   X[i+2*N,3*j+2]=0
            self.X[i + 2 * self.N, 3 * j + 3] = -x[i + 1] * 2
            self.X[i + 2 * self.N, 3 * j + 4] = -1
            j += 1

        self.X = np.mat(self.X[:, 1:])
        self.Y = np.mat(self.Y)
        self.W = np.array(self.X.I * self.Y).reshape(-1)

    def predict(self, X_pre):
        if type(X_pre) != np.ndarray:
            X_pre = np.array(X_pre)

        def fun(x):
            for i in range(self.N):
                if self.x_train[i] <= x and x <= self.x_train[i + 1]:
                    if i == 0:  # 第一条直线
                        return self.W[0] * x + self.W[1]
                    else:  # 之后为二次

                        return self.W[i * 3 - 1] * x ** 2 + self.W[i * 3] * x + self.W[i * 3 + 1]

        return np.array([fun(i) for i in X_pre])


if __name__ == "__main__":
    # 原始数据
    x = [3, 4.5, 6, 7, 9, 12]

    y = [2.5, 1, 2.5, 1, 0.5, 2.1]
    # X_pre要求必须在训练的x范围内
    X_pre = np.linspace(x[0], x[-1], 100)

    model = QuadraticSplineinter()
    model.fit(x, y)
    y_pre = model.predict(X_pre)

    fig = plt.figure(figsize=(6, 8))
    plt.subplot(2, 1, 1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('原散点图像')
    plt.scatter(x, y)

    print("参数")
    print(model.W)
    plt.subplot(2, 1, 2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('二次样条插值图像')
    plt.scatter(x, y, c='black')
    plt.plot(X_pre, y_pre)
    plt.show()