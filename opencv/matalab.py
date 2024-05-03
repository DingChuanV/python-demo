import numpy as np
import matplotlib.pyplot as plt

# 读取数据
data = np.loadtxt(
    '/Users/dingchuan/Documents/Repos/python-demo/opencv/photo_gray.txt')  # 假设数据存储在名为 data.txt 的文本文件中，每行包含时间戳和数据值，用空格或制表符分隔

# 提取时间戳和数据值
timestamps = data[:, 0]
values = data[:, 1]

# 绘制折线图
plt.plot(timestamps, values)
plt.xlabel('时间戳')
plt.ylabel('数据值')
plt.title('数据随时间的变化')
plt.grid(True)
# 设置全局字体
plt.rcParams['font.family'] = 'Arial Unicode MS'
# 显示图表
plt.show()

# 保存图表为图片文件
plt.savefig('plot.png')  # 保存为 PNG 图片文件
