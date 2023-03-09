import cv2 as cv
import numpy as np

filepath = "paradise1.jpg"
img = cv.imread(filepath, 0)

img2 = 255-img
imgs1 = np.hstack((img, img2))
cv.imshow("A)Image B)Negative", imgs1)

img3 = img.copy()
img3 = np.log2(img3)
img3 = 255*(img3/np.max(img3))
img3 = img3.astype(np.uint8)

imgs2 = np.hstack((img, img3))
cv.imshow("A)Image B)Image Log Transform", imgs2)

img4 = img.copy().astype(np.float)
img4 = img4/np.max(img4)
img4 = np.power(img4+1, 2)
img4 = 255*(img4/np.max(img4))
img4 = img4.astype(np.uint8)
imgs3 = np.hstack((img, img2))
cv.imshow("A)Image B)Image Gamma Transform", imgs3)

img5 = img.copy()
img_min = np.min(img5)
img_max = np.max(img5)
band_min = 0
band_max = 255
nimg = (img5-img_min)*((band_max-band_min)/(img_max-img_min))+band_min
print(np.min(nimg), np.max(nimg))
nimg = nimg.astype(np.uint8)
imgs4 = np.hstack((img, nimg))
cv.imshow("Color:: A)Low contrast image B)Contrast Stretched ", imgs4)

cv.waitKey(0)