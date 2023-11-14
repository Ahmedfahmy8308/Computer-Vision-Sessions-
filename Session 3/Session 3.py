import cv2

boat = cv2.imread("Images/boat.jpg")
Red = cv2.imread("Images/RED.png")
Black_White1 = cv2.imread("Images/Black_White.png")
Black_White2 = cv2.imread("Images/Black_White2.png")


#resize the images
Rred = cv2.resize(Red , (720 , 600))
Rboat = cv2.resize(boat , (720 , 600))



# Arithmetic operations
add = cv2.add(Rboat , Rred) 
sub = cv2.subtract(Rboat ,Rred )
Mul = cv2.multiply(Rboat ,Rred)
div = cv2.divide(Rboat ,Rred)

cv2.imshow("Frame1" , add)
cv2.imshow("Frame2" , Rboat)
cv2.imshow("Frame 3" , sub)
cv2.imshow("Frame4" , Mul)
cv2.imshow("Frame 5" , div)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()




#bitwise operations 

and_Image = cv2.bitwise_and(Black_White1 , Black_White2)
or_Image = cv2.bitwise_or(Black_White1 , Black_White2)
not_image = cv2.bitwise_not(Black_White1)

cv2.imshow("Black_White1", Black_White1)
cv2.imshow("Black_White2" ,Black_White2)
cv2.imshow("andFrame" , and_Image)
cv2.imshow("orFrame" , or_Image)
cv2.imshow("notFrame" , not_image)


if cv2.waitKey(0) == ord('q'):
   cv2.destroyAllWindows()






