import cv2
import numpy as np
import matplotlib.pyplot as plt


def normalisation(img):
    row, col = img.shape
    normalized_img = np.zeros((row, col), dtype=np.uint8)
    m = np.min(img)
    n = np.max(img)

    for i in range(row):
        for j in range(col):
            c = (255 * (img[i, j] - m) / (n - m)).astype(int)
            normalized_img[i, j] = c

    return normalized_img


def addition(img1, img2):
    img3 = np.zeros(img2.shape, dtype=np.uint8)
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            img3[i, j] = img1[i][j] + img2[i][j]

    return normalisation(img3)


def subtraction(img1, img2):
    img3 = np.zeros(img2.shape, dtype=np.uint8)
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            if img1[i, j] > img2[i, j]:
                img3[i, j] = img1[i, j] - img2[i, j]
            else:
                img3[i, j] = img2[i, j] - img1[i, j]
    return normalisation(img3)


def multiplication(img1, img2):
    row, col = img1.shape
    img3 = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            img3[i, j] = img1[i, j] * img2[i, j]
    return normalisation(img3)


def division(img1, img2):
    row, col = img1.shape
    img3 = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            img3[i, j] = img1[i, j] / img2[i, j]
    return normalisation(img3)


img1 = cv2.imread('kash.jpg', 0)
img2 = cv2.imread('kash1.jpg', 0)
add = addition(img1, img2)
subtract = subtraction(img1, img2)
multiply = multiplication(img1, img2)
divide = division(img1, img2)

fig = plt.figure(figsize=(16, 10))
plt_x = 2
plt_y = 3
fig.add_subplot(plt_x, plt_y, 1)
plt.imshow(img1, cmap="gray")
plt.axis("off")
plt.title("original grey image 1")

fig.add_subplot(plt_x, plt_y, 2)
plt.imshow(img2, cmap="gray")
plt.axis("off")
plt.title("original grey image 2")

fig.add_subplot(plt_x, plt_y, 3)
plt.imshow(add, cmap="gray")
plt.axis("off")
plt.title("image addition")

fig.add_subplot(plt_x, plt_y, 4)
plt.imshow(subtract, cmap="gray")
plt.axis("off")
plt.title("image subtraction")

fig.add_subplot(plt_x, plt_y, 5)
plt.imshow(multiply, cmap="gray")
plt.axis("off")
plt.title("image multiplication")

fig.add_subplot(plt_x, plt_y, 6)
plt.imshow(divide, cmap="gray")
plt.axis("off")
plt.title("image division")

plt.show()
