import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def channelExtract(img):
    row, col, channel = img.shape

    r_chan = np.zeros((row, col), dtype=np.uint8)
    g_chan = np.zeros((row, col), dtype=np.uint8)
    b_chan = np.zeros((row, col), dtype=np.uint8)

    for i, row in enumerate(img):
        for j, col in enumerate(row):
            r, g, b = col

            r_chan[i, j] = r
            g_chan[i, j] = g
            b_chan[i, j] = b

    return [b_chan, g_chan, r_chan]


def rgbToYCbCr(b, g, r, img):
    row, col, channel = img.shape

    ybr = np.zeros((row, col, channel), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            ybr[i, j, 0] = 0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j]
            ybr[i, j, 1] = -0.168736 * r[i, j] - 0.331264 * g[i, j] + 0.500 * b[i, j]
            ybr[i, j, 2] = 0.500 * r[i, j] - 0.418688 * g[i, j] - 0.081312 * b[i, j]

    return ybr


img = mpimg.imread('weiler.jpg')
b, g, r = channelExtract(img)
ycbcr = rgbToYCbCr(b, g, r, img)

fig = plt.figure(figsize=(16, 10))
fig.add_subplot(2, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.title("Original RGB Image")

fig.add_subplot(2, 2, 2)
plt.imshow(ycbcr, cmap="gray")
plt.axis("off")
plt.title("YCbCr Image")

plt.show()
