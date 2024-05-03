import cv2

# 读取照片
image = cv2.imread('/Users/dingchuan/Desktop/image-20240203201412018.png')  # 替换 'photo.jpg' 为你的照片文件名

# 将照片转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 保存灰度图像像素值到文本文件
with open('photo_gray.txt', 'w') as file:
    for row in gray_image:
        for pixel in row:
            file.write(str(pixel) + ' ')
        file.write('\n')
