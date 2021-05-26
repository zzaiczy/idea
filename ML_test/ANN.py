import random
import math

# ————————————————————函数运算——————————————————————————


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_grad(mat):
    m, n = len(mat[0]), len(mat)
    x = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            x[i][j] = mat[i][j] * (1 - mat[i][j])
    return x


def mat_sigmoid(mat):
    m, n = len(mat[0]), len(mat)
    x = [[0.0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            x[i][j] = sigmoid(mat[i][j])
    return x


def trans_matrix(x):
    m, n = len(x[0]), len(x)
    y = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            y[j][i] = x[i][j]
    return y


def dot_matrix(x, y):
    assert len(x[0]) == len(y)
    z = [[0 for _ in range(len(y[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            tmp = 0
            for k in range(len(x[0])):
                tmp += x[i][k] * y[k][j]
            z[i][j] = tmp
    return z


def num_matrix(alfa, mat):
    m, n = len(mat[0]), len(mat)
    mat1 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mat1[i][j] = alfa * mat[i][j]
    return mat1


def multi_matrix(x, y):
    assert len(x[0]) == len(y[0]) and len(x) == len(y)
    z = [[0 for _ in range(len(x[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            z[i][j] = x[i][j] * y[i][j]
    return z


def add_vec(mat, vec):
    assert len(mat[0]) == len(vec)
    x = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(vec)):
            x[i][j] = mat[i][j] + vec[j]
    return x


def sub_mat(mat1, mat2):
    assert len(mat1[0]) == len(mat2[0]) and len(mat1) == len(mat2)
    mat = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat[i][j] = mat1[i][j] - mat2[i][j]
    return mat


def print_matrix(x):
    print(1111)
    if type(x[0]) == list:
        n, m = len(x), len(x[0])
        for i in range(n):
            for j in range(m):
                print(x[i][j], end=" ")
            print()
    else:
        for i in x:
            print(i, end=" ")
        print()
    return 1


def get_shape(mat):
    return len(mat), len(mat[0])


def mat_to_vec(mat):
    m, n = len(mat[0]), len(mat)
    mat1 = []
    for i in range(n):
        for j in range(m):
            mat1.append(mat[i][j])
    return mat1


class Ann:
    def __init__(self):
        self.layers_nums = 0
        self.layers = {}
        self.shape = {}
        self.result = {}
        self.act_grad = {}
        self.update = {}
        self.length = 0
        self.class_or_not = 1

    # -------------------------------------------------------构建网络----------------------------------------------
    def add_layer(self, left_num, right_num):
        # 增加新的层
        print("添加新的层%d" % (self.layers_nums + 1))
        xavier_initial = math.sqrt(6) / (left_num + right_num)
        layer = [[random.uniform(-xavier_initial, xavier_initial) for _ in range(left_num)] for _ in range(right_num)]
        bas = [[random.uniform(-xavier_initial, xavier_initial)] for _ in range(right_num)]
        self.layers[self.layers_nums] = [layer, bas]
        self.shape[self.layers_nums] = [left_num, right_num]
        self.layers_nums += 1
        print("初始化层权重完成...")
        return 1

    def init_param(self, x):
        self.result[0] = x
        return 1

    def loss_fuc(self, y, method="mse"):
        prep = self.result[self.layers_nums]
        length = len(prep)
        right_num = self.shape[self.layers_nums - 1][1]
        l_y = [[0 for _ in range(right_num)] for _ in range(length)]
        loss = 0
        if method == "mse":
            for i in range(length):
                for j in range(right_num):
                    loss += (prep[i][j] - y[i][j]) ** 2
                    l_y[i][j] = (prep[i][j] - y[i][j]) / length
        return l_y, loss / length

    def forward(self):
        # 向前传播
        # 输入 x.shape(N,3)
        # 输出 y.shape(N,1)
        for i in range(self.layers_nums):
            layer, bas = self.layers[i]
            # 计算向量内积
            a = trans_matrix(layer)
            ans1 = dot_matrix(self.result[i], a)
            bas1 = mat_to_vec(bas)
            ans2 = add_vec(ans1, bas1)
            if i == self.layers_nums - 1 and not self.class_or_not:
                self.result[i + 1] = ans2
                self.act_grad[i] = [[1 for i in range(len(ans2[0]))] for i in range(len(ans2))]
                break
            ans3 = mat_sigmoid(ans2)
            # 向前结果
            self.result[i + 1] = ans3
            # 本层sigmoid导数
            self.act_grad[i] = sigmoid_grad(ans3)
        return 1

    def back_forward(self, l_y):
        # 向后传播
        length = len(l_y)
        last = multi_matrix(l_y, self.act_grad[self.layers_nums - 1])
        for layer_num in range(self.layers_nums - 1, -1, -1):
            # 求参数梯度
            mat1 = trans_matrix(last)
            delta_w = dot_matrix(mat1, self.result[layer_num])
            ones = [[1]] * length
            delta_b = dot_matrix(mat1, ones)
            self.update[layer_num] = [delta_w, delta_b]

            # 求当前一层输出导
            if layer_num > 0:
                last0 = dot_matrix(last, self.layers[layer_num][0])
                last = multi_matrix(last0, self.act_grad[layer_num - 1])
        return 1

    def w_update(self, alfa):
        for layers_num in range(self.layers_nums):
            w2 = num_matrix(alfa, self.update[layers_num][0])
            b2 = num_matrix(alfa, self.update[layers_num][1])
            self.layers[layers_num][0] = sub_mat(self.layers[layers_num][0], w2)
            self.layers[layers_num][1] = sub_mat(self.layers[layers_num][1], b2)
        return 1

    def train(self, alfa, x, y, method="mse", class_or_not=1):
        # 参数准备
        length = len(x)
        assert length == len(y), "输入和输出不等长"
        self.length = length
        self.class_or_not = class_or_not
        assert self.init_param(x)
        step = 0
        last_loss = 0
        while True:
            assert self.forward(), "向前失败"
            l_y, loss = self.loss_fuc(y, method)
            if step % 100 == 0:
                print(loss)
            assert self.back_forward(l_y), "向后失败"
            assert self.w_update(alfa), "更新失败"
            if abs(last_loss - loss) < 10 ** -9:
                print("训练完成！")
                break
            last_loss = loss
            step += 1
        return 0


# --------------------------回归实例----------------------------
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = [[6], [15], [24]]
# ANN = Ann()
# ANN.add_layer(3, 4)
# ANN.add_layer(4, 5)
# ANN.add_layer(5, 1)
# ANN.train(0.03, x, y, "mse", 0)

# -------------------------分类实例-----------------------------
x0 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y0 = [[0], [0], [1]]
ANN = Ann()
ANN.add_layer(3, 4)
ANN.add_layer(4, 5)
ANN.add_layer(5, 1)
ANN.train(0.5, x0, y0, "mse", 1)
