import random


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


a = random_weights()
print(a)

# 画
def draw():
    pass

# main
def main():
    while True:
        pass