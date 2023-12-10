import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'images/Bahgat.jpeg'
Bahgat = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
messi = cv2.imread("images/messi.jpg", cv2.IMREAD_GRAYSCALE)



sobel_x = cv2.Sobel(Bahgat, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(Bahgat, cv2.CV_64F, 0, 1, ksize=3)

abs_sobel_x = np.abs(sobel_x)
abs_sobel_y = np.abs(sobel_y)


gradient_magnitude = np.sqrt(abs_sobel_x**2 + abs_sobel_y**2)


plt.figure(figsize=(20, 10))

plt.subplot(2, 3, 1), plt.imshow(Bahgat, cmap='gray')
plt.title('Original Image'), plt.axis('off')

plt.subplot(2, 3, 2), plt.imshow(abs_sobel_x, cmap='gray')
plt.title('Sobel X'), plt.axis('off')

plt.subplot(2, 3, 3), plt.imshow(abs_sobel_y, cmap='gray')
plt.title('Sobel Y'), plt.axis('off')

plt.subplot(2, 3, 4), plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude'), plt.axis('off')

plt.show()



sobel_x = cv2.Sobel(messi, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(messi, cv2.CV_64F, 0, 1, ksize=3)


abs_sobel_x = np.abs(sobel_x)
abs_sobel_y = np.abs(sobel_y)

gradient_magnitude = np.sqrt(abs_sobel_x**2 + abs_sobel_y**2)

plt.figure(figsize=(30, 15))

plt.subplot(2, 3, 1), plt.imshow(messi, cmap='gray')
plt.title('Original Image'), plt.axis('off')

plt.subplot(2, 3, 2), plt.imshow(abs_sobel_x, cmap='gray')
plt.title('Sobel X'), plt.axis('off')

plt.subplot(2, 3, 3), plt.imshow(abs_sobel_y, cmap='gray')
plt.title('Sobel Y'), plt.axis('off')

plt.subplot(2, 3, 4), plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude'), plt.axis('off')

plt.show()

image = cv2.imread('images/Rose.jpg', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 100)

plt.figure(figsize=(20, 10))
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show()


