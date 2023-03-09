import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('boerboel1.jpg', 0)
cv2.imshow("original image", img)


histr = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(histr)
plt.show()

h, w = img.shape[:2]
intensity_count = [0] * 256
new_img = np.zeros(img.shape)
for i in range(0, h):
    for j in range(0, w):
        intensity_count[img[i, j]] += 1
l = 256

res = []
for val in intensity_count:
    res.append(val / img.size)

cum_list = []
k = 0
for x in range(0, len(res)):
    k += res[x]
    cum_list.append(k)

intensity = cum_list * (l - 1)

for x in range(0, h):
    for y in range(0, w):
        new_img[x, y] = intensity[img[x, y]]

cv2.imshow("new image", new_img)

histo, bin_edges = np.histogram(new_img, bins=256, range=(0, 1))
plt.figure()
plt.title("grayscale histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 1.0])
plt.plot(bin_edges[0:-1], histo)
plt.show()
