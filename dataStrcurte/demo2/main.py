from itertools import zip_longest

a = [i for i in range(10)]
b = [i for i in range(1, 9)]

for num1, num2 in zip_longest(a, b, fillvalue=-1):
    print(num1, num2)

str = 'python'
print(str[:2])
print(str[::2])
