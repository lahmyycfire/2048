import random
import time
import os


# 用4个数组来保存数据
list1 = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]

# print(list1[2][1])

# 生成2和4， 2的权重70%, 4的权重%30
def random_weights(choice={'4': 30, '2': 70,}):
    sum_weights = sum(choice.values())
    rn = random.uniform(0, sum_weights)
    # print(sum, rn)
    res = None
    curr_weight = 0
    for k in choice.keys():
        curr_weight = curr_weight + choice[k]
        # print(curr_weight)
        if rn < curr_weight:
            res = k
            break

    # print(rn, curr_weight)
    return res


# a = random_weights()
# print(a)

# 打印
def draw():
    for j in range(0, 4):
        for k in range(0, 4):
            if k == 3:
                print(list1[j][k])
            else:
                print(list1[j][k], end='  ')

    print('--------------------------')

# 更新数字
def data_op(x, y, direct, a):
    pass

# main
def main():
    while True:
        draw()
        time.sleep(1)
        draw()
        break


if __name__ == '__main__':
    main()