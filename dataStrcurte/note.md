# 数据结构

## 字符串

```text
1.去除空白字符
  #strip函数的作用就是去除字符串首尾的所有空白字符。不会去除掉字符串之间的空白字符
  " a b c ".strip()  #结果'a b c'
  #lstrip 和 rstrip 函数，分别去除字符串左边和右边的空白字符
  " abc ".lstrip() # 结果'abc '
 " abc ".rstrip() # 结果' abc'
 
 2.大小写
 # 将所有字符变成大写
 "china".upper() # CHINA
 # 将字符串的首字母变成大写
 "china".capitalize() # China
 # 将所有字符变成小写
 "CHINA".lower() # china
 # 将每个单词的首字母变成大写
 "i have a dream".title() # I Have A Dream
 
 3.判断字符串是否以指定的字符串开头或者结尾
 startswith  #是否以指定的字符串开头
 endswith  #是否以指定的字符串结尾
 isdigit  #是否是一串数字
 islower  #是否全是小写字母
 isupper  #是否全是大写字母
 
 4.字符串长度 len
 len("China") # 5
 #len() 也可以测量其他所有有长度的对象
 r = range(10)
 len(r) # 10
 
 5.查找函数：find、index--find若找到返回第一个字母索引，没找到返回-1；index若梅找到会报错；
 s.find("not_exists") # 结果是-1
 
 6.计数count
 "abba".count('a') # 2
 
 7.替换函数replace
 "abba".replace('a', 'b') # 结果是'bbbb'
 'apple banana'.replace('apple', 'orange')  # 结果是'orange banana'
```

## 元组

字符串是一种序列，他可以迭代、按索引访问、切片访问。但他的组成只能是单个的字符，又是有了更多元化的序列；远足
元祖和字符串都是只读的，也就是不可修改的

## 列表

## 字典

## 集合



