import table_xy
x,y = table_xy.table_xy()

#字典中x 与 y相互对应
d = {i:j for i,j in zip(x,y)}

def x_Averaging():
    sum_x = 0
    for i in d:
        sum_x += i
    return sum_x / len(d)

def y_Averaging():
    sum_y = 0
    for i in d:
        sum_y += d[i]
    return sum_y / len(d)

# 计算b的值
def b():
    son = 0
    mom = 0
    for i in d:
        son += ((i - x_Averaging()) * (d[i] - y_Averaging()))
        mom += ((i - x_Averaging()) * (i - x_Averaging()))
    # return son / mom
    return float('{:.3f}'.format(son / mom))

# 计算a的值
def a():
    # return y_Averaging() - (b() * x_Averaging())
    return float('{:.3f}'.format(y_Averaging() - (b() * x_Averaging())))

def main(x):
    # print('x平均值为：' + str(x_Averaging()))
    # print('y平均值为：' + str(y_Averaging()))
    # print('a的值为：' + str(a()))
    # print('b的值为：' + str(b()))

    # return b() * x + a()
    return float('{:.3f}'.format(b() * x + a()))

def ab():
    return a(),b()