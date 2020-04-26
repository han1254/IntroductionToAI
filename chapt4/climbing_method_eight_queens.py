# -*- coding: utf-8 -*-

import random

# 函数一:参数为当前棋盘布局状态，根据布局判断当前八皇后布局存在冲突的皇后对数
def get_numof_conflict(status):
    num = 0
    for i in range(len(status)):
        for j in range(i + 1, len(status)):

            if status[i] == status[j]:
                num += 1
            offset = j - i
            if abs(status[i] - status[j]) == offset:
                num += 1
    return num


# 函数二：参数为当前棋盘布局状态，利用爬山法思想选择邻居状态最好的布局并返回
def hill_climbing(status):
    convert = {}
    length = len(status)
    for col in range(length):
        best_move = status[col]
        for row in range(length):
            if status[col] == row:
                continue
            status_copy = list(status)
            status_copy[col] = row
            convert[(col, row)] = get_numof_conflict(status_copy)

    answers = []  # 最佳后继集合
    conflict_now = get_numof_conflict(status)  # 当前皇后冲突对数

    # 遍历存储所有可能后继的字典，找出最佳后继
    for key, value in convert.items():
        if value < conflict_now:
            conflict_now = value
    for key, value in convert.items():
        if value == conflict_now:
            answers.append(key)

    # 如果最佳后继集合元素大于一个 随机选择一个
    if len(answers) > 0:
        x = random.randint(0, len(answers) - 1)
        col = answers[x][0]
        row = answers[x][1]
        status[col] = row

    return status


# 函数三：求得八皇后满足冲突数为0的一个解，循环输出每一步的后继集合 直到不存在冲>突为止
def Queens():
    status = [0, 1, 2, 3, 4, 5, 6, 7]  # 初始状态所有皇后都在对角线

    # 当存在冲突的个数大于0时 循环求解最佳后继 直到找到八皇后解
    while get_numof_conflict(status) > 0:
        status = hill_climbing(status)
        print(status)
        print (get_numof_conflict(status))
    print("the answer is\n")
    print(status)


if __name__ == '__main__':
    Queens()
