import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('berries.jpg', 0)
img2 = cv2.imread('berries1.jpg', 0)
h, w = img1.shape
img3 = np.zeros((h, w), dtype=np.uint8)
for i in range(len(img1)):
    for j in range(len(img1[0])):
        img3[i, j] = (img1[i, j] + img2[i, j]) / 2

fig = plt.figure(figsize=(16, 10))
plt_x = 1
plt_y = 3
fig.add_subplot(plt_x, plt_y, 1)
plt.imshow(img1, cmap="gray")
plt.axis("off")
plt.title("original grey image1")

fig.add_subplot(plt_x, plt_y, 2)
plt.imshow(img2, cmap="gray")
plt.axis("off")
plt.title("original grey image2")

fig.add_subplot(plt_x, plt_y, 3)
plt.imshow(img3, cmap="gray")
plt.axis("off")
plt.title("average image")
plt.show()
