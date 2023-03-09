import cv2
import numpy as np
import matplotlib.pyplot as plt


def mean(img):
    h, w = img.shape
    kernel = np.ones([3, 3], dtype=int)
    kernel = kernel/9
    img_new = np.zeros([h, w], dtype=np.uint8)

    for i in range(1, h-1):
        for j in range(1, w-1):
            temp = (img[i-1][j-1]*kernel[0, 0]+img[i-1][j]*kernel[0, 1]+img[i-1][j+1]*kernel[0, 2]+img[i][j-1]*kernel[1, 0]+img[i][j]*kernel[1, 1]+img[i][j+1]*kernel[1, 2]+img[i+1][j-1]*kernel[2, 0]+img[i+1][j]*kernel[2, 1]+img[i+1][j+1]*kernel[2, 2])
            img_new[i][j] = temp
            
    return img_new


def median(img):
    h, w = img.shape
    img_new = np.zeros([h, w], dtype=np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            temp = [img[i-1, j-1], img[i-1, j], img[i-1, j+1], img[i, j-1], img[i, j], img[i, j+1], img[i+1, j-1], img[i + 1, j], img[i+1, j+1]]
            temp = sorted(temp)
            img_new[i, j] = temp[4]
    return img_new


def max1(img):
    h, w = img.shape
    img_new = np.zeros([h, w], dtype=np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            temp = [img[i-1, j-1], img[i-1, j], img[i-1, j+1], img[i, j-1], img[i, j], img[i, j+1], img[i+1, j-1], img[i+1, j], img[i+1, j+1]]
            temp = max(temp)
            img_new[i, j] = temp
    return img_new


def min1(img):
    h, w = img.shape
    img_new = np.zeros([h, w], dtype=np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            temp = [img[i-1, j-1], img[i-1, j], img[i-1, j+1], img[i, j-1], img[i, j], img[i, j+1], img[i+1, j-1], img[i+1, j], img[i+1, j+1]]
            temp = min(temp)                       # use min(temp) for minimum filter
            img_new[i, j] = temp
    return img_new


def weighted_avg(kernal, img):
    m = int(np.floor(len(kernal) / 2))
    n = int(np.floor(len(list(zip(*kernal)))) / 2)
    k = np.sum(kernal)
    #print(k)
    rows, cols = img.shape                                                            
    blurred_img = np.zeros((rows, cols), np.uint8)                                    
    for i in range(m, rows - m):
        for j in range(n, cols - n):
            sum = 0
            for x in range(-m, m + 1, 1):
                for y in range(-n, n + 1, 1):
                    sum = sum + (img[i + x, j + y] * kernal[m - x][n - y])            
            sum = sum / k
            blurred_img[i, j] = sum
    return blurred_img


img = cv2.imread('rott.jpg', 0)
kernal1 = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]

weighted_avg = weighted_avg(kernal1, img)
mean = mean(img)
median = median(img)
max1 = max1(img)
min1 = min1(img)

fig = plt.figure(figsize=(16, 10))
plt_x = 2
plt_y = 3
fig.add_subplot(plt_x, plt_y, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original grey image")

fig.add_subplot(plt_x, plt_y, 2)
plt.imshow(mean, cmap="gray")
plt.axis("off")
plt.title("mean image")

fig.add_subplot(plt_x, plt_y, 3)
plt.imshow(median, cmap="gray")
plt.axis("off")
plt.title("median image")

fig.add_subplot(plt_x, plt_y, 4)
plt.imshow(max1, cmap="gray")
plt.axis("off")
plt.title("max image")

fig.add_subplot(plt_x, plt_y, 5)
plt.imshow(min1, cmap="gray")
plt.axis("off")
plt.title("min image")

fig.add_subplot(plt_x, plt_y, 6)
plt.imshow(weighted_avg, cmap="gray")
plt.axis("off")
plt.title("weighted average image")

plt.show()


