import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def channelExtraction(img):
    row, col, chan = img.shape

    rchan = np.zeros((row, col), dtype=np.uint8)
    gchan = np.zeros((row, col), dtype=np.uint8)
    bchan = np.zeros((row, col), dtype=np.uint8)

    for i, row in enumerate(img):
        for j, col in enumerate(row):
            r, g, b = col
            rchan[i, j] = r
            gchan[i, j] = g
            bchan[i, j] = b

    return bchan, gchan, rchan


def rgb_to_grey(b, g, r):
    row, col = r.shape
    grey_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grey_chan[i, j] = r[i, j] * 0.30 + g[i, j] * 0.59 + b[i, j] * 0.11

    return grey_chan


def grey_to_binary(grey_image):
    row, col = grey_image.shape
    binary = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            if grey_image[i, j] > 150:
                binary[i, j] = 255
            else:
                binary[i, j] = 0
    return binary


def rgb_to_binary(b, g, r):
    row, col = r.shape
    grey_image = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grey_image[i, j] = r[i, j] * 0.30 + g[i, j] * 0.59 + b[i, j] * 0.11
    row1, col1 = grey_image.shape
    binary = np.zeros((row1, col1), dtype=np.uint8)
    for i1 in range(row1):
        for j1 in range(col1):
            if grey_image[i1, j1] > 150:
                binary[i1, j1] = 255
            else:
                binary[i1, j1] = 0
    return binary


img = mpimg.imread('retriever.jpg')
b, g, r = channelExtraction(img)
greyimg = rgb_to_grey(b, g, r)
binary = grey_to_binary(greyimg)
binary1 = rgb_to_binary(b, g, r)

fig = plt.figure(figsize=(16, 10))
plt_x = 1
plt_y = 4
fig.add_subplot(plt_x, plt_y, 1)
plt.imshow(img)
plt.axis("off")
plt.title("original rgb image")

fig.add_subplot(plt_x, plt_y, 2)
plt.imshow(greyimg, cmap="gray")
plt.axis("off")
plt.title("grey image")

fig.add_subplot(plt_x, plt_y, 3)
plt.imshow(binary, cmap="gray")
plt.axis("off")
plt.title("binary image for grey")

fig.add_subplot(plt_x, plt_y, 4)
plt.imshow(binary1, cmap="gray")
plt.axis("off")
plt.title("binary image for rgb")

plt.show()
