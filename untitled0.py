
import cv2

img = cv2.imread("D://2.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_RGB2YCBCR)

cv2.imshow("image",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()