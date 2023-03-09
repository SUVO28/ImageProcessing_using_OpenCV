import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

lena = mpimg.imread("paradise.jpg")
peppers = cv2.imread("paradise1.jpg")

rows, cols, _ = lena.shape

J = np.zeros((rows, cols, _), dtype=np.uint8)
for i in range(rows):
    for j in range(0, int(cols / 2)):
        J[i, j] = lena[i, j]
for i in range(rows):
    for j in range(int(cols / 2), cols):
        J[i, j] = peppers[i, j]

fig = plt.figure(figsize=(16, 10))
plt_x = 1
plt_y = 3
fig.add_subplot(plt_x, plt_y, 1)
plt.imshow(lena)
plt.axis("off")
plt.title("original image 1")

fig.add_subplot(plt_x, plt_y, 2)
plt.imshow(peppers)
plt.axis("off")
plt.title("original image 2")

fig.add_subplot(plt_x, plt_y, 3)
plt.imshow(J)
plt.axis("off")
plt.title("combined image")

plt.show()
