import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def filter(kx, ky, img):
    m = int(np.floor(len(kx) / 2))
    n = int(np.floor(len(list(zip(*kx)))) / 2)
    rows, cols = img.shape
    filtered_img = np.zeros((rows, cols), np.uint8)
    for i in range(m, rows - m):
        for j in range(n, cols - n):
            sumx = sumy = 0
            for x in range(-m, m + 1, 1):
                for y in range(-n, n + 1, 1):
                    sumx = sumx + (img[i + x, j + y] * kx[m + x][n + y])
                    sumy = sumy + (img[i + x, j + y] * ky[m + x][n + y])
            filtered_img[i, j] = abs(sumx) + abs(sumy)
    return filtered_img


img = cv.imread("scarlett.jpg", 0)

y = [[0, 0, 0], [0, -1, 0], [0, 0, 1]]
x = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
robert = filter(x, y, img)
y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
sobel = filter(x, y, img)
y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
prewitt = filter(x, y, img)

fig = plt.figure(figsize=(17, 12))
fig.add_subplot(2, 2, 1)
plt.imshow(img)
plt.axis('off')
plt.title('Original image')

fig.add_subplot(2, 2, 2)
plt.imshow(robert)
plt.axis('off')
plt.title('Robert filter')

fig.add_subplot(2, 2, 3)
plt.imshow(sobel)
plt.axis('off')
plt.title('Sobel filter')

fig.add_subplot(2, 2, 4)
plt.imshow(prewitt)
plt.axis('off')
plt.title('Prewitt filter')

plt.show()
