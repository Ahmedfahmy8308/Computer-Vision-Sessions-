import cv2
import numpy as np


image_1 = np.ones((500, 500, 3), np.uint8) * 255
image_2 = np.ones((500, 500, 3), np.uint8) * 255



cv2.line(image_1, (0, 0), (500, 500), (0, 0, 0), 3)
cv2.line(image_1, (0, 500), (500, 0), (0, 0, 0), 3)

cv2.rectangle(image_1, (50, 50), (450, 450), (0, 0, 255), 3)
cv2.circle(image_1, (250, 250), 150, (0, 255, 0), 5)
cv2.circle(image_1, (250, 250), 50, (0, 0, 255), -1)

cv2.putText(image_1, "Open CV with Python", (100, 30), cv2.FONT_ITALIC, 1, (0, 0, 0),4)

pts = np.array([[250, 250], [150, 150], [350, 150]])
cv2.polylines(image_1, [pts], 0, (0, 255, 255), 3)



#  Drawing Palestine flag

cv2.rectangle(image_2, (0, 0), (450, 100), (0, 0, 0), -1)
cv2.rectangle(image_2, (0, 100), (450, 200), (255, 255, 255),-1)
cv2.rectangle(image_2, (0, 200), (450, 300), (0, 255, 0), -1)


pts = np.array([[0, 0], [0, 300], [150, 150]])
cv2.fillPoly(image_2, [pts], color=(0, 0, 255))


img = np.hstack([image_2,image_1])

cv2.imshow("img", img)
cv2.imwrite("drawing.png", img)
cv2.waitKey(0)

