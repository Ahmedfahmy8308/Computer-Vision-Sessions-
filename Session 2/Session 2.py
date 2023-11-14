import cv2

##################################################\

boat = cv2.imread(r"Photos\boat.jpg")
red = cv2.imread("Photos/RED.png")
Strawberries = cv2.imread("Photos/Strawberries.jpg")
tumor = cv2.imread("Photos/tumor.jpg")
Vid = cv2.VideoCapture(r"Photos/vid.mp4")

#######################################################


print (boat.shape ,end="\n\n")
cv2.imshow("boat" , boat)
cv2.waitKey(0)

########################################################

print("===================================================")

print("Bfore")
print (red.shape)
cv2.imshow("img" , red)
cv2.waitKey(0)

RRed = cv2.resize(red , (720, 600))

print("After")
print (RRed.shape)
cv2.imshow("Resized img " , RRed)
cv2.waitKey(0)

print("===================================================")

##############################################################






while True :
     Succes , Frame =Vid.read()
     Rframe = cv2.resize(Frame , (720 , 600))

     cv2.imshow("Frame" , Rframe) 
     cv2.waitKey(10)


cv2.destroyAllWindows()

