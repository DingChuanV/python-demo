from random import randint


# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# print(roll_dice())
# print(roll_dice(3))


def fun(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    vari1 = num1 * num2  # 计算出两个整数的乘积,方便后面计算最小公倍数
    vari2 = num1 % num2  # 对2个整数进行取余数

    while vari2 != 0:  # 判断余数是否为0, 如果不为0,则进入循环
        num1 = num2  # 重新进行赋值,进行下次计算
        num2 = vari2
        vari2 = num1 % num2  # 对重新赋值后的两个整数取余数

    vari1 /= num2  # 得出最小公倍数
    print("最大公约数为:%d" % num2)  # 输出
    print("最小公倍数为:%d" % vari1)  # 输出


fun(6, 9)
