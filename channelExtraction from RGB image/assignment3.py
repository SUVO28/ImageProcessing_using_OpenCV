import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('malamute.jpg')
row, col, channel = img.shape

rCha = np.zeros((row, col), dtype=np.int8)
gCha = np.zeros((row, col), dtype=np.int8)
bCha = np.zeros((row, col), dtype=np.int8)

for i, row in enumerate(img):
    for j, col in enumerate(row):
        r, g, b = col
        rCha[i, j] = r
        gCha[i, j] = g
        bCha[i, j] = b

fig = plt.figure(figsize=(17, 12))
fig.add_subplot(2, 2, 1)
plt.imshow(img)
plt.axis('off')
plt.title('Original image')

fig.add_subplot(2, 2, 2)
plt.imshow(rCha)
plt.axis('off')
plt.title('R channel image')

fig.add_subplot(2, 2, 3)
plt.imshow(gCha)
plt.axis('off')
plt.title('G channel image')

fig.add_subplot(2, 2, 4)
plt.imshow(bCha)
plt.axis('off')
plt.title('B channel image')

plt.show()
