# 加/减/乘/除：+，-，*，/
# 取模：%
# 指数：**
# 取整除：//
# 小括号：（）

# 赋值运算符：（算数运算符的基础上，加个=）
# 如：
# 加 / 减 乘 / 除 /取整除法
# 赋值运算符：
# +=、
# -=、
# *=、
# /=、
# //=

# 判断奇偶数
# num = 4

# 1. if...else...语句
# 通过取模运算判断num是否能被2整除
# if num % 2 == 0:
#     print(str(num) + "是一个偶数")
# else:
#     print(str(num) + "是一个奇数")
# 2. elif语句
# score = 89
# if score < 60:
#     print("您的考试成绩不及格")
# elif score < 90:
#     print("您的成绩合格")
# else:
#     print("您的考试成绩优秀")
# 3. if条件嵌套
# score = 88
# if score >= 60:
#     if score >= 70:
#         print("合格")
#     elif score < 90:
#         print("良好")
#     else:
#         print("yum")
# else:
#     print("不及格")

# 键盘输入
# name = input("请输入name")
# print(name)

# 摄氏度和华氏度相互转换
# a = int(input('摄氏度转换为华氏温度请按1\n华氏温度转化为摄氏度请按2\n'))
# while a != 1 and a != 2:
#     a = int(input('你选择不正确，请重新输入。\n摄氏度转换为华氏温度请按1\n华氏温度转换为摄氏度请按2\n'))
# if a == 1:
#     celsius = float(input('输入摄氏度:'))
#     # 计算华氏温度
#     fahrenheit = (celsius * 1.8) + 32
#     print('%.1f摄氏度转为华氏温度为%.1f' % (celsius, fahrenheit))
# else:
#     fahrenheit = float(input('输入华氏度:'))
#     # 计算摄氏度
#     celsius = (fahrenheit - 32) / 1.8
#     print('%.1f华氏度转为摄氏度为%.1f' % (fahrenheit, celsius))

# 自动类型转换
# if 和 elif 的后面总跟着一个表达式，这个表达式的结果必须是True或者False，
# 如果表达式运算出来的 结果不是一个布尔值，则会自动将结果转换为布尔值，无论它是什么类型的值;
# count = 1
# if count:
#     print("ok")
# else:
#     print("no")


# 循环语句
# while 语句
# 循环打印建国喝了1-10杯酒；
# glass = 0
# while glass < 10:
#     glass += 1
#     print(str(glass))


# for循环
# seq = "hello"
# for s in seq:
#     print(s)
#

# for循环打印一连串的数字
# for i in range(5):
#     print(i)

# 打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%s*%s=%s" % (j, i, i * j), end=" ")
#     print()

# break 和 continue
# s = "14.9237834829"
# for i in s:
#     if i == '.':
#         print()
#         break
#     print(i, end=" ")

total = 0
for i in range(11):
    if i % 2 == 1:
        continue
    print(i, end="+")
    total += i
print("=%s" % total)


