import random


# 一、爬山法简介
#
# 爬山法（climbing method）是一种优化算法，其一般从一个随机的解开始，然后逐步找到一个最优解（局部最优）。
# 假定所求问题有多个参数，我们在通过爬山法逐步获得最优解的过程中可以依次分别将某个参数的值增加或者减少一个
# 单位。例如某个问题的解需要使用3个整数类型的参数x1、x2、x3，开始时将这三个参数设值为(2,2,-2)，将x1增加/减少1，
# 得到两个解(1,2,-2), (3, 2,-2)；将x2增加/减少1，得到两个解(2,3, -2)，(2,1, -2)；将x3增加/减少1，得到两个解
# (2,2,-1)，(2,2,-3)，这样就得到了一个解集：
# (2,2,-2), (1, 2,-2), (3, 2,-2), (2,3,-2), (2,1,-2), (2,2,-1), (2,2,-3)
# 从上面的解集中找到最优解，然后将这个最优解依据上面的方法再构造一个解集，再求最优解，就这样，直到前一次的最优解和后一次的最优解相同才结束“爬山”。
#
# 二、Python实例
#
# 设方程 y = x1+x2-x3，x1是区间[-2, 5]中的整数，x2是区间[2, 6]中的整数，x3是区间[-5, 2]中的整数。使用爬山法，找到使得y取值最小的解。

def evaluate(x1, x2, x3):
    return x1 + x2 - x3


if __name__ == '__main__':
    x_range = [[-2, 5], [2, 6], [-5, 2]]
    best_sol = [random.randint(x_range[0][0], x_range[0][1]),
                random.randint(x_range[1][0], x_range[1][1]),
                random.randint(x_range[2][0], x_range[2][1])]

    while True:                                                                      # 1.LOOP DO
        best_evaluate = evaluate(best_sol[0], best_sol[1], best_sol[2])
        current_best_value = best_evaluate
        sols = [best_sol]

        for i in range(len(best_sol)):                                                #
            if best_sol[i] > x_range[i][0]:                                           #
                print("大于：")                                                       #
                print("best_sol[" + str(i) + "] = ", best_sol[i])                     #
                print("x_range[" + str(i) + "][0] = ", x_range[i][0])                 #
                sols.append(best_sol[0:i] + [best_sol[i] - 1] + best_sol[i + 1:])     # ---> 2.extend the neighbor
            if best_sol[i] < x_range[i][1]:                                           # ---> this step isn't in book
                print("小于：")                                                        #
                print("best_sol[" + str(i) + "] = ", best_sol[i])                      #
                print("x_range[" + str(i) + "][0] = ", x_range[i][1])                  #
                sols.append(best_sol[0:i] + [best_sol[i] + 1] + best_sol[i + 1:])      #
            print("结果：")
            print(sols)
        print("本次循环结束，sols扩展为：")
        print(sols)
        for s in sols:
            el = evaluate(s[0], s[1], s[2])
            if el < best_evaluate:
                best_sol = s
                best_evaluate = el            # 3.找到和最小的那个解
        if best_evaluate == current_best_value:  # 5.如果这个和跟上一次相同，估计是到了最小点了，可以返回
            print("找到最优解，结束while循环")
            break
        print("挑选出本次最优解：", best_sol)  # 4.更新目前的最优解

    print('best sol：', current_best_value, best_sol)
