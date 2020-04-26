# 爬山法求八皇后问题

# -*- coding: utf-8 -*-

import random

'''启发值h'''


def get_number_of_conflict(status):
    num = 0
    for i in range(len(status)):
        for j in range(i + 1, len(status)):
            # 不能处于同一列
            if status[i] == status[j]:
                num += 1
            # 不能处于对角线
            if abs(status[i] - status[j]) == (j - i):
                num += 1
    return num


'''根据启发值爬山'''


def climbing_hill(status):
    # 来造一个字典，字典的键值是一个二维点坐标
    convert = {}
    length = len(status)
    for col in range(length):
        for row in range(length):
            if status[col] == row:
                continue
            # 替身攻击，这里牵涉到对status的更改，所以需要弄一个新的，不要破坏status
            status_copy = list(status)
            status_copy[col] = row
            # 对每一列，每个行数上都尝试放上一个皇后，更新皇后的位置,记录col列
            # 的第row行放置皇后产生的冲突数
            convert[(row, col)] = get_number_of_conflict(status_copy)
    answers = []
    conflict_now = get_number_of_conflict(status)
    # 第一次遍历，获得最小冲突值
    for key, value in convert.items():
        if value < conflict_now:
            conflict_now = value
    # 第二次遍历，获得冲突最少的点集合
    for key, value in convert.items():
        if value == conflict_now:
            # answers这个家伙就是个元组数组，里面的每个元素都是一个坐标
            answers.append(key)
    # 可能有好几个坐标点都能达到最小的冲突值
    # 随机取一个就行
    if len(answers) > 0:
        x = random.randint(0, len(answers) - 1)
        row = answers[x][0]
        col = answers[x][1]
        # 更新状态
        status[col] = row
    return status


def eight_queens():
    status = [0, 1, 2, 3, 4, 5, 6, 7]  # 初始化所有的八皇后在对角线
    while get_number_of_conflict(status) > 0:
        status = climbing_hill(status)
        print(status)
        print("conflict number: " + str(get_number_of_conflict(status)))
    print("answer:")
    print(status)


if __name__ == '__main__':
    eight_queens()
    
# [5, 0, 2, 3, 4, 2, 6, 7]
# conflict number: 11
# [5, 0, 1, 3, 4, 2, 6, 7]
# conflict number: 7
# [5, 0, 1, 1, 4, 2, 6, 7]
# conflict number: 5
# [5, 0, 1, 1, 4, 2, 6, 3]
# conflict number: 3
# [5, 0, 4, 1, 4, 2, 6, 3]
# conflict number: 2
# [5, 0, 4, 1, 7, 2, 6, 3]
# conflict number: 0
# answer:
# [5, 0, 4, 1, 7, 2, 6, 3]
#
