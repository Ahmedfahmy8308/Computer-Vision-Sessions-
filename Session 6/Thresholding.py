import cv2
import numpy as np


ArrayG = np.ones((400,500) , dtype= "uint8") * 70
cv2.rectangle(ArrayG , (300 , 300) , (50,50) , (220) , -1)


cv2.imshow("ArrayG" , ArrayG)
k = cv2.waitKey(0)

if k == ord('q') :
    cv2.destroyAllWindows()


#  Threshold

ret, thresholded = cv2.threshold(ArrayG, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("thresholded" , thresholded)
k = cv2.waitKey(0)

if k == ord('q') :
    cv2.destroyAllWindows()


sudoko = cv2.imread("Images/sudoku.png" ,cv2.IMREAD_GRAYSCALE)
coins = cv2.imread("Images/Coins.png" , cv2.IMREAD_GRAYSCALE)


ret, thresh_sudoko = cv2.threshold(sudoko, 127, 255, cv2.THRESH_BINARY)


cv2.imshow("Sudoko" ,sudoko)
cv2.imshow("threshBinary_Sudoko" , thresh_sudoko)
k = cv2.waitKey(0)

if k == ord('q') :
    cv2.destroyAllWindows()


# Adaptive Threshold


thresh_sudoko2 = cv2.adaptiveThreshold(sudoko, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 111, 2)


cv2.imshow("Sudoko" ,sudoko)
cv2.imshow("Adaptive_Sudoko" , thresh_sudoko2)
k = cv2.waitKey(0)

if k == ord('q') :
    cv2.destroyAllWindows()


# Otsu Threshold


ret, OTSU = cv2.threshold(coins, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("coins" ,coins)
cv2.imshow("OTSU_Coins" , OTSU)
k = cv2.waitKey(0)

if k == ord('q') :
    cv2.destroyAllWindows()






