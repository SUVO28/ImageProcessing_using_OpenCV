import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

filepath = "malamute.jpg"
img = cv.imread(filepath, 0)

r, c = img.shape
noise = np.random.randint(0, 50, [r, c], np.uint8)
img2 = img+noise
diff = np.abs(img-img2)

fig = plt.figure(figsize=(17, 12))

fig.add_subplot(2, 2, 1)
plt.imshow(img)
plt.axis('off')
plt.title('Original image')

fig.add_subplot(2, 2, 2)
plt.imshow(img2)
plt.axis('off')
plt.title('Noisy image')

fig.add_subplot(2, 2, 3)
plt.imshow(diff)
plt.axis('off')
plt.title('Original image - Noisy image')

plt.show()
