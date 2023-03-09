import cv2
import numpy as np
import matplotlib.pyplot as plt


def channelExtract(img):
    row, col, channel = img.shape

    r_chan = np.zeros((row, col), dtype=np.uint8)
    g_chan = np.zeros((row, col), dtype=np.uint8)
    b_chan = np.zeros((row, col), dtype=np.uint8)

    for i, row in enumerate(img):
        for j, col in enumerate(row):
            b, g, r = col

            r_chan[i, j] = r
            g_chan[i, j] = g
            b_chan[i, j] = b

    return [b_chan, g_chan, r_chan]


def greyConversion(b, g, r):
    row, col = b.shape
    grey_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grey_chan[i, j] = r[i, j] * 0.3 + g[i, j] * 0.59 + b[i, j] * 0.11

    return grey_chan


def histogram(grey_image):
    row, col = grey_image.shape
    hist = np.zeros(256, dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            hist[grey_image[i, j]] += 1
    return hist


img = cv2.imread("paradise.jpg")
b, g, r = channelExtract(img)
greyImage = greyConversion(b, g, r)
hist = histogram(greyImage)

fig = plt.figure(figsize=(17, 12))
pltX = 2
pltY = 1

fig.add_subplot(pltX, pltY, 1)
plt.imshow(greyImage, cmap="gray")
plt.axis("off")
plt.title("grey image")

fig.add_subplot(pltX, pltY, 2)
plt.bar(np.arange(len(hist)), hist)
plt.title("histogram")

plt.show()

